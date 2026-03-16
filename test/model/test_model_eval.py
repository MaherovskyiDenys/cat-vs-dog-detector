import torch
from torch import nn

# Plot
import matplotlib.pyplot as plt

# Data
import webdataset as wds
from data.loader import test_dataset

# Hint
from torch.utils.data import DataLoader

# Model
from network.classifier.model import Classifier

def run_epoch(model: nn.Module, dataloader: DataLoader, loss_func: nn.Module):
    wrong_img = []
    wrong_labels = []

    correct = 0
    total = 0
    total_loss = 0.0
    batches = 0

    model.eval()
    with torch.no_grad():
        for data, targets in dataloader:
            data = data.to(device)
            target = torch.cat([t["label"] for t in targets]).to(device).long()

            _, logits = model(data)
            loss = loss_func(logits, target)

            predicted = logits.argmax(dim=1)

            if predicted != target:
                wrong_img.append(data)
                wrong_labels.append(predicted)

            correct += (predicted == target).sum().item()
            total += target.size(0)
            total_loss += loss.item()
            batches += 1

        return wrong_img, wrong_labels

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

model = Classifier()
model.to(device)

params = torch.load("weights.pt", map_location=device)
model.load_state_dict(params)

dataset_test = wds.WebLoader(test_dataset.batched(1), pin_memory=True, batch_size=None)

loss_function = nn.CrossEntropyLoss()

imgs, labels = run_epoch(model, dataset_test, loss_function)

mean = torch.tensor([0.479, 0.446, 0.395]).view(3, 1, 1).cpu()
std = torch.tensor([0.262, 0.257, 0.265]).view(3, 1, 1).cpu()

for i in range(len(imgs)):
    denorm = ((imgs[i].squeeze().cpu() * std) + mean).permute(1, 2, 0)
    label = "cat" if labels[i].item() == 0 else "dog"

    plt.imshow(denorm)
    plt.title(f"Predicted: {label.capitalize()}")
    plt.show()
