"""
Training script for the image classifier

This module trains a classifier on top of a backbone feature extractor
using PyTorch. It performs training and evaluation across multiple epochs,
tracks metrics, and saves trained model weights

Usage:
    py train.py
"""

import torch
from torch import nn
from torch import optim

# Models
from network.backbone.model import Backbone
from network.classifier.model import Classifier

# Data
from data.loader import train_dataset, test_dataset
from torch.utils.data import DataLoader

from network.utils.metrics import EpochMetrics

from network.utils.plot import plot_training_results

from datetime import datetime


EPOCHS = 30
BATCH_SIZE = 16
NUM_WORKERS = 4
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

def run_epoch(
        backbone: nn.Module, classifier: nn.Module,
        dataloader: DataLoader, loss_func: nn.Module,
        optimizer: optim.Optimizer | None = None) -> EpochMetrics:
    """
    Runs a single training or evaluation epoch

    :param backbone: Feature extractor network
    :param classifier: Classification head
    :param dataloader: Dataset loader
    :param loss_func: Loss function used for optimization
    :param optimizer: If provided, runs in training mode

    :return:
        EpochMetrics with loss and accuracy
    """
    is_train = optimizer is not None

    if is_train:
        backbone.train()
        classifier.train()
    else:
        backbone.eval()
        classifier.eval()

    # Metrics
    correct = 0
    total = 0

    total_loss = 0.0

    batches = 0

    grad_context = torch.enable_grad() if is_train else torch.no_grad()

    with grad_context:
        for img, target in dataloader:
            img = img.to(device)
            # Targets come as a list of dicts -> extract labels into tensor with dtype int64
            labels = torch.cat([t["label"] for t in target]).to(device).long()

            features = backbone(img)
            logits = classifier(features)

            loss = loss_func(logits, labels)

            if is_train:
                optimizer.zero_grad()
                loss.backward()
                optimizer.step()

            predicted = logits.argmax(dim=1)

            # Metrics
            correct += (predicted == labels).sum().item()
            total += labels.size(0)

            total_loss += loss.item()

            batches += 1

        return EpochMetrics(loss=total_loss / batches, accuracy=correct / total)

def train():
    backbone = Backbone().to(device)
    classifier = Classifier().to(device)

    # Datasets
    dataset_train = DataLoader(train_dataset.batched(BATCH_SIZE), num_workers=NUM_WORKERS, pin_memory=True, batch_size=None)
    dataset_test = DataLoader(test_dataset.batched(BATCH_SIZE), num_workers=NUM_WORKERS, pin_memory=True, batch_size=None)

    # Current dataset was disbalanced -> weight parameter is used in loss function
    loss = nn.CrossEntropyLoss(weight=torch.tensor([2.08, 1.0]).to(device), label_smoothing=0.1)

    optimizer = optim.AdamW([
        {'params': backbone.parameters(),  "lr": 1e-04, "weight_decay": 1e-03},
        {'params': classifier.parameters(), "lr": 1e-04, "weight_decay": 1e-03}
    ])

    scheduler = optim.lr_scheduler.MultiStepLR(optimizer, milestones=[10, 20, 25], gamma=0.5)

    timer = datetime.now()

    # Collect plotting params
    train_metrics = []
    test_metrics = []

    for epoch in range(EPOCHS):
        # Train dataset
        train_output = run_epoch(backbone, classifier, dataset_train, loss, optimizer=optimizer)
        train_metrics.append(train_output)

        # Test dataset
        test_output = run_epoch(backbone, classifier, dataset_test, loss)
        test_metrics.append(test_output)

        lrs = scheduler.get_last_lr()
        train_time = str(datetime.now() - timer).split(".")[0]

        # Prints
        print(f"#{epoch + 1} Time: {train_time} | ", end="")
        print(f"Train Loss: {train_output.loss:.4f} | Test Loss: {test_output.loss:.4f} | ", end="")
        print(f"Train Acc: {train_output.accuracy * 100:.2f}% | Test Acc: {test_output.accuracy * 100:.2f}% | ", end="")
        print(f"Gaps: {test_output.loss - train_output.loss:.4f} / {(test_output.accuracy - train_output.accuracy) * 100:.2f}% | ", end="")
        print(f"LR-cls: {lrs[1]} | LR-bck: {lrs[0]}")

        scheduler.step()

    # Plotting
    plot_training_results(train_metrics, test_metrics, metrics=["loss", "accuracy"])

    torch.save(backbone.state_dict(), "../../weights/backbone.pt")
    torch.save(classifier.state_dict(), "../../weights/classifier.pt")


if __name__ == "__main__":
    train()