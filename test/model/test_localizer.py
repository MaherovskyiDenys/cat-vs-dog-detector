import torch
from torch import nn
from torchvision.ops import box_iou, complete_box_iou_loss, generalized_box_iou
from torchvision.ops import box_convert

from torchvision.utils import draw_bounding_boxes
import torchvision
import matplotlib.pyplot as plt

# Data
from data.loader import test_dataset, train_dataset

# Models
from network.backbone.model import Backbone
from network.localizer.model import Localizer

from torch.utils.data import DataLoader

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

mean = torch.tensor([0.479, 0.446, 0.395]).view(3, 1, 1).to(device)
std = torch.tensor([0.262, 0.257, 0.265]).view(3, 1, 1).to(device)


def run_epoch(backbone: nn.Module, localizer: nn.Module, dataloader: DataLoader):
    backbone.eval()
    localizer.eval()
    cnt = 0

    with torch.no_grad():
        for img, label in dataloader:
            img = img.to(device)
            # target_label = label['label'].to(device)
            box = label['bbox'].to(device)

            features = backbone(img.unsqueeze(0))
            predicted_bbox = localizer(features)

            # Denorm * std + mean
            img = img * std + mean

            # Denormalize pred-box/true-box values from 0-1 to 0-255
            h, w = box.canvas_size

            box[:, 0] *= w
            box[:, 1] *= h
            box[:, 2] *= w
            box[:, 3] *= h

            predicted_bbox[:, 0] *= w
            predicted_bbox[:, 1] *= h
            predicted_bbox[:, 2] *= w
            predicted_bbox[:, 3] *= h

            true_xyxy = box_convert(box, in_fmt="cxcywh", out_fmt="xyxy")
            pred_xyxy = box_convert(predicted_bbox, in_fmt="cxcywh", out_fmt="xyxy")

            # 2 boxes to 1 tensor
            bboxes = torch.cat([true_xyxy, pred_xyxy])

            iou = box_iou(true_xyxy, pred_xyxy)

            if iou <= 0.2:
                # Draw box
                cnt += 1
                plot_image_bbox = draw_bounding_boxes(img, bboxes, width=3, colors=["green", "red"])

                # transform this image to PIL image
                image_to_show = torchvision.transforms.ToPILImage()(plot_image_bbox)

                plt.imshow(image_to_show)
                plt.title(f"IoU: {iou.item():.2f}")
                plt.show()

        return cnt


def train():
    # Backbone
    backbone = Backbone()
    backbone.to(device)

    params = torch.load("../weights/backbone.pt", map_location=device)
    backbone.load_state_dict(params)

    # Localizer
    localizer = Localizer()
    localizer.to(device)

    params = torch.load("../weights/localizer.pt", map_location=device)
    localizer.load_state_dict(params)

    # Datasets
    dataset_train = DataLoader(train_dataset.batched(16), num_workers=4, pin_memory=True, batch_size=None)
    dataset_test = DataLoader(test_dataset.batched(16), num_workers=4, pin_memory=True, batch_size=None)

    cnt = run_epoch(backbone, localizer, dataset_test)
    print(cnt)

if __name__ == "__main__":
    train()