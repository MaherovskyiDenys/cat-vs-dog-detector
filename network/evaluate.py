"""
Evaluate CatVsDogDetector on a single image.

Loads a trained model, runs inference on an input image,
and saves a PNG with predicted bounding box and class label.

Usage:
    py -m network.evaluate <model.pt> <image> <output_dir>
"""

import torch

from network.model import CatVsDogDetector

from torchvision.io import read_image, write_png
from torchvision.transforms import v2

from torchvision.utils import draw_bounding_boxes
from torchvision.ops import box_convert

from pathlib import Path

import argparse


device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

def get_args():
    """
    Parses given arguments from terminal

    Args:
        model - Path to a .pt file of a pre-trained model
        path - Path to a single image to be evaluated
        output - Path to an output directory to save a result

    :return: Given args
    """
    example = r"""Example of usage: 
        py -m network.evaluate C:\models\detector.pt C:\data\test.jpg C:\output\ """

    parser = argparse.ArgumentParser(
        prog='CatsVsDogs Detector',
        description='Identifies cats or dogs in images and applies bounding boxes.',
        epilog=example,
        formatter_class=argparse.RawDescriptionHelpFormatter)

    parser.add_argument("model", type=Path, help="Path to pre-trained .pt model")
    parser.add_argument("path", type=Path, help="Path to the input image")
    parser.add_argument("output", type=Path, help="Directory to save the results")

    args = parser.parse_args()

    # Validate given paths
    if not args.model.is_file():
        parser.error(f"The model file was not found at: {args.model}")

    if not args.path.is_file():
        parser.error(f"The image file was not found at: {args.path}")

    if not args.output.exists():
        print(f"Note: Creating missing output directory at {args.output}")
        args.output.mkdir(parents=True, exist_ok=True)
    elif not args.output.is_dir():
        parser.error(f"The output path exists but is not a directory: {args.output}")

    return args


def evaluate(weights: Path, path_to_custom_image: Path, output_directory: Path):
    """
    Evaluates given single image on pre-trained CatVsDogDetector. Saves result to an output dir

    :param weights: Pre-train .pt model
    :param path_to_custom_image: Path to single image
    :param output_directory: Output directory to save result
    """
    model = CatVsDogDetector().to(device)

    params = torch.load(weights, map_location=device)
    model.load_state_dict(params)

    raw_image = read_image(path_to_custom_image.as_posix()).to(device)

    height, width = 448, 448
    mean = torch.tensor([0.479, 0.446, 0.395]).to(device)
    std = torch.tensor([0.262, 0.257, 0.265]).to(device)

    transform = v2.Compose([
        v2.ToDtype(torch.float32, scale=True),
        v2.Resize((height, width)),
        v2.Normalize(mean=mean, std=std)
    ])

    # Adding batch dim by .unsqueeze(0) so model can function properly
    input_image = transform(raw_image).unsqueeze(0)

    model.eval()
    with torch.no_grad():
        output = model(input_image)

        logits = output["logits"]
        bbox = output["bbox"]

        title = "Cat" if logits.argmax(dim=1).item() == 0 else "Dog"
        bbox_color = "red" if title == "Cat" else "blue"

        # Denormalize bounding box -> to get actual pixels coordinates
        bbox[:, 0] *= width
        bbox[:, 1] *= height
        bbox[:, 2] *= width
        bbox[:, 3] *= height

        # Changing format for draw_bounding_boxes() function
        pred_xyxy = box_convert(bbox, in_fmt="cxcywh", out_fmt="xyxy")

        visualize_image = v2.Resize((height, width))(raw_image)

        plot_image_bbox = draw_bounding_boxes(
            visualize_image.cpu(),
            pred_xyxy.cpu(),
            width=2,
            colors=bbox_color,
            labels=[title],
        )

        output_path = output_directory / f"{path_to_custom_image.stem}_output.png"
        write_png(plot_image_bbox, output_path.as_posix())
        print(f"Result saved to: {output_path.absolute()}")

if __name__ == "__main__":
    arguments = get_args()
    evaluate(arguments.model, arguments.path, arguments.output)
