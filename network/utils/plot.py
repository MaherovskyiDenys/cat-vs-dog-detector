import matplotlib.pyplot as plt
from typing import List
from network.utils.metrics import EpochMetrics


def plot_training_results(train: List[EpochMetrics], test: List[EpochMetrics], metrics: List[str] = None):
    """
    Dynamically plots any available metrics from EpochMetrics

    :param train: List of results for train dataset.
    :param test: List of results for test dataset.
    :param metrics: List of attribute names to plot (e.g., ['loss', 'accuracy', 'ciou'])
    """
    if not metrics:
        metrics = [k for k, v in train[0].__dict__.items() if v is not None]

    num_metrics = len(metrics)
    fig, axes = plt.subplots(1, num_metrics, figsize=(5 * num_metrics, 5))

    if num_metrics == 1:
        axes = [axes]

    labels = {
        "loss": "Loss",
        "accuracy": "Accuracy (%)",
        "ciou": "CIoU"
    }

    for ax, attr in zip(axes, metrics):
        # Extract data multiply by 100 if it's accuracy for percentage view
        train_vals = [getattr(m, attr) * (100 if attr == "accuracy" else 1) for m in train]
        test_vals = [getattr(m, attr) * (100 if attr == "accuracy" else 1) for m in test]

        ax.plot(train_vals, label="Train", linewidth=2)
        ax.plot(test_vals, label="Test", linestyle="--")

        ax.set_title(labels.get(attr, attr.capitalize()))
        ax.set_xlabel("Epoch")
        ax.set_ylabel(labels.get(attr, attr.capitalize()))
        ax.legend()
        ax.grid(True, alpha=0.3)

    plt.tight_layout()
    plt.show()