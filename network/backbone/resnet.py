import torch
from torch import nn


class ResBlock(nn.Module):
    def __init__(self, in_channels: int, out_channels: int, stride: int|tuple[int, int] = 1):
        super().__init__()

        self.in_channels = in_channels
        self.out_channels = out_channels
        self.stride = stride

        self.block = nn.Sequential(
            nn.Conv2d(self.in_channels, self.out_channels, 3, stride=self.stride, padding=1),
            nn.BatchNorm2d(self.out_channels),
            nn.ReLU(inplace=True),
            nn.Conv2d(self.out_channels, self.out_channels, 3, padding=1),
            nn.BatchNorm2d(self.out_channels)
        )

        self.shortcut = nn.Sequential()
        if stride != 1 or in_channels != out_channels:
            self.shortcut = nn.Sequential(
                nn.Conv2d(in_channels, out_channels, 1, stride=stride, bias=False),
                nn.BatchNorm2d(out_channels)
            )

        self.activation = nn.ReLU()

    def forward(self, x: torch.Tensor):
        output = self.block(x)

        output += self.shortcut(x)

        return self.activation(output)