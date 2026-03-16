import torch
from torchvision.tv_tensors import BoundingBoxes

label = 1

x_min = 20
y_min = 30
x_max = 220
y_max = 230

box = torch.tensor([[x_min, y_min, x_max, y_max]], dtype=torch.float32)
height, width = 256, 256

bbox = BoundingBoxes(
    box,
    format="XYXY",
    canvas_size=(height, width)
)

target = {
    "label": torch.tensor([label]),
    "bbox": bbox
}

torch.save(target, "file.pt")

target = torch.load("file.pt", weights_only=False)
print(type(target))
"""
{
    'label': tensor([1]), 
    'bbox': BoundingBoxes([[ 20.,  30., 220., 230.]], format=BoundingBoxFormat.XYXY, canvas_size=(256, 256), clamping_mode=soft)
}
"""