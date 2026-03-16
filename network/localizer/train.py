"""
Training script for the bounding box localization model

This module trains a localization head on top of a pretrained
backbone network using Complete IoU (CIoU) loss. The training
process progressively unfreezes backbone layers to allow
fine-tuning during later epochs

Usage:
    Run only after pretraining the backbone network with the classification head!

    py train.py
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

# Models
from network.backbone.model import Backbone
from network.localizer.model import Localizer

from datetime import datetime


EPOCHS = 50
BATCH_SIZE = 16
NUM_WORKERS = 4
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

def run_epoch(
        backbone: nn.Module, localizer: nn.Module,
        dataloader: DataLoader, optimizer: optim.Optimizer | None = None) -> EpochMetrics:
    """
    Runs a single training or evaluation epoch

    :param backbone: Feature extractor network
    :param localizer: Bounding box regression head
    :param dataloader: Dataset loader
    :param optimizer: If provided, runs in training mode

    :return:
        EpochMetrics with loss and CIoU score
    """
    is_train = optimizer is not None

    if is_train:
        backbone.train()
        localizer.train()
    else:
        backbone.eval()
        localizer.eval()

    # Metrics
    total_loss = 0.0
    total_ciou = 0.0

    batches = 0

    grad_context = torch.enable_grad() if is_train else torch.no_grad()

    with grad_context:
        for img, target in dataloader:
            img = img.to(device)
            # Target comes as a list of dicts -> extract bounding boxes and combine into tensor with dtype torchvision.tv_tensors.BoundingBoxes
            bboxes = torch.cat([t["bbox"] for t in target]).to(device)

            features = backbone(img)
            predicted_bboxes = localizer(features)

            true_xyxy = ops.box_convert(bboxes, in_fmt="cxcywh", out_fmt="xyxy")
            pred_xyxy = ops.box_convert(predicted_bboxes, in_fmt="cxcywh", out_fmt="xyxy")

            # Loss CIoU function
            ciou_loss = ops.complete_box_iou_loss(true_xyxy, pred_xyxy).mean()  # (16,).mean()

            loss = ciou_loss

            # Compute mean CIoU for the batch
            ciou = ops.complete_box_iou(true_xyxy, pred_xyxy).diagonal().mean()

            if is_train:
                optimizer.zero_grad()
                loss.backward()
                optimizer.step()

            total_loss += loss.item()
            total_ciou += ciou.item()

            batches += 1

        return EpochMetrics(loss=total_loss / batches, ciou=total_ciou / batches)

def train():
    backbone = Backbone().to(device)

    params = torch.load("../../weights/backbone.pt", map_location=device)
    backbone.load_state_dict(params)

    for param in backbone.parameters():
        param.requires_grad = False

    # Unfreeze block 4 only to fine tune params
    for param in backbone.block4.parameters():
        param.requires_grad = True

    localizer = Localizer().to(device)

    # Datasets
    dataset_train = DataLoader(train_dataset.batched(BATCH_SIZE), num_workers=NUM_WORKERS, pin_memory=True, batch_size=None)
    dataset_test = DataLoader(test_dataset.batched(BATCH_SIZE), num_workers=NUM_WORKERS, pin_memory=True, batch_size=None)

    # Optimizer
    optimizer = optim.AdamW([
        {"params": localizer.parameters(), "lr": 1e-04, "weight_decay": 1e-03},
        {"params": backbone.block4.parameters(), "lr": 1e-04, "weight_decay": 1e-03}
    ])

    scheduler = optim.lr_scheduler.MultiStepLR(optimizer, milestones=[15, 25, 35, 45], gamma=0.5)

    timer = datetime.now()

    # Collect plotting params
    train_metrics = []
    test_metrics = []

    for epoch in range(EPOCHS):
        # Unfreeze backbone's block 3 on 15th epoch
        if epoch == 15:
            for param in backbone.block3.parameters():
                param.requires_grad = True

            optimizer.add_param_group(
                {"params": backbone.block3.parameters(), "lr": 5e-05, "weight_decay": 1e-04}
            )

        # Unfreeze whole backbone on 20th epoch
        if epoch == 20:
            for param in backbone.block2.parameters():
                param.requires_grad = True
            for param in backbone.block1.parameters():
                param.requires_grad = True
            for param in backbone.conv.parameters():
                param.requires_grad = True

            optimizer.add_param_group(
                {"params": backbone.block2.parameters(), "lr": 5e-05, "weight_decay": 1e-04},
            )
            optimizer.add_param_group(
                {"params": backbone.block1.parameters(), "lr": 5e-05, "weight_decay": 1e-04},
            )
            optimizer.add_param_group(
                {"params": backbone.conv.parameters(), "lr": 5e-05, "weight_decay": 1e-04},
            )

        # Train dataset
        train_output = run_epoch(backbone, localizer, dataset_train, optimizer)
        train_metrics.append(train_output)

        # Test dataset
        test_output = run_epoch(backbone, localizer, dataset_test)
        test_metrics.append(test_output)

        lrs = scheduler.get_last_lr()
        train_time = str(datetime.now() - timer).split(".")[0]

        # Prints
        print(f"#{epoch + 1} Time: {train_time} | ", end="")
        print(f"Train Loss: {train_output.loss:.4f} | Test Loss: {test_output.loss:.4f} | ", end="")
        print(f"Train CIoU: {train_output.ciou:.4f} | Test CIoU: {test_output.ciou:.4f} | ", end="")
        print(f"LR-loc: {lrs[0]} | LR-bck: {lrs[1]}")

        scheduler.step()

    # Plotting
    plot_training_results(train_metrics, test_metrics, metrics=["loss", "ciou"])

    torch.save(backbone.state_dict(), "../../weights/backbone.pt")
    torch.save(localizer.state_dict(), "../../weights/localizer.pt")

if __name__ == "__main__":
    train()