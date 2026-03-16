"""
Localization head for bounding box regression

This module takes backbone feature maps and predicts
a single bounding box per image using a small CNN
followed by a fully connected regression head
"""

from torch import nn

class Localizer(nn.Module):
    def __init__(self):
        super().__init__()

        self.features = nn.Sequential(
            nn.Conv2d(512, 256, 3, padding=1),
            nn.BatchNorm2d(256),
            nn.ReLU(inplace=True),

            nn.Conv2d(256, 128, 3, padding=1),
            nn.BatchNorm2d(128),
            nn.ReLU(inplace=True),

            nn.Conv2d(128, 64, 3, padding=1),
            nn.BatchNorm2d(64),
            nn.ReLU(inplace=True),

            nn.AdaptiveAvgPool2d((7, 7))
        )

        self.regressor = nn.Sequential(
            nn.Flatten(),
            nn.Linear(64 * 7 * 7, 512),
            nn.Dropout(0.2),
            nn.ReLU(inplace=True),

            nn.Linear(512, 128),
            nn.ReLU(inplace=True),

            nn.Linear(128, 4),
            # Output normalized bounding box coordinates in range [0, 1]
            nn.Sigmoid()
        )

    def forward(self, x):
        """
        Forward pass of the localization head

        :param x: Feature tensor from the backbone of shape (B, 512, H, W)
        :return:
            Bounding box predictions of shape (B, 4) in normalized
            coordinates (cx, xy, w, h).
        """
        x = self.features(x)
        return self.regressor(x)