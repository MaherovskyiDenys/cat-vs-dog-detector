import torch
from torch import nn


class Classifier(nn.Module):
    def __init__(self):
        super().__init__()

        self.flatten = nn.Flatten()
        self.pool = nn.AdaptiveAvgPool2d((1, 1))

        self.fc = nn.Sequential(
            nn.Dropout(0.1),
            nn.Linear(512,2)
        )

    def forward(self, x: torch.Tensor):
        """
        Features from a backbone passed as tensor x

        which are then pooled to 1x1 shape, flatten, and then run through FC

        :param x: Tensor dims [n, 512, h, w]
        :return: Raw predicted logits dims [n, 2]
        """
        features_pooled = self.pool(x)
        flatten = self.flatten(features_pooled)

        return self.fc(flatten)