import io
from pathlib import Path

import torch
from torchvision.transforms import v2

import webdataset as wds
from torchvision.tv_tensors import BoundingBoxes

base = Path(__file__).parent.resolve()

test_folder = f"file://{base.joinpath("test/catsvsdogs-test-{0001..0006}.tar").as_posix()}"
train_folder = f"file://{base.joinpath("train/catsvsdogs-train-{0001..0024}.tar").as_posix()}"

train_transform = v2.Compose([
    v2.ToDtype(torch.float32, scale=True),
    v2.Resize((448, 448)),
    # v2.RandomCrop(size=(412, 412)),  # Uncomment when training classifier
    v2.RandomHorizontalFlip(p=0.5),
    v2.ColorJitter(brightness=0.125, contrast=0.125, saturation=0.1),
    v2.RandomGrayscale(0.2),
    v2.Normalize(
        mean=[0.479, 0.446, 0.395],
        std=[0.262, 0.257, 0.265]
    )
])

test_transform = v2.Compose([
    v2.ToDtype(torch.float32, scale=True),
    v2.Resize((448, 448)),
    v2.Normalize(
        mean=[0.479, 0.446, 0.395],
        std=[0.262, 0.257, 0.265]
    )
])


def convert_and_normalize(box: BoundingBoxes):
    """
    Takes Bounding boxs and converts them into CXCYWH yolo format
    Normalizes them

    :param box: Bounding box dtype torchvision.tv_tensors.BoundingBoxes
    :return: Converted and Normalized Bounding Box
    """
    converter = v2.ConvertBoundingBoxFormat("CXCYWH")
    box = converter(box)

    # Normalize
    h, w = box.canvas_size
    box[:, 0] /= w
    box[:, 1] /= h
    box[:, 2] /= w
    box[:, 3] /= h

    return box

def apply_train_transform(sample):
    """Apply transform on img and label, converts bbox format"""
    img, target = sample
    img, target = train_transform(img, target)

    target["bbox"] = convert_and_normalize(target["bbox"])

    return img, target

def apply_test_transform(sample):
    """Apply transform on img and label, converts bbox format"""
    img, target = sample
    img, target = test_transform(img, target)

    target["bbox"] = convert_and_normalize(target["bbox"])

    return img, target

def translate(b: bytes):
    """Convert from bytes to dict"""
    return torch.load(io.BytesIO(b), weights_only=False)

train_dataset = (wds.WebDataset
                (train_folder, shardshuffle=False)
                .shuffle(1000)
                .decode("torch")
                .map_dict(pt=translate)
                .to_tuple("png", "pt")
                .map(apply_train_transform)
                )

test_dataset = (wds.WebDataset
                (test_folder, shardshuffle=False)
                .decode("torch")
                .map_dict(pt=translate)
                .to_tuple("png", "pt")
                .map(apply_test_transform)
                )
