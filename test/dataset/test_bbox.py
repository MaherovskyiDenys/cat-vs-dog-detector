from torchvision.utils import draw_bounding_boxes
import matplotlib.pyplot as plt

from data.loader import train_dataset, test_dataset

for i, t in train_dataset:
    label = "Cat" if t["label"].item() == 0 else "dog"
    print(f"Label: {label}")

    color =  "red" if t["label"].item() == 0 else "orange"

    img = draw_bounding_boxes(i, t["bbox"], width=2, colors=color)

    # Display
    plt.imshow(img.permute(1, 2, 0))
    plt.title(label.capitalize())
    plt.show()