"""
Combined detection model for cat vs dog detection

This module integrates the backbone feature extractor,
a bounding box localization head, and a classification
head into a single network.
"""

import torch
from torch import nn

from network.backbone.model import Backbone
from network.localizer.model import Localizer
from network.classifier.model import Classifier


class CatVsDogDetector(nn.Module):
    def __init__(self):
        super().__init__()

        self.backbone = Backbone()
        self.localizer = Localizer()
        self.classifier = Classifier()

    def forward(self, img: torch.Tensor):
        """
        Forward pass combining backbone feature extraction with
        classification and localization heads

        :param img: Batch of images with dims (B, C, H, W)
        :return:
            logits: Tensor of shape (B, num_classes)
            bbox: Tensor of shape (B, 4) with (cx, cy, w, h)
        """
        features = self.backbone(img)

        return {
            "logits": self.classifier(features),
            "bbox": self.localizer(features)
        }