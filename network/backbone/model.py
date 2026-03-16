import torch
from torch import nn
from network.backbone.resnet import ResBlock


class Backbone(nn.Module):
    def __init__(self):
        super().__init__()

        # Convolutional
        self.conv = nn.Sequential(
            nn.Conv2d(3, 64, 7, stride=2, padding=3),
            nn.BatchNorm2d(64),
            nn.ReLU(inplace=True)
        )

        # ResNet-18 blocks
        self.block1 = nn.Sequential(
            ResBlock(64, 64, stride=2),
            ResBlock(64, 64)
        )
        self.block2 = nn.Sequential(
            ResBlock(64, 128, stride=2),
            ResBlock(128, 128)
        )
        self.block3 = nn.Sequential(
            ResBlock(128, 256, stride=2),
            ResBlock(256, 256)
        )
        self.block4 = nn.Sequential(
            ResBlock(256, 512, stride=2),
            ResBlock(512, 512)
        )

    def forward(self, x: torch.Tensor):
        c = self.conv(x)

        b1 = self.block1(c)
        b2 = self.block2(b1)
        b3 = self.block3(b2)
        features = self.block4(b3)

        return features