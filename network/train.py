"""
Training script for the full CatVsDogDetector model

This script fine-tunes the combined detection model consisting of:
    - a pretrained backbone feature extractor
    - a classification head
    - a bounding box localization head

The model is initialized from separately pretrained components
and trained using a combination of classification loss and
Complete IoU (CIoU) localization loss

Usage:
    Run after training the backbone, classifier, and localizer!

    python train.py
"""

import torch
from torch import nn
from torch import optim

from torchvision import ops

# Data
from data.loader import train_dataset, test_dataset
from torch.utils.data import DataLoader

from network.utils.metrics import EpochMetrics

from network.utils.plot import plot_training_results

from network.model import CatVsDogDetector

from datetime import datetime


EPOCHS = 50
BATCH_SIZE = 16
NUM_WORKERS = 4
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

def run_epoch(
        model: nn.Module, dataloader: DataLoader,
        loss_func: nn.Module, optimizer: optim.Optimizer | None = None) -> EpochMetrics:
    """
    Runs a single training or evaluation epoch

    Combines losses

    :param model: CatVsDog Detector model(backbone/classifier/localizer)
    :param dataloader: Dataset loader
    :param loss_func: Loss function used for optimization used for classification
    :param optimizer: If provided, runs in training mode

    :return:
        EpochMetrics with loss and accuracy and CIoU scores
    """

    is_train = optimizer is not None

    if is_train:
        model.train()
    else:
        model.eval()

    # Metrics
    correct = 0
    total = 0

    total_loss = 0.0
    total_ciou = 0.0

    batches = 0

    grad_context = torch.enable_grad() if is_train else torch.no_grad()

    with grad_context:
        for img, target in dataloader:
            img = img.to(device)
            # Targets come as a list of dicts -> extract labels into tensor with dtype int64
            labels = torch.cat([t["label"] for t in target]).to(device).long()
            # Target comes as a list of dicts -> extract bounding boxes and combine into tensor with dtype torchvision.tv_tensors.BoundingBoxes
            bboxes = torch.cat([t["bbox"] for t in target]).to(device)

            output = model(img)
            predicted_logits = output["logits"]
            predicted_bboxes = output["bbox"]

            true_xyxy = ops.box_convert(bboxes, in_fmt="cxcywh", out_fmt="xyxy")
            pred_xyxy = ops.box_convert(predicted_bboxes, in_fmt="cxcywh", out_fmt="xyxy")

            # Losses
            loss_classifier = loss_func(predicted_logits, labels)
            loss_localizer = ops.complete_box_iou_loss(true_xyxy, pred_xyxy).mean()

            # 0.5 because normally loss from classifier is way bigger than loss from localizer
            loss = 1.0 * loss_localizer + 0.5 * loss_classifier

            # Compute mean CIoU for the batch
            ciou = ops.complete_box_iou(true_xyxy, pred_xyxy).diagonal().mean()  # (x, y).diagonal().mean()

            if is_train:
                optimizer.zero_grad()
                loss.backward()
                optimizer.step()

            predicted = predicted_logits.argmax(dim=1)

            correct += (predicted == labels).sum().item()
            total += labels.size(0)

            total_loss += loss.item()
            total_ciou += ciou.item()

            batches += 1

        return EpochMetrics(loss=total_loss / batches, accuracy=correct / total, ciou=total_ciou / batches)

def train():
    model = CatVsDogDetector().to(device)

    params = torch.load("../weights/backbone.pt", map_location=device)
    model.backbone.load_state_dict(params)

    params = torch.load("../weights/localizer.pt", map_location=device)
    model.localizer.load_state_dict(params)

    params = torch.load("../weights/classifier.pt", map_location=device)
    model.classifier.load_state_dict(params)

    for param in model.backbone.parameters():
        param.requires_grad = False

    # Unfreeze block 4 only to fine-tune params
    for param in model.backbone.block4.parameters():
        param.requires_grad = True

    # Datasets
    dataset_train = DataLoader(train_dataset.batched(BATCH_SIZE), num_workers=NUM_WORKERS, pin_memory=True, batch_size=None)
    dataset_test = DataLoader(test_dataset.batched(BATCH_SIZE), num_workers=NUM_WORKERS, pin_memory=True, batch_size=None)

    # Current dataset was disbalanced -> weight parameter is used in loss function for classifier
    loss = nn.CrossEntropyLoss(weight=torch.tensor([2.08, 1.0]).to(device), label_smoothing=0.1)

    # Optimizer
    optimizer = optim.AdamW([
        {"params": model.localizer.parameters(), "lr": 1e-04, "weight_decay": 1e-04},
        {"params": model.classifier.parameters(), "lr": 1e-04, "weight_decay": 1e-04},
        {"params": model.backbone.block4.parameters(), "lr": 1e-05, "weight_decay": 1e-04}
    ])

    scheduler = optim.lr_scheduler.ReduceLROnPlateau(optimizer, mode='max', factor=0.5, patience=3)

    timer = datetime.now()

    # Collect plotting params
    train_metrics = []
    test_metrics = []

    for epoch in range(EPOCHS):
        # Unfreeze backbone's block 3
        if epoch == 5:
            for param in model.backbone.block3.parameters():
                param.requires_grad = True

            optimizer.add_param_group(
                {"params": model.backbone.block3.parameters(), "lr": 1e-05, "weight_decay": 1e-05}
            )

        # Unfreeze whole backbone
        if epoch == 10:
            for param in model.backbone.block2.parameters():
                param.requires_grad = True
            for param in model.backbone.block1.parameters():
                param.requires_grad = True
            for param in model.backbone.conv.parameters():
                param.requires_grad = True

            optimizer.add_param_group(
                {"params": model.backbone.block2.parameters(), "lr": 1e-05, "weight_decay": 1e-05},
            )
            optimizer.add_param_group(
                {"params": model.backbone.block1.parameters(), "lr": 1e-05, "weight_decay": 1e-05},
            )
            optimizer.add_param_group(
                {"params": model.backbone.conv.parameters(), "lr": 1e-05, "weight_decay": 1e-05},
            )

        # Train dataset
        train_output = run_epoch(model, dataset_train, loss, optimizer)
        train_metrics.append(train_output)

        # Test dataset
        test_output = run_epoch(model, dataset_test, loss)
        test_metrics.append(test_output)

        lrs = scheduler.get_last_lr()
        train_time = str(datetime.now() - timer).split(".")[0]

        # Prints
        print(f"#{epoch + 1} Time: {train_time} | ", end="")
        print(f"Train Loss: {train_output.loss:.4f} | Test Loss: {test_output.loss:.4f} | ", end="")
        print(f"Train Acc: {train_output.accuracy * 100:.2f}% | Test Acc: {test_output.accuracy * 100:.2f}% | ", end="")
        print(f"Train CIoU: {train_output.ciou:.4f} | Test CIoU: {test_output.ciou:.4f} | ", end="")
        print(f"LR-loc: {lrs[0]} | LR-cls: {lrs[1]} | LR-bck: {lrs[2]}")

        # Tracking test_output.ciou for our loss scheduler
        scheduler.step(test_output.ciou)

    # Plotting
    plot_training_results(train_metrics, test_metrics, metrics=["loss", "accuracy", "ciou"])

    torch.save(model.state_dict(), "../weights/catvsdogdetector.pt")


if __name__ == "__main__":
    train()