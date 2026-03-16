# Run #1
## Hyper params

* lr = 1e-4
* epochs = 20
* optimizer = optim.Adam(model.parameters(), lr=lr, weight_decay=1e-3)
* loss = nn.CrossEntropyLoss(label_smoothing=0.1)

## Augmentation
```
v2.Resize((256, 256)),
v2.RandomCrop(size=(224, 224)),
v2.RandomHorizontalFlip(p=0.5),
v2.ColorJitter(brightness=0.125, contrast=0.125, saturation=0.1),
v2.RandomGrayscale(0.2),
v2.Normalize(
    mean=[0.479, 0.446, 0.395],
    std=[0.262, 0.257, 0.265]
)
```

## Output

* Epoch 1 | Time: 0:00:24.262214 | Train Loss: 0.6620 | Test Loss: 0.7253 | Train Acc: 65.68% | Test Acc: 67.84% | Gaps: 0.0633 / ~2.16% | LR: 0.0001
* Epoch 2 | Time: 0:00:47.873107 | Train Loss: 0.6229 | Test Loss: 0.6023 | Train Acc: 68.02% | Test Acc: 69.19% | Gaps: 0.0206 / ~1.16% | LR: 0.0001
* Epoch 3 | Time: 0:01:11.492482 | Train Loss: 0.5983 | Test Loss: 0.5825 | Train Acc: 70.67% | Test Acc: 72.03% | Gaps: 0.0157 / ~1.35% | LR: 0.0001
* Epoch 4 | Time: 0:01:35.084607 | Train Loss: 0.5691 | Test Loss: 0.6119 | Train Acc: 71.89% | Test Acc: 67.97% | Gaps: 0.0429 / ~3.92% | LR: 0.0001
* Epoch 5 | Time: 0:01:58.761803 | Train Loss: 0.5577 | Test Loss: 0.5761 | Train Acc: 73.76% | Test Acc: 73.51% | Gaps: 0.0184 / ~0.25% | LR: 0.0001
* Epoch 6 | Time: 0:02:22.423794 | Train Loss: 0.5216 | Test Loss: 0.6352 | Train Acc: 77.39% | Test Acc: 64.19% | Gaps: 0.1136 / ~13.20% | LR: 0.0001
* Epoch 7 | Time: 0:02:46.135729 | Train Loss: 0.5051 | Test Loss: 0.5167 | Train Acc: 79.26% | Test Acc: 78.11% | Gaps: 0.0116 / ~1.15% | LR: 0.0001
* Epoch 8 | Time: 0:03:10.265348 | Train Loss: 0.4765 | Test Loss: 0.5368 | Train Acc: 81.81% | Test Acc: 75.81% | Gaps: 0.0603 / ~6.00% | LR: 0.0001
* Epoch 9 | Time: 0:03:34.114816 | Train Loss: 0.4575 | Test Loss: 0.5040 | Train Acc: 83.10% | Test Acc: 78.92% | Gaps: 0.0465 / ~4.18% | LR: 0.0001
* Epoch 10 | Time: 0:03:57.713499 | Train Loss: 0.4431 | Test Loss: 0.4954 | Train Acc: 84.18% | Test Acc: 80.14% | Gaps: 0.0523 / ~4.05% | LR: 0.0001
* Epoch 11 | Time: 0:04:21.484160 | Train Loss: 0.4127 | Test Loss: 0.4938 | Train Acc: 86.15% | Test Acc: 80.14% | Gaps: 0.0811 / ~6.02% | LR: 0.0001
* Epoch 12 | Time: 0:04:45.132540 | Train Loss: 0.4054 | Test Loss: 0.4438 | Train Acc: 86.93% | Test Acc: 85.14% | Gaps: 0.0384 / ~1.80% | LR: 0.0001
* Epoch 13 | Time: 0:05:08.788274 | Train Loss: 0.3960 | Test Loss: 0.5191 | Train Acc: 87.78% | Test Acc: 75.95% | Gaps: 0.1231 / ~11.83% | LR: 0.0001
* Epoch 14 | Time: 0:05:32.502099 | Train Loss: 0.3868 | Test Loss: 0.4265 | Train Acc: 87.95% | Test Acc: 87.57% | Gaps: 0.0397 / ~0.38% | LR: 0.0001
* Epoch 15 | Time: 0:05:56.110780 | Train Loss: 0.3794 | Test Loss: 0.4282 | Train Acc: 88.56% | Test Acc: 85.54% | Gaps: 0.0488 / ~3.02% | LR: 0.0001
* Epoch 16 | Time: 0:06:19.803420 | Train Loss: 0.3734 | Test Loss: 0.5616 | Train Acc: 89.38% | Test Acc: 75.27% | Gaps: 0.1882 / ~14.11% | LR: 0.0001
* Epoch 17 | Time: 0:06:43.432630 | Train Loss: 0.3675 | Test Loss: 0.4154 | Train Acc: 89.61% | Test Acc: 87.43% | Gaps: 0.0479 / ~2.18% | LR: 0.0001
* Epoch 18 | Time: 0:07:07.087987 | Train Loss: 0.3613 | Test Loss: 0.4729 | Train Acc: 90.60% | Test Acc: 82.30% | Gaps: 0.1116 / ~8.30% | LR: 0.0001
* Epoch 19 | Time: 0:07:30.878228 | Train Loss: 0.3494 | Test Loss: 0.3857 | Train Acc: 91.21% | Test Acc: 88.92% | Gaps: 0.0363 / ~2.29% | LR: 0.0001
* Epoch 20 | Time: 0:07:55.166028 | Train Loss: 0.3427 | Test Loss: 0.4143 | Train Acc: 91.31% | Test Acc: 86.08% | Gaps: 0.0716 / ~5.23% | LR: 0.0001

# Run #2

## Hyper params

* lr = 1e-4
* epochs = 20
* optimizer = optim.Adam(model.parameters(), lr=lr, weight_decay=1e-4)
* loss = nn.CrossEntropyLoss(label_smoothing=0.1)

## Augmentation
```
v2.Resize((256, 256)),
v2.RandomCrop(size=(224, 224)),
v2.RandomHorizontalFlip(p=0.5),
v2.ColorJitter(brightness=0.125, contrast=0.125, saturation=0.1),
v2.RandomGrayscale(0.2),
v2.Normalize(
    mean=[0.479, 0.446, 0.395],
    std=[0.262, 0.257, 0.265]
)
```

## Output

* Epoch 1 | Time: 0:00:24.726210 | Train Loss: 0.6506 | Test Loss: 0.6113 | Train Acc: 66.73% | Test Acc: 70.27% | Gaps: 0.0393 / ~3.54% | LR: 0.0001
* Epoch 2 | Time: 0:00:48.731448 | Train Loss: 0.6161 | Test Loss: 0.6024 | Train Acc: 68.47% | Test Acc: 69.32% | Gaps: 0.0137 / ~0.86% | LR: 0.0001
* Epoch 3 | Time: 0:01:13.035405 | Train Loss: 0.5925 | Test Loss: 0.5938 | Train Acc: 70.94% | Test Acc: 72.43% | Gaps: 0.0014 / ~1.49% | LR: 0.0001
* Epoch 4 | Time: 0:01:36.574918 | Train Loss: 0.5852 | Test Loss: 0.5789 | Train Acc: 71.59% | Test Acc: 72.43% | Gaps: 0.0063 / ~0.84% | LR: 0.0001
* Epoch 5 | Time: 0:02:00.069579 | Train Loss: 0.5573 | Test Loss: 0.6788 | Train Acc: 73.96% | Test Acc: 69.86% | Gaps: 0.1215 / ~4.10% | LR: 0.0001
* Epoch 6 | Time: 0:02:23.585738 | Train Loss: 0.5476 | Test Loss: 0.5616 | Train Acc: 75.32% | Test Acc: 75.14% | Gaps: 0.0140 / ~0.19% | LR: 0.0001
* Epoch 7 | Time: 0:02:47.133269 | Train Loss: 0.5252 | Test Loss: 0.6109 | Train Acc: 76.68% | Test Acc: 71.08% | Gaps: 0.0857 / ~5.60% | LR: 0.0001
* Epoch 8 | Time: 0:03:10.620146 | Train Loss: 0.5012 | Test Loss: 0.5500 | Train Acc: 79.74% | Test Acc: 74.32% | Gaps: 0.0489 / ~5.41% | LR: 0.0001
* Epoch 9 | Time: 0:03:34.105678 | Train Loss: 0.4684 | Test Loss: 0.5135 | Train Acc: 82.42% | Test Acc: 78.78% | Gaps: 0.0452 / ~3.63% | LR: 0.0001
* Epoch 10 | Time: 0:03:57.563240 | Train Loss: 0.4459 | Test Loss: 0.4740 | Train Acc: 83.44% | Test Acc: 82.16% | Gaps: 0.0281 / ~1.27% | LR: 0.0001
* Epoch 11 | Time: 0:04:21.134207 | Train Loss: 0.4110 | Test Loss: 0.4437 | Train Acc: 86.25% | Test Acc: 82.97% | Gaps: 0.0327 / ~3.28% | LR: 0.0001
* Epoch 12 | Time: 0:04:44.559109 | Train Loss: 0.4101 | Test Loss: 0.4284 | Train Acc: 87.03% | Test Acc: 84.86% | Gaps: 0.0183 / ~2.17% | LR: 0.0001
* Epoch 13 | Time: 0:05:08.015459 | Train Loss: 0.4016 | Test Loss: 0.5484 | Train Acc: 87.64% | Test Acc: 77.97% | Gaps: 0.1469 / ~9.67% | LR: 0.0001
* Epoch 14 | Time: 0:05:31.542266 | Train Loss: 0.3918 | Test Loss: 0.5341 | Train Acc: 88.39% | Test Acc: 79.19% | Gaps: 0.1423 / ~9.20% | LR: 0.0001
* Epoch 15 | Time: 0:05:54.990053 | Train Loss: 0.3756 | Test Loss: 0.4079 | Train Acc: 89.41% | Test Acc: 87.16% | Gaps: 0.0323 / ~2.25% | LR: 0.0001
* Epoch 16 | Time: 0:06:18.639666 | Train Loss: 0.3609 | Test Loss: 0.3960 | Train Acc: 90.19% | Test Acc: 88.78% | Gaps: 0.0351 / ~1.41% | LR: 0.0001
* Epoch 17 | Time: 0:06:42.126945 | Train Loss: 0.3584 | Test Loss: 0.4064 | Train Acc: 91.04% | Test Acc: 87.43% | Gaps: 0.0481 / ~3.61% | LR: 0.0001
* Epoch 18 | Time: 0:07:05.586948 | Train Loss: 0.3487 | Test Loss: 0.3788 | Train Acc: 90.80% | Test Acc: 90.68% | Gaps: 0.0301 / ~0.13% | LR: 0.0001
* Epoch 19 | Time: 0:07:29.075694 | Train Loss: 0.3354 | Test Loss: 0.3630 | Train Acc: 91.99% | Test Acc: 90.81% | Gaps: 0.0276 / ~1.18% | LR: 0.0001
* Epoch 20 | Time: 0:07:52.521718 | Train Loss: 0.3410 | Test Loss: 0.3650 | Train Acc: 91.41% | Test Acc: 90.27% | Gaps: 0.0240 / ~1.14% | LR: 0.0001

### Notes:
  * noticed weight decay increased acc on test dataset, maybe a pure luck but will experiment

# Run #3
## Hyper params

* lr = 1e-4
* epochs = 30
* optimizer = optim.Adam(model.parameters(), lr=lr, weight_decay=1e-4)
* loss = nn.CrossEntropyLoss(label_smoothing=0.1)

## Augmentation
```
v2.Resize((256, 256)),
v2.RandomCrop(size=(224, 224)),
v2.RandomHorizontalFlip(p=0.5),
v2.ColorJitter(brightness=0.125, contrast=0.125, saturation=0.1),
v2.RandomGrayscale(0.2),
v2.Normalize(
    mean=[0.479, 0.446, 0.395],
    std=[0.262, 0.257, 0.265]
)
```

## Output

* Epoch 1 | Time: 0:00:23.951315 | Train Loss: 0.6492 | Test Loss: 0.6630 | Train Acc: 66.26% | Test Acc: 62.16% | Gaps: 0.0137 / ~4.10% | LR: 0.0001
* Epoch 2 | Time: 0:00:48.173666 | Train Loss: 0.6167 | Test Loss: 0.6126 | Train Acc: 68.74% | Test Acc: 69.86% | Gaps: 0.0041 / ~1.13% | LR: 0.0001
* Epoch 3 | Time: 0:01:12.230081 | Train Loss: 0.5911 | Test Loss: 0.5870 | Train Acc: 71.93% | Test Acc: 71.62% | Gaps: 0.0041 / ~0.31% | LR: 0.0001
* Epoch 4 | Time: 0:01:35.852122 | Train Loss: 0.5649 | Test Loss: 0.6814 | Train Acc: 73.69% | Test Acc: 64.59% | Gaps: 0.1165 / ~9.10% | LR: 0.0001
* Epoch 5 | Time: 0:01:59.425036 | Train Loss: 0.5630 | Test Loss: 0.5465 | Train Acc: 74.20% | Test Acc: 76.22% | Gaps: 0.0165 / ~2.01% | LR: 0.0001
* Epoch 6 | Time: 0:02:23.372400 | Train Loss: 0.5404 | Test Loss: 0.6060 | Train Acc: 75.19% | Test Acc: 68.11% | Gaps: 0.0656 / ~7.08% | LR: 0.0001
* Epoch 7 | Time: 0:02:47.891258 | Train Loss: 0.5234 | Test Loss: 0.5401 | Train Acc: 76.85% | Test Acc: 76.62% | Gaps: 0.0167 / ~0.23% | LR: 0.0001
* Epoch 8 | Time: 0:03:12.075761 | Train Loss: 0.4930 | Test Loss: 0.5267 | Train Acc: 80.99% | Test Acc: 79.59% | Gaps: 0.0337 / ~1.40% | LR: 0.0001
* Epoch 9 | Time: 0:03:36.290410 | Train Loss: 0.4675 | Test Loss: 0.4673 | Train Acc: 82.42% | Test Acc: 83.51% | Gaps: 0.0002 / ~1.10% | LR: 0.0001
* Epoch 10 | Time: 0:04:00.564913 | Train Loss: 0.4529 | Test Loss: 0.4770 | Train Acc: 83.84% | Test Acc: 80.81% | Gaps: 0.0242 / ~3.03% | LR: 0.0001
* Epoch 11 | Time: 0:04:25.099003 | Train Loss: 0.4255 | Test Loss: 0.5310 | Train Acc: 85.88% | Test Acc: 74.59% | Gaps: 0.1055 / ~11.28% | LR: 0.0001
* Epoch 12 | Time: 0:04:50.211903 | Train Loss: 0.4109 | Test Loss: 0.4276 | Train Acc: 86.01% | Test Acc: 85.41% | Gaps: 0.0168 / ~0.61% | LR: 0.0001
* Epoch 13 | Time: 0:05:14.407614 | Train Loss: 0.3943 | Test Loss: 0.4145 | Train Acc: 88.05% | Test Acc: 86.35% | Gaps: 0.0202 / ~1.70% | LR: 0.0001
* Epoch 14 | Time: 0:05:38.360622 | Train Loss: 0.3858 | Test Loss: 0.4205 | Train Acc: 88.22% | Test Acc: 86.49% | Gaps: 0.0347 / ~1.73% | LR: 0.0001
* Epoch 15 | Time: 0:06:02.509232 | Train Loss: 0.3635 | Test Loss: 0.4185 | Train Acc: 89.78% | Test Acc: 87.57% | Gaps: 0.0550 / ~2.22% | LR: 0.0001
* Epoch 16 | Time: 0:06:26.334214 | Train Loss: 0.3669 | Test Loss: 0.4216 | Train Acc: 89.41% | Test Acc: 87.16% | Gaps: 0.0547 / ~2.25% | LR: 0.0001
* Epoch 17 | Time: 0:06:50.322201 | Train Loss: 0.3598 | Test Loss: 0.3767 | Train Acc: 90.29% | Test Acc: 90.00% | Gaps: 0.0169 / ~0.29% | LR: 0.0001
* Epoch 18 | Time: 0:07:14.307752 | Train Loss: 0.3387 | Test Loss: 0.4001 | Train Acc: 92.16% | Test Acc: 87.84% | Gaps: 0.0614 / ~4.32% | LR: 0.0001
* Epoch 19 | Time: 0:07:38.248392 | Train Loss: 0.3366 | Test Loss: 0.4496 | Train Acc: 91.68% | Test Acc: 84.86% | Gaps: 0.1130 / ~6.82% | LR: 0.0001
* Epoch 20 | Time: 0:08:01.997967 | Train Loss: 0.3383 | Test Loss: 0.4217 | Train Acc: 91.48% | Test Acc: 89.05% | Gaps: 0.0833 / ~2.43% | LR: 0.0001
* Epoch 21 | Time: 0:08:26.539898 | Train Loss: 0.3204 | Test Loss: 0.3725 | Train Acc: 93.38% | Test Acc: 90.54% | Gaps: 0.0522 / ~2.84% | LR: 0.0001
* Epoch 22 | Time: 0:08:50.537259 | Train Loss: 0.3204 | Test Loss: 0.4141 | Train Acc: 93.04% | Test Acc: 87.70% | Gaps: 0.0938 / ~5.34% | LR: 0.0001
* Epoch 23 | Time: 0:09:14.329831 | Train Loss: 0.3119 | Test Loss: 0.3507 | Train Acc: 93.38% | Test Acc: 91.62% | Gaps: 0.0388 / ~1.76% | LR: 0.0001
* Epoch 24 | Time: 0:09:38.001356 | Train Loss: 0.3120 | Test Loss: 0.3926 | Train Acc: 93.25% | Test Acc: 90.14% | Gaps: 0.0806 / ~3.11% | LR: 0.0001
* Epoch 25 | Time: 0:10:02.006571 | Train Loss: 0.3035 | Test Loss: 0.4223 | Train Acc: 94.43% | Test Acc: 86.22% | Gaps: 0.1187 / ~8.22% | LR: 0.0001
* Epoch 26 | Time: 0:10:25.774614 | Train Loss: 0.3102 | Test Loss: 0.4513 | Train Acc: 93.55% | Test Acc: 85.27% | Gaps: 0.1411 / ~8.28% | LR: 0.0001
* Epoch 27 | Time: 0:10:49.298713 | Train Loss: 0.2986 | Test Loss: 0.4077 | Train Acc: 94.57% | Test Acc: 87.16% | Gaps: 0.1092 / ~7.41% | LR: 0.0001
* Epoch 28 | Time: 0:11:13.017271 | Train Loss: 0.2856 | Test Loss: 0.3936 | Train Acc: 95.15% | Test Acc: 88.24% | Gaps: 0.1079 / ~6.90% | LR: 0.0001
* Epoch 29 | Time: 0:11:36.749682 | Train Loss: 0.2806 | Test Loss: 0.3934 | Train Acc: 95.52% | Test Acc: 88.24% | Gaps: 0.1128 / ~7.28% | LR: 0.0001
* Epoch 30 | Time: 0:12:00.289223 | Train Loss: 0.2907 | Test Loss: 0.3563 | Train Acc: 94.53% | Test Acc: 92.03% | Gaps: 0.0656 / ~2.51% | LR: 0.0001

### Notes:
* epoches increased just wanted to see if model will still memorize train dataset
* as expected not model still was learning loss was stable at the same spot and acc increasing

# Run #4
## Hyper params

* lr = 1e-4
* epochs = 30
* optimizer = optim.Adam(model.parameters(), lr=lr, weight_decay=1e-4)
* weight = torch.tensor([2.1, 1.0]).to(device)
* loss = nn.CrossEntropyLoss(weight=weight, label_smoothing=0.1)


## Augmentation
```
v2.Resize((256, 256)),
v2.RandomCrop(size=(224, 224)),
v2.RandomHorizontalFlip(p=0.5),
v2.ColorJitter(brightness=0.125, contrast=0.125, saturation=0.1),
v2.RandomGrayscale(0.2),
v2.Normalize(
    mean=[0.479, 0.446, 0.395],
    std=[0.262, 0.257, 0.265]
)
```

## Output

* Epoch 1 | Time: 0:00:25.161008 | Train Loss: 0.7263 | Test Loss: 0.6829 | Train Acc: 54.48% | Test Acc: 65.00% | Gaps: 0.0434 / ~10.52% | LR: 0.0001
* Epoch 2 | Time: 0:00:49.655509 | Train Loss: 0.6772 | Test Loss: 0.6706 | Train Acc: 60.42% | Test Acc: 55.68% | Gaps: 0.0067 / ~4.75% | LR: 0.0001
* Epoch 3 | Time: 0:01:13.842071 | Train Loss: 0.6565 | Test Loss: 0.7348 | Train Acc: 62.63% | Test Acc: 46.49% | Gaps: 0.0783 / ~16.14% | LR: 0.0001
* Epoch 4 | Time: 0:01:38.206740 | Train Loss: 0.6340 | Test Loss: 0.6626 | Train Acc: 67.48% | Test Acc: 68.11% | Gaps: 0.0286 / ~0.63% | LR: 0.0001
* Epoch 5 | Time: 0:02:03.495195 | Train Loss: 0.6206 | Test Loss: 0.6042 | Train Acc: 67.01% | Test Acc: 66.08% | Gaps: 0.0164 / ~0.93% | LR: 0.0001
* Epoch 6 | Time: 0:02:28.024334 | Train Loss: 0.6150 | Test Loss: 0.6576 | Train Acc: 68.30% | Test Acc: 67.84% | Gaps: 0.0427 / ~0.46% | LR: 0.0001
* Epoch 7 | Time: 0:02:52.494657 | Train Loss: 0.5937 | Test Loss: 0.5946 | Train Acc: 71.18% | Test Acc: 64.86% | Gaps: 0.0008 / ~6.32% | LR: 0.0001
* Epoch 8 | Time: 0:03:17.751582 | Train Loss: 0.5599 | Test Loss: 0.5943 | Train Acc: 73.15% | Test Acc: 77.43% | Gaps: 0.0344 / ~4.28% | LR: 0.0001
* Epoch 9 | Time: 0:03:43.589609 | Train Loss: 0.5405 | Test Loss: 0.5627 | Train Acc: 76.85% | Test Acc: 70.81% | Gaps: 0.0222 / ~6.04% | LR: 0.0001
* Epoch 10 | Time: 0:04:09.605999 | Train Loss: 0.5165 | Test Loss: 0.5580 | Train Acc: 78.51% | Test Acc: 81.76% | Gaps: 0.0415 / ~3.24% | LR: 0.0001
* Epoch 11 | Time: 0:04:35.161018 | Train Loss: 0.4889 | Test Loss: 0.8492 | Train Acc: 81.64% | Test Acc: 38.78% | Gaps: 0.3603 / ~42.85% | LR: 0.0001
* Epoch 12 | Time: 0:05:00.658505 | Train Loss: 0.4683 | Test Loss: 0.5286 | Train Acc: 83.67% | Test Acc: 72.16% | Gaps: 0.0603 / ~11.51% | LR: 0.0001
* Epoch 13 | Time: 0:05:26.193679 | Train Loss: 0.4702 | Test Loss: 0.5848 | Train Acc: 83.06% | Test Acc: 63.51% | Gaps: 0.1146 / ~19.55% | LR: 0.0001
* Epoch 14 | Time: 0:05:52.861195 | Train Loss: 0.4572 | Test Loss: 0.4890 | Train Acc: 84.01% | Test Acc: 79.86% | Gaps: 0.0318 / ~4.15% | LR: 0.0001
* Epoch 15 | Time: 0:06:18.865657 | Train Loss: 0.4376 | Test Loss: 0.4998 | Train Acc: 85.51% | Test Acc: 87.30% | Gaps: 0.0622 / ~1.79% | LR: 0.0001
* Epoch 16 | Time: 0:06:44.192909 | Train Loss: 0.4358 | Test Loss: 0.4413 | Train Acc: 86.32% | Test Acc: 84.05% | Gaps: 0.0055 / ~2.27% | LR: 0.0001
* Epoch 17 | Time: 0:07:10.157788 | Train Loss: 0.4143 | Test Loss: 0.4562 | Train Acc: 87.71% | Test Acc: 82.30% | Gaps: 0.0419 / ~5.41% | LR: 0.0001
* Epoch 18 | Time: 0:07:36.266546 | Train Loss: 0.4154 | Test Loss: 0.4429 | Train Acc: 88.05% | Test Acc: 84.05% | Gaps: 0.0275 / ~4.00% | LR: 0.0001
* Epoch 19 | Time: 0:08:02.266327 | Train Loss: 0.3968 | Test Loss: 0.4385 | Train Acc: 88.90% | Test Acc: 84.46% | Gaps: 0.0417 / ~4.44% | LR: 0.0001
* Epoch 20 | Time: 0:08:28.435736 | Train Loss: 0.3902 | Test Loss: 0.5337 | Train Acc: 89.31% | Test Acc: 71.62% | Gaps: 0.1435 / ~17.69% | LR: 0.0001
* Epoch 21 | Time: 0:08:53.747934 | Train Loss: 0.3874 | Test Loss: 0.4488 | Train Acc: 89.78% | Test Acc: 81.08% | Gaps: 0.0614 / ~8.70% | LR: 0.0001
* Epoch 22 | Time: 0:09:18.438160 | Train Loss: 0.3796 | Test Loss: 0.5361 | Train Acc: 89.85% | Test Acc: 71.08% | Gaps: 0.1564 / ~18.77% | LR: 0.0001
* Epoch 23 | Time: 0:09:43.375242 | Train Loss: 0.3597 | Test Loss: 0.4378 | Train Acc: 91.48% | Test Acc: 82.70% | Gaps: 0.0781 / ~8.78% | LR: 0.0001
* Epoch 24 | Time: 0:10:08.157634 | Train Loss: 0.3645 | Test Loss: 0.4218 | Train Acc: 91.00% | Test Acc: 87.84% | Gaps: 0.0573 / ~3.17% | LR: 0.0001
* Epoch 25 | Time: 0:10:32.782045 | Train Loss: 0.3518 | Test Loss: 0.4564 | Train Acc: 92.23% | Test Acc: 80.41% | Gaps: 0.1046 / ~11.82% | LR: 0.0001
* Epoch 26 | Time: 0:10:57.203777 | Train Loss: 0.3439 | Test Loss: 0.4085 | Train Acc: 92.94% | Test Acc: 90.54% | Gaps: 0.0645 / ~2.40% | LR: 0.0001
* Epoch 27 | Time: 0:11:21.494280 | Train Loss: 0.3256 | Test Loss: 0.4583 | Train Acc: 94.33% | Test Acc: 80.68% | Gaps: 0.1328 / ~13.66% | LR: 0.0001
* Epoch 28 | Time: 0:11:45.817613 | Train Loss: 0.3321 | Test Loss: 0.4359 | Train Acc: 93.72% | Test Acc: 82.70% | Gaps: 0.1037 / ~11.02% | LR: 0.0001
* Epoch 29 | Time: 0:12:10.145883 | Train Loss: 0.3310 | Test Loss: 0.4046 | Train Acc: 93.48% | Test Acc: 91.89% | Gaps: 0.0736 / ~1.59% | LR: 0.0001
* Epoch 30 | Time: 0:12:34.640968 | Train Loss: 0.3279 | Test Loss: 0.3841 | Train Acc: 94.23% | Test Acc: 88.78% | Gaps: 0.0562 / ~5.45% | LR: 0.0001
* 

### Notes:
* added weight to loss functon to handle imbalance in dataset with ration ~ 1:2.1 so cats gets more priority
* verdict: test acc started behave jumpy however we def could reach higher acc

# Run #5
## Hyper params

* lr = 1e-4
* epochs = 30
* optimizer = optim.Adam(model.parameters(), lr=lr, weight_decay=1e-4)
* weight = torch.tensor([2.1, 1.0]).to(device)
* loss = nn.CrossEntropyLoss(weight=weight, label_smoothing=0.1)
* scheduler = optim.lr_scheduler.MultiStepLR(optimizer, milestones=[10, 20, 25], gamma=0.5)


## Augmentation
```
v2.Resize((256, 256)),
v2.RandomCrop(size=(224, 224)),
v2.RandomHorizontalFlip(p=0.5),
v2.ColorJitter(brightness=0.125, contrast=0.125, saturation=0.1),
v2.RandomGrayscale(0.2),
v2.Normalize(
    mean=[0.479, 0.446, 0.395],
    std=[0.262, 0.257, 0.265]
)
```

## Output

* Epoch 1 | Time: 0:00:24.239773 | Train Loss: 0.7330 | Test Loss: 0.7126 | Train Acc: 53.87% | Test Acc: 66.62% | Gaps: 0.0203 / ~12.75% | LR: 0.0001
* Epoch 2 | Time: 0:00:47.840032 | Train Loss: 0.6780 | Test Loss: 0.7132 | Train Acc: 60.39% | Test Acc: 70.54% | Gaps: 0.0352 / ~10.15% | LR: 0.0001
* Epoch 3 | Time: 0:01:11.575485 | Train Loss: 0.6571 | Test Loss: 0.6657 | Train Acc: 64.36% | Test Acc: 65.27% | Gaps: 0.0086 / ~0.91% | LR: 0.0001
* Epoch 4 | Time: 0:01:35.339955 | Train Loss: 0.6371 | Test Loss: 0.6920 | Train Acc: 65.89% | Test Acc: 53.38% | Gaps: 0.0549 / ~12.51% | LR: 0.0001
* Epoch 5 | Time: 0:01:59.152656 | Train Loss: 0.6209 | Test Loss: 0.6177 | Train Acc: 68.60% | Test Acc: 68.92% | Gaps: 0.0033 / ~0.32% | LR: 0.0001
* Epoch 6 | Time: 0:02:23.013396 | Train Loss: 0.5985 | Test Loss: 0.6210 | Train Acc: 70.20% | Test Acc: 75.41% | Gaps: 0.0224 / ~5.21% | LR: 0.0001
* Epoch 7 | Time: 0:02:46.771057 | Train Loss: 0.5784 | Test Loss: 0.6792 | Train Acc: 72.51% | Test Acc: 73.92% | Gaps: 0.1008 / ~1.41% | LR: 0.0001
* Epoch 8 | Time: 0:03:10.542493 | Train Loss: 0.5779 | Test Loss: 0.5844 | Train Acc: 73.29% | Test Acc: 73.92% | Gaps: 0.0065 / ~0.63% | LR: 0.0001
* Epoch 9 | Time: 0:03:34.312356 | Train Loss: 0.5416 | Test Loss: 0.6890 | Train Acc: 76.51% | Test Acc: 76.35% | Gaps: 0.1474 / ~0.16% | LR: 0.0001
* Epoch 10 | Time: 0:03:58.034263 | Train Loss: 0.5176 | Test Loss: 0.5341 | Train Acc: 78.58% | Test Acc: 78.38% | Gaps: 0.0164 / ~0.20% | LR: 0.0001
* Epoch 11 | Time: 0:04:21.850396 | Train Loss: 0.4719 | Test Loss: 0.4825 | Train Acc: 81.87% | Test Acc: 80.81% | Gaps: 0.0105 / ~1.06% | LR: 5e-05
* Epoch 12 | Time: 0:04:45.628358 | Train Loss: 0.4483 | Test Loss: 0.5234 | Train Acc: 84.35% | Test Acc: 82.03% | Gaps: 0.0752 / ~2.32% | LR: 5e-05
* Epoch 13 | Time: 0:05:09.614654 | Train Loss: 0.4386 | Test Loss: 0.4595 | Train Acc: 85.74% | Test Acc: 84.19% | Gaps: 0.0209 / ~1.55% | LR: 5e-05
* Epoch 14 | Time: 0:05:33.485205 | Train Loss: 0.4225 | Test Loss: 0.4836 | Train Acc: 87.51% | Test Acc: 86.62% | Gaps: 0.0611 / ~0.89% | LR: 5e-05
* Epoch 15 | Time: 0:05:57.242476 | Train Loss: 0.4100 | Test Loss: 0.4445 | Train Acc: 87.85% | Test Acc: 86.35% | Gaps: 0.0344 / ~1.50% | LR: 5e-05
* Epoch 16 | Time: 0:06:20.995858 | Train Loss: 0.4086 | Test Loss: 0.4554 | Train Acc: 87.95% | Test Acc: 84.86% | Gaps: 0.0468 / ~3.08% | LR: 5e-05
* Epoch 17 | Time: 0:06:44.760471 | Train Loss: 0.3910 | Test Loss: 0.5615 | Train Acc: 89.71% | Test Acc: 71.49% | Gaps: 0.1705 / ~18.23% | LR: 5e-05
* Epoch 18 | Time: 0:07:08.553939 | Train Loss: 0.3903 | Test Loss: 0.5146 | Train Acc: 89.38% | Test Acc: 74.19% | Gaps: 0.1244 / ~15.19% | LR: 5e-05
* Epoch 19 | Time: 0:07:32.372311 | Train Loss: 0.3826 | Test Loss: 0.4508 | Train Acc: 90.05% | Test Acc: 86.89% | Gaps: 0.0682 / ~3.16% | LR: 5e-05
* Epoch 20 | Time: 0:07:56.134826 | Train Loss: 0.3811 | Test Loss: 0.4158 | Train Acc: 90.56% | Test Acc: 87.30% | Gaps: 0.0347 / ~3.27% | LR: 5e-05
* Epoch 21 | Time: 0:08:19.909703 | Train Loss: 0.3471 | Test Loss: 0.4192 | Train Acc: 93.04% | Test Acc: 86.35% | Gaps: 0.0721 / ~6.69% | LR: 2.5e-05
* Epoch 22 | Time: 0:08:43.687110 | Train Loss: 0.3327 | Test Loss: 0.4072 | Train Acc: 94.16% | Test Acc: 85.81% | Gaps: 0.0745 / ~8.35% | LR: 2.5e-05
* Epoch 23 | Time: 0:09:07.476731 | Train Loss: 0.3308 | Test Loss: 0.4581 | Train Acc: 93.75% | Test Acc: 89.46% | Gaps: 0.1273 / ~4.29% | LR: 2.5e-05
* Epoch 24 | Time: 0:09:31.285889 | Train Loss: 0.3241 | Test Loss: 0.4358 | Train Acc: 94.13% | Test Acc: 83.78% | Gaps: 0.1117 / ~10.34% | LR: 2.5e-05
* Epoch 25 | Time: 0:09:55.120714 | Train Loss: 0.3230 | Test Loss: 0.4039 | Train Acc: 94.50% | Test Acc: 86.76% | Gaps: 0.0809 / ~7.74% | LR: 2.5e-05
* Epoch 26 | Time: 0:10:18.956001 | Train Loss: 0.3035 | Test Loss: 0.3845 | Train Acc: 96.06% | Test Acc: 90.00% | Gaps: 0.0811 / ~6.06% | LR: 1.25e-05
* Epoch 27 | Time: 0:10:42.750425 | Train Loss: 0.3040 | Test Loss: 0.3927 | Train Acc: 95.89% | Test Acc: 88.65% | Gaps: 0.0886 / ~7.24% | LR: 1.25e-05
* Epoch 28 | Time: 0:11:06.476310 | Train Loss: 0.2985 | Test Loss: 0.3762 | Train Acc: 96.03% | Test Acc: 92.43% | Gaps: 0.0777 / ~3.60% | LR: 1.25e-05
* Epoch 29 | Time: 0:11:30.289961 | Train Loss: 0.2998 | Test Loss: 0.3872 | Train Acc: 96.27% | Test Acc: 90.95% | Gaps: 0.0873 / ~5.32% | LR: 1.25e-05
* Epoch 30 | Time: 0:11:54.019662 | Train Loss: 0.3004 | Test Loss: 0.3853 | Train Acc: 96.30% | Test Acc: 90.14% | Gaps: 0.0849 / ~6.16% | LR: 1.25e-05

### Notes:
* weight clases did work but lr became too aggressive, let's add scheduler
* verdict: we definitely moving in the right direction but need to play with scheduler around, have reached best acc ever


# Run #6
## Hyper params

* lr = 1e-4
* epochs = 30
* optimizer = optim.Adam(model.parameters(), lr=lr, weight_decay=1e-4)
* weight = torch.tensor([2.1, 1.0]).to(device)
* loss = nn.CrossEntropyLoss(weight=weight, label_smoothing=0.1)
* scheduler = optim.lr_scheduler.MultiStepLR(optimizer, milestones=[10, 20, 25], gamma=0.5)

added dropout to fc        
self.fc = nn.Sequential(
    nn.Dropout(0.2),
    nn.Linear(512, 2)
)


## Augmentation
```
v2.Resize((256, 256)),
v2.RandomCrop(size=(224, 224)),
v2.RandomHorizontalFlip(p=0.5),
v2.ColorJitter(brightness=0.125, contrast=0.125, saturation=0.1),
v2.RandomGrayscale(0.2),
v2.Normalize(
    mean=[0.479, 0.446, 0.395],
    std=[0.262, 0.257, 0.265]
)
```

## Output

* Epoch 1 | Time: 0:00:28.427528 | Train Loss: 0.7302 | Test Loss: 0.6700 | Train Acc: 55.74% | Test Acc: 51.89% | Gaps: 0.0602 / ~3.84% | LR: 0.0001
* Epoch 2 | Time: 0:00:55.299259 | Train Loss: 0.6782 | Test Loss: 0.6586 | Train Acc: 60.66% | Test Acc: 57.43% | Gaps: 0.0196 / ~3.23% | LR: 0.0001
* Epoch 3 | Time: 0:01:19.256088 | Train Loss: 0.6626 | Test Loss: 0.6791 | Train Acc: 63.24% | Test Acc: 45.27% | Gaps: 0.0164 / ~17.97% | LR: 0.0001
* Epoch 4 | Time: 0:01:43.254505 | Train Loss: 0.6463 | Test Loss: 0.6567 | Train Acc: 66.12% | Test Acc: 53.38% | Gaps: 0.0104 / ~12.75% | LR: 0.0001
* Epoch 5 | Time: 0:02:06.876668 | Train Loss: 0.6296 | Test Loss: 0.7614 | Train Acc: 67.52% | Test Acc: 41.89% | Gaps: 0.1317 / ~25.62% | LR: 0.0001
* Epoch 6 | Time: 0:02:30.472416 | Train Loss: 0.6136 | Test Loss: 0.6048 | Train Acc: 69.55% | Test Acc: 70.27% | Gaps: 0.0088 / ~0.72% | LR: 0.0001
* Epoch 7 | Time: 0:02:54.119490 | Train Loss: 0.5843 | Test Loss: 0.6697 | Train Acc: 72.51% | Test Acc: 74.86% | Gaps: 0.0855 / ~2.36% | LR: 0.0001
* Epoch 8 | Time: 0:03:17.755566 | Train Loss: 0.5526 | Test Loss: 0.5635 | Train Acc: 74.75% | Test Acc: 75.00% | Gaps: 0.0109 / ~0.25% | LR: 0.0001
* Epoch 9 | Time: 0:03:41.469293 | Train Loss: 0.5321 | Test Loss: 0.5522 | Train Acc: 77.36% | Test Acc: 79.73% | Gaps: 0.0201 / ~2.37% | LR: 0.0001
* Epoch 10 | Time: 0:04:05.614797 | Train Loss: 0.5074 | Test Loss: 0.5483 | Train Acc: 79.40% | Test Acc: 76.76% | Gaps: 0.0410 / ~2.64% | LR: 0.0001
* Epoch 11 | Time: 0:04:30.358450 | Train Loss: 0.4666 | Test Loss: 0.4550 | Train Acc: 83.03% | Test Acc: 84.86% | Gaps: 0.0117 / ~1.84% | LR: 5e-05
* Epoch 12 | Time: 0:04:54.813449 | Train Loss: 0.4449 | Test Loss: 0.5144 | Train Acc: 85.57% | Test Acc: 86.62% | Gaps: 0.0695 / ~1.05% | LR: 5e-05
* Epoch 13 | Time: 0:05:18.504940 | Train Loss: 0.4325 | Test Loss: 0.4990 | Train Acc: 87.10% | Test Acc: 86.89% | Gaps: 0.0665 / ~0.21% | LR: 5e-05
* Epoch 14 | Time: 0:05:42.204055 | Train Loss: 0.4179 | Test Loss: 0.4798 | Train Acc: 87.85% | Test Acc: 77.97% | Gaps: 0.0619 / ~9.87% | LR: 5e-05
* Epoch 15 | Time: 0:06:05.853990 | Train Loss: 0.4083 | Test Loss: 0.4337 | Train Acc: 88.32% | Test Acc: 85.95% | Gaps: 0.0254 / ~2.38% | LR: 5e-05
* Epoch 16 | Time: 0:06:29.534319 | Train Loss: 0.4201 | Test Loss: 0.4457 | Train Acc: 86.63% | Test Acc: 87.30% | Gaps: 0.0256 / ~0.67% | LR: 5e-05
* Epoch 17 | Time: 0:06:53.202981 | Train Loss: 0.4104 | Test Loss: 0.4675 | Train Acc: 88.32% | Test Acc: 79.59% | Gaps: 0.0571 / ~8.73% | LR: 5e-05
* Epoch 18 | Time: 0:07:16.846112 | Train Loss: 0.3925 | Test Loss: 0.4088 | Train Acc: 89.34% | Test Acc: 90.14% | Gaps: 0.0162 / ~0.79% | LR: 5e-05
* Epoch 19 | Time: 0:07:40.460468 | Train Loss: 0.3818 | Test Loss: 0.4308 | Train Acc: 90.56% | Test Acc: 91.08% | Gaps: 0.0490 / ~0.52% | LR: 5e-05
* Epoch 20 | Time: 0:08:04.121069 | Train Loss: 0.3766 | Test Loss: 0.4460 | Train Acc: 90.63% | Test Acc: 82.43% | Gaps: 0.0694 / ~8.20% | LR: 5e-05
* Epoch 21 | Time: 0:08:27.788240 | Train Loss: 0.3583 | Test Loss: 0.3813 | Train Acc: 92.19% | Test Acc: 89.73% | Gaps: 0.0230 / ~2.46% | LR: 2.5e-05
* Epoch 22 | Time: 0:08:51.624821 | Train Loss: 0.3379 | Test Loss: 0.3804 | Train Acc: 93.69% | Test Acc: 92.57% | Gaps: 0.0425 / ~1.12% | LR: 2.5e-05
* Epoch 23 | Time: 0:09:15.297853 | Train Loss: 0.3322 | Test Loss: 0.3849 | Train Acc: 94.23% | Test Acc: 91.62% | Gaps: 0.0527 / ~2.61% | LR: 2.5e-05
* Epoch 24 | Time: 0:09:39.053759 | Train Loss: 0.3367 | Test Loss: 0.3804 | Train Acc: 93.65% | Test Acc: 92.03% | Gaps: 0.0437 / ~1.63% | LR: 2.5e-05
* Epoch 25 | Time: 0:10:02.716212 | Train Loss: 0.3270 | Test Loss: 0.3775 | Train Acc: 94.16% | Test Acc: 91.08% | Gaps: 0.0505 / ~3.08% | LR: 2.5e-05
* Epoch 26 | Time: 0:10:26.998565 | Train Loss: 0.3139 | Test Loss: 0.3754 | Train Acc: 94.84% | Test Acc: 92.57% | Gaps: 0.0615 / ~2.27% | LR: 1.25e-05
* Epoch 27 | Time: 0:10:50.671593 | Train Loss: 0.3117 | Test Loss: 0.3620 | Train Acc: 95.82% | Test Acc: 91.76% | Gaps: 0.0503 / ~4.07% | LR: 1.25e-05
* Epoch 28 | Time: 0:11:14.437678 | Train Loss: 0.3130 | Test Loss: 0.3747 | Train Acc: 95.49% | Test Acc: 92.16% | Gaps: 0.0617 / ~3.32% | LR: 1.25e-05
* Epoch 29 | Time: 0:11:38.107050 | Train Loss: 0.3020 | Test Loss: 0.3612 | Train Acc: 96.13% | Test Acc: 91.62% | Gaps: 0.0593 / ~4.51% | LR: 1.25e-05
* Epoch 30 | Time: 0:12:01.762945 | Train Loss: 0.2975 | Test Loss: 0.3607 | Train Acc: 95.89% | Test Acc: 93.11% | Gaps: 0.0632 / ~2.78% | LR: 1.25e-05

### Notes:
* model was memorizing very well at the end, want to try dropout on fc with 0.2
* verdict: model reached highest acc and looking at loss difference model became way more stable with learning


# Run #7
## Hyper params

* lr = 1e-4
* epochs = 30
* optimizer = optim.Adam(model.parameters(), lr=lr, weight_decay=1e-4)
* weight = torch.tensor([2.1, 1.0]).to(device)
* loss = nn.CrossEntropyLoss(weight=weight, label_smoothing=0.1)
* scheduler = optim.lr_scheduler.MultiStepLR(optimizer, milestones=[10, 20, 25], gamma=0.5)
* self.fc = nn.Sequential(**nn.Dropout(0.2)**, nn.Linear(512, 2))


## Augmentation
```
v2.Resize((256, 256)),
v2.RandomCrop(size=(224, 224)),
v2.RandomHorizontalFlip(p=0.5),
v2.ColorJitter(brightness=0.125, contrast=0.125, saturation=0.1),
v2.RandomGrayscale(0.5),
v2.Normalize(
    mean=[0.479, 0.446, 0.395],
    std=[0.262, 0.257, 0.265]
)
```

## Output

* Epoch 1 | Time: 0:00:29.869184 | Train Loss: 0.7167 | Test Loss: 0.7279 | Train Acc: 56.28% | Test Acc: 44.59% | Gaps: 0.0113 / ~11.69% | LR: 0.0001
* Epoch 2 | Time: 0:00:56.633573 | Train Loss: 0.6822 | Test Loss: 0.6491 | Train Acc: 58.83% | Test Acc: 62.97% | Gaps: 0.0332 / ~4.15% | LR: 0.0001
* Epoch 3 | Time: 0:01:22.922236 | Train Loss: 0.6699 | Test Loss: 0.6573 | Train Acc: 62.25% | Test Acc: 61.76% | Gaps: 0.0126 / ~0.50% | LR: 0.0001
* Epoch 4 | Time: 0:01:48.794887 | Train Loss: 0.6681 | Test Loss: 0.6514 | Train Acc: 61.71% | Test Acc: 61.35% | Gaps: 0.0167 / ~0.36% | LR: 0.0001
* Epoch 5 | Time: 0:02:14.188172 | Train Loss: 0.6373 | Test Loss: 0.6198 | Train Acc: 66.23% | Test Acc: 68.38% | Gaps: 0.0174 / ~2.15% | LR: 0.0001
* Epoch 6 | Time: 0:02:39.351004 | Train Loss: 0.6101 | Test Loss: 0.6304 | Train Acc: 69.55% | Test Acc: 59.19% | Gaps: 0.0203 / ~10.36% | LR: 0.0001
* Epoch 7 | Time: 0:03:04.651057 | Train Loss: 0.5850 | Test Loss: 0.5700 | Train Acc: 72.34% | Test Acc: 75.41% | Gaps: 0.0150 / ~3.07% | LR: 0.0001
* Epoch 8 | Time: 0:03:29.214385 | Train Loss: 0.5614 | Test Loss: 0.7687 | Train Acc: 74.68% | Test Acc: 74.32% | Gaps: 0.2073 / ~0.35% | LR: 0.0001
* Epoch 9 | Time: 0:03:53.585606 | Train Loss: 0.5429 | Test Loss: 0.6713 | Train Acc: 76.58% | Test Acc: 76.22% | Gaps: 0.1284 / ~0.36% | LR: 0.0001
* Epoch 10 | Time: 0:04:19.186497 | Train Loss: 0.5284 | Test Loss: 0.5500 | Train Acc: 78.04% | Test Acc: 71.35% | Gaps: 0.0216 / ~6.69% | LR: 0.0001
* Epoch 11 | Time: 0:04:43.583868 | Train Loss: 0.4722 | Test Loss: 0.5108 | Train Acc: 82.93% | Test Acc: 82.57% | Gaps: 0.0386 / ~0.36% | LR: 5e-05
* Epoch 12 | Time: 0:05:07.801179 | Train Loss: 0.4621 | Test Loss: 0.4674 | Train Acc: 83.74% | Test Acc: 79.73% | Gaps: 0.0053 / ~4.01% | LR: 5e-05
* Epoch 13 | Time: 0:05:33.158701 | Train Loss: 0.4357 | Test Loss: 0.4433 | Train Acc: 85.44% | Test Acc: 86.62% | Gaps: 0.0075 / ~1.18% | LR: 5e-05
* Epoch 14 | Time: 0:05:58.847557 | Train Loss: 0.4336 | Test Loss: 0.4713 | Train Acc: 86.73% | Test Acc: 79.05% | Gaps: 0.0377 / ~7.67% | LR: 5e-05
* Epoch 15 | Time: 0:06:24.243922 | Train Loss: 0.4220 | Test Loss: 0.4453 | Train Acc: 87.24% | Test Acc: 87.70% | Gaps: 0.0233 / ~0.47% | LR: 5e-05
* Epoch 16 | Time: 0:06:49.725911 | Train Loss: 0.4136 | Test Loss: 0.4850 | Train Acc: 87.14% | Test Acc: 83.51% | Gaps: 0.0714 / ~3.62% | LR: 5e-05
* Epoch 17 | Time: 0:07:27.976616 | Train Loss: 0.4108 | Test Loss: 0.4583 | Train Acc: 88.49% | Test Acc: 87.97% | Gaps: 0.0475 / ~0.52% | LR: 5e-05
* Epoch 18 | Time: 0:07:51.772794 | Train Loss: 0.3963 | Test Loss: 0.4094 | Train Acc: 88.93% | Test Acc: 89.73% | Gaps: 0.0131 / ~0.80% | LR: 5e-05
* Epoch 19 | Time: 0:08:15.545528 | Train Loss: 0.3964 | Test Loss: 0.4365 | Train Acc: 89.51% | Test Acc: 83.38% | Gaps: 0.0401 / ~6.13% | LR: 5e-05
* Epoch 20 | Time: 0:08:39.299574 | Train Loss: 0.3798 | Test Loss: 0.4648 | Train Acc: 90.50% | Test Acc: 80.81% | Gaps: 0.0849 / ~9.68% | LR: 5e-05
* Epoch 21 | Time: 0:09:03.135417 | Train Loss: 0.3499 | Test Loss: 0.3748 | Train Acc: 92.19% | Test Acc: 91.08% | Gaps: 0.0249 / ~1.11% | LR: 2.5e-05
* Epoch 22 | Time: 0:09:26.826071 | Train Loss: 0.3513 | Test Loss: 0.3778 | Train Acc: 92.29% | Test Acc: 90.00% | Gaps: 0.0265 / ~2.29% | LR: 2.5e-05
* Epoch 23 | Time: 0:09:51.097883 | Train Loss: 0.3470 | Test Loss: 0.3692 | Train Acc: 92.46% | Test Acc: 91.49% | Gaps: 0.0222 / ~0.98% | LR: 2.5e-05
* Epoch 24 | Time: 0:10:16.668451 | Train Loss: 0.3378 | Test Loss: 0.4275 | Train Acc: 93.08% | Test Acc: 90.27% | Gaps: 0.0897 / ~2.81% | LR: 2.5e-05
* Epoch 25 | Time: 0:10:43.107706 | Train Loss: 0.3234 | Test Loss: 0.3624 | Train Acc: 94.57% | Test Acc: 92.03% | Gaps: 0.0390 / ~2.54% | LR: 2.5e-05
* Epoch 26 | Time: 0:11:12.885906 | Train Loss: 0.3325 | Test Loss: 0.3775 | Train Acc: 93.79% | Test Acc: 90.14% | Gaps: 0.0451 / ~3.65% | LR: 1.25e-05
* Epoch 27 | Time: 0:11:37.960450 | Train Loss: 0.3141 | Test Loss: 0.3624 | Train Acc: 94.91% | Test Acc: 91.62% | Gaps: 0.0483 / ~3.29% | LR: 1.25e-05
* Epoch 28 | Time: 0:12:04.217310 | Train Loss: 0.3145 | Test Loss: 0.3668 | Train Acc: 95.42% | Test Acc: 91.22% | Gaps: 0.0523 / ~4.20% | LR: 1.25e-05
* Epoch 29 | Time: 0:12:36.289393 | Train Loss: 0.3197 | Test Loss: 0.3555 | Train Acc: 94.94% | Test Acc: 92.57% | Gaps: 0.0358 / ~2.37% | LR: 1.25e-05
* Epoch 30 | Time: 0:13:02.149161 | Train Loss: 0.3114 | Test Loss: 0.3740 | Train Acc: 95.42% | Test Acc: 92.70% | Gaps: 0.0626 / ~2.71% | LR: 1.25e-05

### Notes:
* a little test on grayscale aug probability

# Run #8
## Hyper params

* lr = 1e-4
* epochs = 30
* optimizer = optim.Adam(model.parameters(), lr=lr, weight_decay=1e-4)
* weight = torch.tensor([2.1, 1.0]).to(device)
* loss = nn.CrossEntropyLoss(weight=weight, label_smoothing=0.1)
* scheduler = optim.lr_scheduler.MultiStepLR(optimizer, milestones=[10, 20, 25], gamma=0.5)
* self.fc = nn.Sequential(**nn.Dropout(0.2)**, nn.Linear(512, 2))


## Augmentation
```
v2.Resize((256, 256)),
v2.RandomCrop(size=(224, 224)),
v2.RandomHorizontalFlip(p=0.5),
v2.ColorJitter(brightness=0.125, contrast=0.125, saturation=0.1, hue=0.05),
v2.RandomGrayscale(0.35),
v2.Normalize(
    mean=[0.479, 0.446, 0.395],
    std=[0.262, 0.257, 0.265]
)
```

added hue with 0.05 and decreased random gray to 0.35

## Output

* Epoch 1 | Time: 0:00:30.055750 | Train Loss: 0.7431 | Test Loss: 0.7156 | Train Acc: 54.68% | Test Acc: 61.76% | Gaps: 0.0275 / ~7.07% | LR: 0.0001
* Epoch 2 | Time: 0:00:59.139191 | Train Loss: 0.6952 | Test Loss: 0.6853 | Train Acc: 58.96% | Test Acc: 66.22% | Gaps: 0.0099 / ~7.25% | LR: 0.0001
* Epoch 3 | Time: 0:01:27.134419 | Train Loss: 0.6768 | Test Loss: 0.6744 | Train Acc: 60.15% | Test Acc: 65.27% | Gaps: 0.0024 / ~5.12% | LR: 0.0001
* Epoch 4 | Time: 0:01:55.795627 | Train Loss: 0.6672 | Test Loss: 0.6553 | Train Acc: 62.25% | Test Acc: 64.05% | Gaps: 0.0118 / ~1.80% | LR: 0.0001
* Epoch 5 | Time: 0:02:24.012673 | Train Loss: 0.6535 | Test Loss: 0.6211 | Train Acc: 63.03% | Test Acc: 68.78% | Gaps: 0.0324 / ~5.75% | LR: 0.0001
* Epoch 6 | Time: 0:02:52.408828 | Train Loss: 0.6251 | Test Loss: 0.7084 | Train Acc: 67.92% | Test Acc: 69.32% | Gaps: 0.0833 / ~1.40% | LR: 0.0001
* Epoch 7 | Time: 0:03:33.299257 | Train Loss: 0.6017 | Test Loss: 0.6530 | Train Acc: 69.72% | Test Acc: 55.14% | Gaps: 0.0512 / ~14.59% | LR: 0.0001
* Epoch 8 | Time: 0:04:15.838717 | Train Loss: 0.5996 | Test Loss: 0.7915 | Train Acc: 71.01% | Test Acc: 74.19% | Gaps: 0.1918 / ~3.18% | LR: 0.0001
* Epoch 9 | Time: 0:04:52.513968 | Train Loss: 0.5632 | Test Loss: 0.5882 | Train Acc: 73.93% | Test Acc: 72.30% | Gaps: 0.0250 / ~1.63% | LR: 0.0001
* Epoch 10 | Time: 0:05:24.376373 | Train Loss: 0.5332 | Test Loss: 0.5907 | Train Acc: 76.58% | Test Acc: 78.65% | Gaps: 0.0575 / ~2.07% | LR: 0.0001
* Epoch 11 | Time: 0:05:53.042694 | Train Loss: 0.4970 | Test Loss: 0.5315 | Train Acc: 79.97% | Test Acc: 69.73% | Gaps: 0.0346 / ~10.24% | LR: 5e-05
* Epoch 12 | Time: 0:06:19.402980 | Train Loss: 0.4793 | Test Loss: 0.5073 | Train Acc: 82.21% | Test Acc: 85.68% | Gaps: 0.0280 / ~3.46% | LR: 5e-05
* Epoch 13 | Time: 0:06:45.772173 | Train Loss: 0.4684 | Test Loss: 0.4792 | Train Acc: 83.23% | Test Acc: 85.95% | Gaps: 0.0109 / ~2.71% | LR: 5e-05
* Epoch 14 | Time: 0:07:11.962726 | Train Loss: 0.4517 | Test Loss: 0.5109 | Train Acc: 85.23% | Test Acc: 86.89% | Gaps: 0.0592 / ~1.66% | LR: 5e-05
* Epoch 15 | Time: 0:07:38.122145 | Train Loss: 0.4375 | Test Loss: 0.4675 | Train Acc: 85.34% | Test Acc: 82.57% | Gaps: 0.0300 / ~2.77% | LR: 5e-05
* Epoch 16 | Time: 0:08:04.603965 | Train Loss: 0.4496 | Test Loss: 0.4313 | Train Acc: 85.30% | Test Acc: 88.51% | Gaps: 0.0182 / ~3.21% | LR: 5e-05
* Epoch 17 | Time: 0:08:30.933977 | Train Loss: 0.4277 | Test Loss: 0.4544 | Train Acc: 86.76% | Test Acc: 80.68% | Gaps: 0.0267 / ~6.09% | LR: 5e-05
* Epoch 18 | Time: 0:08:57.099552 | Train Loss: 0.4114 | Test Loss: 0.4285 | Train Acc: 87.47% | Test Acc: 87.57% | Gaps: 0.0172 / ~0.09% | LR: 5e-05
* Epoch 19 | Time: 0:09:23.939274 | Train Loss: 0.3986 | Test Loss: 0.4182 | Train Acc: 89.00% | Test Acc: 89.32% | Gaps: 0.0195 / ~0.32% | LR: 5e-05
* Epoch 20 | Time: 0:09:50.449593 | Train Loss: 0.3950 | Test Loss: 0.6902 | Train Acc: 89.00% | Test Acc: 66.08% | Gaps: 0.2952 / ~22.92% | LR: 5e-05
* Epoch 21 | Time: 0:10:17.777724 | Train Loss: 0.3837 | Test Loss: 0.3959 | Train Acc: 90.60% | Test Acc: 92.70% | Gaps: 0.0122 / ~2.11% | LR: 2.5e-05
* Epoch 22 | Time: 0:10:44.200327 | Train Loss: 0.3666 | Test Loss: 0.3945 | Train Acc: 91.48% | Test Acc: 90.68% | Gaps: 0.0279 / ~0.80% | LR: 2.5e-05
* Epoch 23 | Time: 0:11:08.945235 | Train Loss: 0.3614 | Test Loss: 0.4133 | Train Acc: 91.62% | Test Acc: 86.76% | Gaps: 0.0519 / ~4.86% | LR: 2.5e-05
* Epoch 24 | Time: 0:11:33.569865 | Train Loss: 0.3570 | Test Loss: 0.3859 | Train Acc: 92.23% | Test Acc: 88.92% | Gaps: 0.0288 / ~3.31% | LR: 2.5e-05
* Epoch 25 | Time: 0:11:58.226379 | Train Loss: 0.3423 | Test Loss: 0.4039 | Train Acc: 93.28% | Test Acc: 90.41% | Gaps: 0.0616 / ~2.87% | LR: 2.5e-05
* Epoch 26 | Time: 0:12:22.800105 | Train Loss: 0.3373 | Test Loss: 0.3860 | Train Acc: 93.75% | Test Acc: 91.89% | Gaps: 0.0487 / ~1.86% | LR: 1.25e-05
* Epoch 27 | Time: 0:12:47.512808 | Train Loss: 0.3340 | Test Loss: 0.3765 | Train Acc: 93.52% | Test Acc: 90.41% | Gaps: 0.0425 / ~3.11% | LR: 1.25e-05
* Epoch 28 | Time: 0:13:12.466785 | Train Loss: 0.3194 | Test Loss: 0.3722 | Train Acc: 94.77% | Test Acc: 90.00% | Gaps: 0.0529 / ~4.77% | LR: 1.25e-05
* Epoch 29 | Time: 0:13:37.113807 | Train Loss: 0.3299 | Test Loss: 0.3969 | Train Acc: 94.57% | Test Acc: 87.70% | Gaps: 0.0670 / ~6.87% | LR: 1.25e-05
* Epoch 30 | Time: 0:14:01.725072 | Train Loss: 0.3094 | Test Loss: 0.3655 | Train Acc: 95.82% | Test Acc: 92.97% | Gaps: 0.0561 / ~2.85% | LR: 1.25e-05

### Notes:
* Hue def not helping here, but I think we found a sweet spot for gray scale
* let's change out scheduler

# Run #9
## Hyper params

* lr = 1e-4
* epochs = 35
* optimizer = optim.Adam(model.parameters(), lr=lr, weight_decay=1e-4)
* weight = torch.tensor([2.1, 1.0]).to(device)
* loss = nn.CrossEntropyLoss(weight=weight, label_smoothing=0.1)
* scheduler = optim.lr_scheduler.MultiStepLR(optimizer, milestones=[10, 20, 25, 30], gamma=0.5)
* self.fc = nn.Sequential(**nn.Dropout(0.1)**, nn.Linear(512, 2))

## Augmentation
```
v2.Resize((256, 256)),
v2.RandomCrop(size=(224, 224)),
v2.RandomHorizontalFlip(p=0.5),
v2.ColorJitter(brightness=0.125, contrast=0.125, saturation=0.1),
v2.RandomGrayscale(0.2),
v2.Normalize(
    mean=[0.479, 0.446, 0.395],
    std=[0.262, 0.257, 0.265]
)
```

## Output

* Epoch 1 | Time: 0:00:30.062232 | Train Loss: 0.7262 | Test Loss: 0.6882 | Train Acc: 55.40% | Test Acc: 55.14% | Gaps: 0.0381 / ~0.26% | LR: 0.0001
* Epoch 2 | Time: 0:00:58.515703 | Train Loss: 0.6786 | Test Loss: 0.7517 | Train Acc: 61.54% | Test Acc: 39.73% | Gaps: 0.0731 / ~21.81% | LR: 0.0001
* Epoch 3 | Time: 0:01:25.206997 | Train Loss: 0.6591 | Test Loss: 0.7260 | Train Acc: 63.20% | Test Acc: 45.54% | Gaps: 0.0669 / ~17.66% | LR: 0.0001
* Epoch 4 | Time: 0:01:51.891753 | Train Loss: 0.6401 | Test Loss: 0.6467 | Train Acc: 65.48% | Test Acc: 56.89% | Gaps: 0.0066 / ~8.59% | LR: 0.0001
* Epoch 5 | Time: 0:02:18.473074 | Train Loss: 0.6127 | Test Loss: 0.7835 | Train Acc: 69.28% | Test Acc: 41.62% | Gaps: 0.1707 / ~27.66% | LR: 0.0001
* Epoch 6 | Time: 0:02:45.233538 | Train Loss: 0.5962 | Test Loss: 0.6388 | Train Acc: 72.10% | Test Acc: 56.62% | Gaps: 0.0426 / ~15.48% | LR: 0.0001
* Epoch 7 | Time: 0:03:11.894294 | Train Loss: 0.5716 | Test Loss: 0.6219 | Train Acc: 73.01% | Test Acc: 63.11% | Gaps: 0.0503 / ~9.91% | LR: 0.0001
* Epoch 8 | Time: 0:03:38.552773 | Train Loss: 0.5376 | Test Loss: 0.6237 | Train Acc: 76.78% | Test Acc: 60.95% | Gaps: 0.0861 / ~15.84% | LR: 0.0001
* Epoch 9 | Time: 0:04:05.140181 | Train Loss: 0.5155 | Test Loss: 0.6397 | Train Acc: 78.99% | Test Acc: 58.78% | Gaps: 0.1243 / ~20.20% | LR: 0.0001
* Epoch 10 | Time: 0:04:31.820703 | Train Loss: 0.4945 | Test Loss: 0.5322 | Train Acc: 81.13% | Test Acc: 70.27% | Gaps: 0.0377 / ~10.86% | LR: 0.0001
* Epoch 11 | Time: 0:04:58.318810 | Train Loss: 0.4580 | Test Loss: 0.4594 | Train Acc: 84.22% | Test Acc: 81.76% | Gaps: 0.0014 / ~2.46% | LR: 5e-05
* Epoch 12 | Time: 0:05:25.045232 | Train Loss: 0.4346 | Test Loss: 0.5747 | Train Acc: 86.08% | Test Acc: 86.22% | Gaps: 0.1401 / ~0.13% | LR: 5e-05
* Epoch 13 | Time: 0:05:51.667417 | Train Loss: 0.4180 | Test Loss: 0.4488 | Train Acc: 87.47% | Test Acc: 81.76% | Gaps: 0.0309 / ~5.72% | LR: 5e-05
* Epoch 14 | Time: 0:06:18.230840 | Train Loss: 0.4152 | Test Loss: 0.4480 | Train Acc: 88.29% | Test Acc: 85.95% | Gaps: 0.0327 / ~2.34% | LR: 5e-05
* Epoch 15 | Time: 0:06:44.943689 | Train Loss: 0.4062 | Test Loss: 0.4956 | Train Acc: 88.15% | Test Acc: 75.68% | Gaps: 0.0894 / ~12.48% | LR: 5e-05
* Epoch 16 | Time: 0:07:11.525911 | Train Loss: 0.3979 | Test Loss: 0.4556 | Train Acc: 88.53% | Test Acc: 79.86% | Gaps: 0.0577 / ~8.66% | LR: 5e-05
* Epoch 17 | Time: 0:07:38.261837 | Train Loss: 0.3891 | Test Loss: 0.4357 | Train Acc: 90.16% | Test Acc: 80.41% | Gaps: 0.0466 / ~9.75% | LR: 5e-05
* Epoch 18 | Time: 0:08:04.878072 | Train Loss: 0.3829 | Test Loss: 0.5361 | Train Acc: 90.60% | Test Acc: 69.46% | Gaps: 0.1532 / ~21.14% | LR: 5e-05
* Epoch 19 | Time: 0:08:31.557803 | Train Loss: 0.3777 | Test Loss: 0.4643 | Train Acc: 90.90% | Test Acc: 86.22% | Gaps: 0.0866 / ~4.69% | LR: 5e-05
* Epoch 20 | Time: 0:08:58.112114 | Train Loss: 0.3668 | Test Loss: 0.4195 | Train Acc: 91.48% | Test Acc: 88.92% | Gaps: 0.0527 / ~2.56% | LR: 5e-05
* Epoch 21 | Time: 0:09:24.661756 | Train Loss: 0.3408 | Test Loss: 0.3900 | Train Acc: 93.08% | Test Acc: 87.84% | Gaps: 0.0493 / ~5.24% | LR: 2.5e-05
* Epoch 22 | Time: 0:09:51.280276 | Train Loss: 0.3319 | Test Loss: 0.3797 | Train Acc: 94.37% | Test Acc: 89.19% | Gaps: 0.0478 / ~5.18% | LR: 2.5e-05
* Epoch 23 | Time: 0:10:17.891281 | Train Loss: 0.3339 | Test Loss: 0.4258 | Train Acc: 93.79% | Test Acc: 91.22% | Gaps: 0.0919 / ~2.57% | LR: 2.5e-05
* Epoch 24 | Time: 0:10:44.566793 | Train Loss: 0.3311 | Test Loss: 0.4253 | Train Acc: 93.45% | Test Acc: 83.38% | Gaps: 0.0942 / ~10.07% | LR: 2.5e-05
* Epoch 25 | Time: 0:11:11.070463 | Train Loss: 0.3213 | Test Loss: 0.3636 | Train Acc: 94.67% | Test Acc: 92.97% | Gaps: 0.0423 / ~1.70% | LR: 2.5e-05
* Epoch 26 | Time: 0:11:37.626163 | Train Loss: 0.3066 | Test Loss: 0.3641 | Train Acc: 95.76% | Test Acc: 92.16% | Gaps: 0.0575 / ~3.59% | LR: 1.25e-05
* Epoch 27 | Time: 0:12:04.226064 | Train Loss: 0.3015 | Test Loss: 0.3645 | Train Acc: 95.93% | Test Acc: 92.43% | Gaps: 0.0630 / ~3.49% | LR: 1.25e-05
* Epoch 28 | Time: 0:12:30.747030 | Train Loss: 0.2946 | Test Loss: 0.3668 | Train Acc: 96.67% | Test Acc: 88.51% | Gaps: 0.0722 / ~8.16% | LR: 1.25e-05
* Epoch 29 | Time: 0:12:57.357766 | Train Loss: 0.2972 | Test Loss: 0.3619 | Train Acc: 96.50% | Test Acc: 91.49% | Gaps: 0.0647 / ~5.02% | LR: 1.25e-05
* Epoch 30 | Time: 0:13:23.996577 | Train Loss: 0.2901 | Test Loss: 0.3602 | Train Acc: 97.05% | Test Acc: 92.84% | Gaps: 0.0701 / ~4.21% | LR: 1.25e-05

### Notes:
* decreased dropouts to 0.1, random gray to 0.2

# Run #10

## Description

I separated my ResNet18 model into Classifier which is responsible for classifying from given features and
Backbone that is responsible for extracting features this will give me ability to set different lrs for each stage also will be very useful with 
freezing the model in the future when training Localizer, have to mention that feature extractor have to learn steady and classifier have to adapt faster
that's why lr 1e-04 for my ResNet18 model was good but not the best now since I'm able to give two different lr result will be higher

## Hyper params

params = [
    {
        'params': backbone.parameters(),
        "lr": 1e-04
    },
    {
        'params': classifier.parameters(),
        "lr": 1e-03
    }
]

* lrs = backbone: 1e-4, classifier: 1e-03
* epochs = 30
* optimizer = optim.Adam(params, weight_decay=1e-4)
* weight = torch.tensor([2.1, 1.0]).to(device)
* loss = nn.CrossEntropyLoss(weight=weight, label_smoothing=0.1)
* scheduler = optim.lr_scheduler.MultiStepLR(optimizer, milestones=[10, 20, 25, 30], gamma=0.5)
* dropout in classifier set to 0.1

## Augmentation
```
v2.Resize((256, 256)),
v2.RandomCrop(size=(224, 224)),
v2.RandomHorizontalFlip(p=0.5),
v2.ColorJitter(brightness=0.125, contrast=0.125, saturation=0.1),
v2.RandomGrayscale(0.2),
v2.Normalize(
    mean=[0.479, 0.446, 0.395],
    std=[0.262, 0.257, 0.265]
)
```

## Output

* Epoch 1 | Time: 0:00:28.036980 | Train Loss: 0.7315 | Test Loss: 0.6782 | Train Acc: 54.41% | Test Acc: 65.27% | Gaps: 0.0532 / ~10.86% | LR backbone: 0.0001 | LR classifier: 0.001
* Epoch 2 | Time: 0:00:55.668402 | Train Loss: 0.6833 | Test Loss: 0.7464 | Train Acc: 60.66% | Test Acc: 65.00% | Gaps: 0.0632 / ~4.34% | LR backbone: 0.0001 | LR classifier: 0.001
* Epoch 3 | Time: 0:01:23.316626 | Train Loss: 0.6761 | Test Loss: 0.6348 | Train Acc: 62.02% | Test Acc: 66.49% | Gaps: 0.0413 / ~4.47% | LR backbone: 0.0001 | LR classifier: 0.001
* Epoch 4 | Time: 0:01:50.593848 | Train Loss: 0.6449 | Test Loss: 0.6450 | Train Acc: 65.24% | Test Acc: 71.76% | Gaps: 0.0001 / ~6.52% | LR backbone: 0.0001 | LR classifier: 0.001
* Epoch 5 | Time: 0:02:17.298424 | Train Loss: 0.6331 | Test Loss: 0.6409 | Train Acc: 67.35% | Test Acc: 60.68% | Gaps: 0.0077 / ~6.67% | LR backbone: 0.0001 | LR classifier: 0.001
* Epoch 6 | Time: 0:02:43.582564 | Train Loss: 0.6160 | Test Loss: 0.5947 | Train Acc: 70.23% | Test Acc: 73.38% | Gaps: 0.0214 / ~3.15% | LR backbone: 0.0001 | LR classifier: 0.001
* Epoch 7 | Time: 0:03:10.393254 | Train Loss: 0.5820 | Test Loss: 0.6229 | Train Acc: 72.81% | Test Acc: 56.22% | Gaps: 0.0408 / ~16.59% | LR backbone: 0.0001 | LR classifier: 0.001
* Epoch 8 | Time: 0:03:36.275610 | Train Loss: 0.5716 | Test Loss: 0.5507 | Train Acc: 73.83% | Test Acc: 70.54% | Gaps: 0.0209 / ~3.29% | LR backbone: 0.0001 | LR classifier: 0.001
* Epoch 9 | Time: 0:04:03.994238 | Train Loss: 0.5515 | Test Loss: 0.5527 | Train Acc: 77.36% | Test Acc: 75.95% | Gaps: 0.0012 / ~1.41% | LR backbone: 0.0001 | LR classifier: 0.001
* Epoch 10 | Time: 0:04:31.280471 | Train Loss: 0.5287 | Test Loss: 0.6069 | Train Acc: 78.72% | Test Acc: 73.92% | Gaps: 0.0782 / ~4.80% | LR backbone: 0.0001 | LR classifier: 0.001
* Epoch 11 | Time: 0:04:58.731098 | Train Loss: 0.4732 | Test Loss: 0.4686 | Train Acc: 82.96% | Test Acc: 82.30% | Gaps: 0.0046 / ~0.66% | LR backbone: 5e-05 | LR classifier: 0.0005
* Epoch 12 | Time: 0:05:26.062552 | Train Loss: 0.4420 | Test Loss: 0.4689 | Train Acc: 85.61% | Test Acc: 80.95% | Gaps: 0.0269 / ~4.66% | LR backbone: 5e-05 | LR classifier: 0.0005
* Epoch 13 | Time: 0:05:52.741376 | Train Loss: 0.4297 | Test Loss: 0.4648 | Train Acc: 85.85% | Test Acc: 80.41% | Gaps: 0.0351 / ~5.44% | LR backbone: 5e-05 | LR classifier: 0.0005
* Epoch 14 | Time: 0:06:19.392874 | Train Loss: 0.4246 | Test Loss: 0.4499 | Train Acc: 87.10% | Test Acc: 83.65% | Gaps: 0.0253 / ~3.45% | LR backbone: 5e-05 | LR classifier: 0.0005
* Epoch 15 | Time: 0:06:46.267205 | Train Loss: 0.4117 | Test Loss: 0.4762 | Train Acc: 87.34% | Test Acc: 76.49% | Gaps: 0.0645 / ~10.85% | LR backbone: 5e-05 | LR classifier: 0.0005
* Epoch 16 | Time: 0:07:12.846758 | Train Loss: 0.4077 | Test Loss: 0.4539 | Train Acc: 89.10% | Test Acc: 82.70% | Gaps: 0.0463 / ~6.40% | LR backbone: 5e-05 | LR classifier: 0.0005
* Epoch 17 | Time: 0:07:39.120196 | Train Loss: 0.4007 | Test Loss: 0.4692 | Train Acc: 89.17% | Test Acc: 77.57% | Gaps: 0.0685 / ~11.60% | LR backbone: 5e-05 | LR classifier: 0.0005
* Epoch 18 | Time: 0:08:05.520966 | Train Loss: 0.3926 | Test Loss: 0.4145 | Train Acc: 88.97% | Test Acc: 88.51% | Gaps: 0.0219 / ~0.45% | LR backbone: 5e-05 | LR classifier: 0.0005
* Epoch 19 | Time: 0:08:31.675701 | Train Loss: 0.3687 | Test Loss: 0.4039 | Train Acc: 91.24% | Test Acc: 89.19% | Gaps: 0.0353 / ~2.05% | LR backbone: 5e-05 | LR classifier: 0.0005
* Epoch 20 | Time: 0:08:58.178572 | Train Loss: 0.3637 | Test Loss: 0.4865 | Train Acc: 91.82% | Test Acc: 76.08% | Gaps: 0.1227 / ~15.74% | LR backbone: 5e-05 | LR classifier: 0.0005
* Epoch 21 | Time: 0:09:25.460543 | Train Loss: 0.3440 | Test Loss: 0.4176 | Train Acc: 93.41% | Test Acc: 83.92% | Gaps: 0.0736 / ~9.50% | LR backbone: 2.5e-05 | LR classifier: 0.00025
* Epoch 22 | Time: 0:09:51.987088 | Train Loss: 0.3310 | Test Loss: 0.3890 | Train Acc: 93.75% | Test Acc: 91.62% | Gaps: 0.0581 / ~2.13% | LR backbone: 2.5e-05 | LR classifier: 0.00025
* Epoch 23 | Time: 0:10:18.541143 | Train Loss: 0.3336 | Test Loss: 0.3799 | Train Acc: 94.09% | Test Acc: 91.76% | Gaps: 0.0464 / ~2.34% | LR backbone: 2.5e-05 | LR classifier: 0.00025
* Epoch 24 | Time: 0:10:44.349765 | Train Loss: 0.3315 | Test Loss: 0.3977 | Train Acc: 93.48% | Test Acc: 91.22% | Gaps: 0.0662 / ~2.27% | LR backbone: 2.5e-05 | LR classifier: 0.00025
* Epoch 25 | Time: 0:11:09.859318 | Train Loss: 0.3149 | Test Loss: 0.3628 | Train Acc: 95.15% | Test Acc: 90.95% | Gaps: 0.0478 / ~4.20% | LR backbone: 2.5e-05 | LR classifier: 0.00025
* Epoch 26 | Time: 0:11:35.208918 | Train Loss: 0.3141 | Test Loss: 0.3655 | Train Acc: 95.25% | Test Acc: 91.22% | Gaps: 0.0515 / ~4.03% | LR backbone: 1.25e-05 | LR classifier: 0.000125
* Epoch 27 | Time: 0:12:00.947007 | Train Loss: 0.3045 | Test Loss: 0.3617 | Train Acc: 95.59% | Test Acc: 91.22% | Gaps: 0.0572 / ~4.37% | LR backbone: 1.25e-05 | LR classifier: 0.000125
* Epoch 28 | Time: 0:12:26.746766 | Train Loss: 0.2978 | Test Loss: 0.3642 | Train Acc: 96.61% | Test Acc: 91.08% | Gaps: 0.0664 / ~5.52% | LR backbone: 1.25e-05 | LR classifier: 0.000125
* Epoch 29 | Time: 0:12:52.180470 | Train Loss: 0.2965 | Test Loss: 0.3575 | Train Acc: 96.61% | Test Acc: 91.76% | Gaps: 0.0610 / ~4.85% | LR backbone: 1.25e-05 | LR classifier: 0.000125
* Epoch 30 | Time: 0:13:17.334910 | Train Loss: 0.2969 | Test Loss: 0.3519 | Train Acc: 96.57% | Test Acc: 94.05% | Gaps: 0.0551 / ~2.52% | LR backbone: 1.25e-05 | LR classifier: 0.000125

### Notes:
* Max accuracy was reached simply by separating models into 2 and giving 2 lrs

# Run #11

## Description

After going through my dataset I noticed that my model was getting distracted by lots of noise and humans on the samples 
I cleaned up dataset by removing them

## Hyper params

params = [
    {
        'params': backbone.parameters(),
        "lr": 1e-04
    },
    {
        'params': classifier.parameters(),
        "lr": 1e-03
    }
]

* lrs = backbone: 1e-4, classifier: 1e-03
* epochs = 30
* optimizer = optim.Adam(params, weight_decay=1e-4)
* weight = torch.tensor([2.08, 1.0]).to(device)
* loss = nn.CrossEntropyLoss(weight=weight, label_smoothing=0.1)
* scheduler = optim.lr_scheduler.ReduceLROnPlateau(optimizer, mode='max', factor=0.5, patience=3)

## Augmentation
```
v2.Resize((448, 448)),
# v2.RandomCrop(size=(412, 412)),
v2.RandomHorizontalFlip(p=0.5),
v2.ColorJitter(brightness=0.125, contrast=0.125, saturation=0.1),
v2.RandomGrayscale(0.2),
v2.Normalize(
    mean=[0.479, 0.446, 0.395],
    std=[0.262, 0.257, 0.265]
)
```

## Output

* Epoch 1 | Time: 0:00:49.727952 | Train Loss: 0.7516 | Test Loss: 0.9307 | Train Acc: 53.62% | Test Acc: 68.22% | Gaps: 0.1791 / ~14.60% | LR backbone: 0.0001 | LR classifier: 0.001
* Epoch 2 | Time: 0:01:38.971981 | Train Loss: 0.7043 | Test Loss: 0.7586 | Train Acc: 55.10% | Test Acc: 63.70% | Gaps: 0.0542 / ~8.60% | LR backbone: 0.0001 | LR classifier: 0.001
* Epoch 3 | Time: 0:02:28.268925 | Train Loss: 0.7054 | Test Loss: 0.9740 | Train Acc: 56.61% | Test Acc: 57.34% | Gaps: 0.2686 / ~0.73% | LR backbone: 0.0001 | LR classifier: 0.001
* Epoch 4 | Time: 0:03:17.718431 | Train Loss: 0.6902 | Test Loss: 1.1742 | Train Acc: 56.03% | Test Acc: 59.18% | Gaps: 0.4840 / ~3.15% | LR backbone: 0.0001 | LR classifier: 0.001
* Epoch 5 | Time: 0:04:07.191225 | Train Loss: 0.6884 | Test Loss: 0.7168 | Train Acc: 58.68% | Test Acc: 62.29% | Gaps: 0.0285 / ~3.61% | LR backbone: 0.0001 | LR classifier: 0.001
* Epoch 6 | Time: 0:04:58.097424 | Train Loss: 0.6833 | Test Loss: 0.6865 | Train Acc: 58.99% | Test Acc: 46.61% | Gaps: 0.0032 / ~12.38% | LR backbone: 0.0001 | LR classifier: 0.001
* Epoch 7 | Time: 0:05:47.862118 | Train Loss: 0.6756 | Test Loss: 0.7830 | Train Acc: 59.99% | Test Acc: 66.38% | Gaps: 0.1074 / ~6.40% | LR backbone: 0.0001 | LR classifier: 0.001
* Epoch 8 | Time: 0:06:37.029465 | Train Loss: 0.6814 | Test Loss: 0.7035 | Train Acc: 61.26% | Test Acc: 56.64% | Gaps: 0.0220 / ~4.62% | LR backbone: 0.0001 | LR classifier: 0.001
* Epoch 9 | Time: 0:07:26.404710 | Train Loss: 0.6573 | Test Loss: 0.6585 | Train Acc: 62.33% | Test Acc: 63.84% | Gaps: 0.0011 / ~1.51% | LR backbone: 0.0001 | LR classifier: 0.001
* Epoch 10 | Time: 0:08:15.770003 | Train Loss: 0.6536 | Test Loss: 0.6478 | Train Acc: 63.74% | Test Acc: 68.50% | Gaps: 0.0057 / ~4.76% | LR backbone: 0.0001 | LR classifier: 0.001
* Epoch 11 | Time: 0:09:05.199558 | Train Loss: 0.6268 | Test Loss: 0.8456 | Train Acc: 68.39% | Test Acc: 74.01% | Gaps: 0.2188 / ~5.62% | LR backbone: 5e-05 | LR classifier: 0.0005
* Epoch 12 | Time: 0:09:54.557709 | Train Loss: 0.6027 | Test Loss: 0.6608 | Train Acc: 70.14% | Test Acc: 52.97% | Gaps: 0.0581 / ~17.18% | LR backbone: 5e-05 | LR classifier: 0.0005
* Epoch 13 | Time: 0:10:44.872115 | Train Loss: 0.5899 | Test Loss: 0.7334 | Train Acc: 71.87% | Test Acc: 74.01% | Gaps: 0.1435 / ~2.14% | LR backbone: 5e-05 | LR classifier: 0.0005
* Epoch 14 | Time: 0:11:34.553362 | Train Loss: 0.5653 | Test Loss: 0.7152 | Train Acc: 73.66% | Test Acc: 59.60% | Gaps: 0.1499 / ~14.05% | LR backbone: 5e-05 | LR classifier: 0.0005
* Epoch 15 | Time: 0:12:23.755246 | Train Loss: 0.5554 | Test Loss: 0.8642 | Train Acc: 75.76% | Test Acc: 74.01% | Gaps: 0.3087 / ~1.75% | LR backbone: 5e-05 | LR classifier: 0.0005
* Epoch 16 | Time: 0:13:13.081114 | Train Loss: 0.5207 | Test Loss: 0.9311 | Train Acc: 77.03% | Test Acc: 74.01% | Gaps: 0.4104 / ~3.02% | LR backbone: 5e-05 | LR classifier: 0.0005
* Epoch 17 | Time: 0:14:02.485694 | Train Loss: 0.5145 | Test Loss: 0.6291 | Train Acc: 78.62% | Test Acc: 69.49% | Gaps: 0.1146 / ~9.12% | LR backbone: 5e-05 | LR classifier: 0.0005
* Epoch 18 | Time: 0:14:51.875827 | Train Loss: 0.5059 | Test Loss: 0.6367 | Train Acc: 78.79% | Test Acc: 80.08% | Gaps: 0.1308 / ~1.30% | LR backbone: 5e-05 | LR classifier: 0.0005
* Epoch 19 | Time: 0:15:41.444035 | Train Loss: 0.4928 | Test Loss: 0.7223 | Train Acc: 81.34% | Test Acc: 54.94% | Gaps: 0.2295 / ~26.39% | LR backbone: 5e-05 | LR classifier: 0.0005
* Epoch 20 | Time: 0:16:30.700514 | Train Loss: 0.4751 | Test Loss: 0.9175 | Train Acc: 82.95% | Test Acc: 78.11% | Gaps: 0.4424 / ~4.85% | LR backbone: 5e-05 | LR classifier: 0.0005
* Epoch 21 | Time: 0:17:20.102077 | Train Loss: 0.4347 | Test Loss: 0.4966 | Train Acc: 85.23% | Test Acc: 77.82% | Gaps: 0.0619 / ~7.40% | LR backbone: 2.5e-05 | LR classifier: 0.00025
* Epoch 22 | Time: 0:18:09.288296 | Train Loss: 0.4162 | Test Loss: 0.4493 | Train Acc: 87.26% | Test Acc: 83.47% | Gaps: 0.0330 / ~3.78% | LR backbone: 2.5e-05 | LR classifier: 0.00025
* Epoch 23 | Time: 0:18:58.421422 | Train Loss: 0.4084 | Test Loss: 0.6712 | Train Acc: 88.60% | Test Acc: 70.20% | Gaps: 0.2628 / ~18.40% | LR backbone: 2.5e-05 | LR classifier: 0.00025
* Epoch 24 | Time: 0:19:47.814572 | Train Loss: 0.4101 | Test Loss: 0.5690 | Train Acc: 89.15% | Test Acc: 84.04% | Gaps: 0.1589 / ~5.11% | LR backbone: 2.5e-05 | LR classifier: 0.00025
* Epoch 25 | Time: 0:20:37.168022 | Train Loss: 0.3903 | Test Loss: 0.5792 | Train Acc: 90.25% | Test Acc: 78.81% | Gaps: 0.1889 / ~11.44% | LR backbone: 2.5e-05 | LR classifier: 0.00025
* Epoch 26 | Time: 0:21:26.595457 | Train Loss: 0.3869 | Test Loss: 0.4119 | Train Acc: 89.22% | Test Acc: 87.71% | Gaps: 0.0250 / ~1.51% | LR backbone: 1.25e-05 | LR classifier: 0.000125
* Epoch 27 | Time: 0:22:15.976909 | Train Loss: 0.3618 | Test Loss: 0.4251 | Train Acc: 91.98% | Test Acc: 88.56% | Gaps: 0.0633 / ~3.42% | LR backbone: 1.25e-05 | LR classifier: 0.000125
* Epoch 28 | Time: 0:23:05.330073 | Train Loss: 0.3625 | Test Loss: 0.4131 | Train Acc: 91.25% | Test Acc: 85.88% | Gaps: 0.0505 / ~5.38% | LR backbone: 1.25e-05 | LR classifier: 0.000125
* Epoch 29 | Time: 0:23:54.754368 | Train Loss: 0.3585 | Test Loss: 0.4330 | Train Acc: 92.42% | Test Acc: 85.45% | Gaps: 0.0745 / ~6.97% | LR backbone: 1.25e-05 | LR classifier: 0.000125
* Epoch 30 | Time: 0:24:43.917260 | Train Loss: 0.3536 | Test Loss: 0.4138 | Train Acc: 92.22% | Test Acc: 88.70% | Gaps: 0.0601 / ~3.52% | LR backbone: 1.25e-05 | LR classifier: 0.000125

### Notes:
* Lower accuracy but higher CIoU in localization, accuracy will improve when two heads are trained together


# Run #12

## Description



## Hyper params

* lrs = backbone: 1e-4, classifier: 1e-04
* epochs = 30
* optimizer = optim.AdamW([
    {'params': backbone.parameters(),  "lr": 1e-04, "weight_decay": 1e-03},
    {'params': classifier.parameters(), "lr": 1e-04, "weight_decay": 1e-03}
])
* weight = torch.tensor([2.08, 1.0]).to(device)
* loss = nn.CrossEntropyLoss(weight=weight, label_smoothing=0.1)
* scheduler = optim.lr_scheduler.ReduceLROnPlateau(optimizer, mode='max', factor=0.5, patience=3)

## Augmentation
```
v2.Resize((448, 448)),
v2.RandomCrop(size=(412, 412)),
v2.RandomHorizontalFlip(p=0.5),
v2.ColorJitter(brightness=0.125, contrast=0.125, saturation=0.1),
v2.RandomGrayscale(0.2),
v2.Normalize(
    mean=[0.479, 0.446, 0.395],
    std=[0.262, 0.257, 0.265]
)
```

## Output

* #1 Time: 0:00:50.609276 | Train Loss: 0.7265 | Test Loss: 0.6624 | Train Acc: 55.37% | Test Acc: 57.77% | Gaps: -0.0642 / 2.40% | LR backbone: 0.0001 | LR classifier: 0.0001
* #2 Time: 0:01:41.006141 | Train Loss: 0.6819 | Test Loss: 0.6743 | Train Acc: 59.09% | Test Acc: 61.16% | Gaps: -0.0076 / 2.07% | LR backbone: 0.0001 | LR classifier: 0.0001
* #3 Time: 0:02:31.374682 | Train Loss: 0.6819 | Test Loss: 0.7038 | Train Acc: 59.23% | Test Acc: 66.81% | Gaps: 0.0220 / 7.58% | LR backbone: 0.0001 | LR classifier: 0.0001
* #4 Time: 0:03:22.238376 | Train Loss: 0.6712 | Test Loss: 0.7231 | Train Acc: 62.05% | Test Acc: 49.72% | Gaps: 0.0519 / -12.33% | LR backbone: 0.0001 | LR classifier: 0.0001
* #5 Time: 0:04:12.060878 | Train Loss: 0.6638 | Test Loss: 0.6494 | Train Acc: 62.05% | Test Acc: 60.31% | Gaps: -0.0144 / -1.74% | LR backbone: 0.0001 | LR classifier: 0.0001
* #6 Time: 0:05:02.784985 | Train Loss: 0.6736 | Test Loss: 0.6630 | Train Acc: 58.99% | Test Acc: 66.81% | Gaps: -0.0106 / 7.82% | LR backbone: 0.0001 | LR classifier: 0.0001
* #7 Time: 0:05:52.605549 | Train Loss: 0.6673 | Test Loss: 0.6832 | Train Acc: 61.16% | Test Acc: 68.08% | Gaps: 0.0159 / 6.92% | LR backbone: 0.0001 | LR classifier: 0.0001
* #8 Time: 0:06:44.011607 | Train Loss: 0.6592 | Test Loss: 0.7820 | Train Acc: 62.47% | Test Acc: 45.20% | Gaps: 0.1229 / -17.27% | LR backbone: 0.0001 | LR classifier: 0.0001
* #9 Time: 0:07:36.288422 | Train Loss: 0.6571 | Test Loss: 0.6568 | Train Acc: 64.19% | Test Acc: 65.40% | Gaps: -0.0003 / 1.21% | LR backbone: 0.0001 | LR classifier: 0.0001
* #10 Time: 0:08:26.533475 | Train Loss: 0.6413 | Test Loss: 0.8838 | Train Acc: 66.94% | Test Acc: 68.22% | Gaps: 0.2425 / 1.28% | LR backbone: 0.0001 | LR classifier: 0.0001
* #11 Time: 0:09:16.331230 | Train Loss: 0.6260 | Test Loss: 0.6485 | Train Acc: 68.18% | Test Acc: 66.67% | Gaps: 0.0225 / -1.52% | LR backbone: 5e-05 | LR classifier: 5e-05
* #12 Time: 0:10:07.158222 | Train Loss: 0.5978 | Test Loss: 0.6043 | Train Acc: 71.11% | Test Acc: 65.82% | Gaps: 0.0065 / -5.29% | LR backbone: 5e-05 | LR classifier: 5e-05
* #13 Time: 0:10:56.898460 | Train Loss: 0.5840 | Test Loss: 0.6371 | Train Acc: 72.45% | Test Acc: 73.59% | Gaps: 0.0531 / 1.14% | LR backbone: 5e-05 | LR classifier: 5e-05
* #14 Time: 0:11:47.314031 | Train Loss: 0.5553 | Test Loss: 0.5931 | Train Acc: 75.48% | Test Acc: 75.71% | Gaps: 0.0378 / 0.22% | LR backbone: 5e-05 | LR classifier: 5e-05
* #15 Time: 0:12:37.469074 | Train Loss: 0.5504 | Test Loss: 0.6013 | Train Acc: 76.34% | Test Acc: 76.13% | Gaps: 0.0509 / -0.21% | LR backbone: 5e-05 | LR classifier: 5e-05
* #16 Time: 0:13:27.451467 | Train Loss: 0.5263 | Test Loss: 0.5236 | Train Acc: 78.48% | Test Acc: 75.56% | Gaps: -0.0027 / -2.91% | LR backbone: 5e-05 | LR classifier: 5e-05
* #17 Time: 0:14:17.663619 | Train Loss: 0.5133 | Test Loss: 0.5326 | Train Acc: 79.34% | Test Acc: 78.53% | Gaps: 0.0194 / -0.81% | LR backbone: 5e-05 | LR classifier: 5e-05
* #18 Time: 0:15:08.055647 | Train Loss: 0.5005 | Test Loss: 0.5765 | Train Acc: 80.03% | Test Acc: 81.50% | Gaps: 0.0760 / 1.47% | LR backbone: 5e-05 | LR classifier: 5e-05
* #19 Time: 0:15:57.530000 | Train Loss: 0.4712 | Test Loss: 0.6044 | Train Acc: 83.44% | Test Acc: 83.19% | Gaps: 0.1333 / -0.24% | LR backbone: 5e-05 | LR classifier: 5e-05
* #20 Time: 0:16:46.913375 | Train Loss: 0.4657 | Test Loss: 0.5044 | Train Acc: 83.85% | Test Acc: 86.44% | Gaps: 0.0387 / 2.59% | LR backbone: 5e-05 | LR classifier: 5e-05
* #21 Time: 0:17:36.069745 | Train Loss: 0.4249 | Test Loss: 0.6516 | Train Acc: 86.57% | Test Acc: 83.90% | Gaps: 0.2268 / -2.67% | LR backbone: 2.5e-05 | LR classifier: 2.5e-05
* #22 Time: 0:18:25.466403 | Train Loss: 0.4148 | Test Loss: 0.4329 | Train Acc: 87.53% | Test Acc: 86.30% | Gaps: 0.0181 / -1.24% | LR backbone: 2.5e-05 | LR classifier: 2.5e-05
* #23 Time: 0:19:14.893306 | Train Loss: 0.3993 | Test Loss: 0.4261 | Train Acc: 88.22% | Test Acc: 88.84% | Gaps: 0.0268 / 0.62% | LR backbone: 2.5e-05 | LR classifier: 2.5e-05
* #24 Time: 0:20:04.236732 | Train Loss: 0.3827 | Test Loss: 0.4347 | Train Acc: 90.63% | Test Acc: 89.12% | Gaps: 0.0520 / -1.51% | LR backbone: 2.5e-05 | LR classifier: 2.5e-05
* #25 Time: 0:20:53.597110 | Train Loss: 0.3806 | Test Loss: 0.4586 | Train Acc: 91.15% | Test Acc: 88.98% | Gaps: 0.0780 / -2.17% | LR backbone: 2.5e-05 | LR classifier: 2.5e-05
* #26 Time: 0:21:42.978774 | Train Loss: 0.3529 | Test Loss: 0.4238 | Train Acc: 92.67% | Test Acc: 91.38% | Gaps: 0.0710 / -1.28% | LR backbone: 1.25e-05 | LR classifier: 1.25e-05
* #27 Time: 0:22:32.246299 | Train Loss: 0.3523 | Test Loss: 0.4238 | Train Acc: 92.91% | Test Acc: 91.53% | Gaps: 0.0715 / -1.38% | LR backbone: 1.25e-05 | LR classifier: 1.25e-05
* #28 Time: 0:23:21.433929 | Train Loss: 0.3501 | Test Loss: 0.4160 | Train Acc: 93.29% | Test Acc: 91.81% | Gaps: 0.0659 / -1.48% | LR backbone: 1.25e-05 | LR classifier: 1.25e-05
* #29 Time: 0:24:10.774773 | Train Loss: 0.3329 | Test Loss: 0.3784 | Train Acc: 94.21% | Test Acc: 92.09% | Gaps: 0.0456 / -2.12% | LR backbone: 1.25e-05 | LR classifier: 1.25e-05
* #30 Time: 0:25:00.131814 | Train Loss: 0.3354 | Test Loss: 0.4090 | Train Acc: 94.04% | Test Acc: 92.09% | Gaps: 0.0737 / -1.95% | LR backbone: 1.25e-05 | LR classifier: 1.25e-05

### Notes:
* Changed lr to 0.0001 for both heads


# Run #13

## Description
The latest one see - graph.png

## Hyper params

* lrs = backbone: 1e-4, classifier: 1e-04
* epochs = 30
* optimizer = optim.AdamW(
[
    {'params': backbone.parameters(),  "lr": 1e-04, "weight_decay": 1e-03},
    {'params': classifier.parameters(), "lr": 1e-04, "weight_decay": 1e-03}
])
* loss = nn.CrossEntropyLoss(weight=torch.tensor([2.08, 1.0]).to(device), label_smoothing=0.1)
* scheduler = optim.lr_scheduler.MultiStepLR(optimizer, milestones=[10, 20, 25], gamma=0.5)
self.fc = nn.Sequential(
            nn.Dropout(0.1),
            nn.Linear(512,2)
        )

## Augmentation
```
v2.Resize((448, 448)),
v2.RandomCrop(size=(412, 412)),  # Uncomment when training classifier
v2.RandomHorizontalFlip(p=0.5),
v2.ColorJitter(brightness=0.125, contrast=0.125, saturation=0.1),
v2.RandomGrayscale(0.2),
v2.Normalize(
    mean=[0.479, 0.446, 0.395],
    std=[0.262, 0.257, 0.265]
)
```

## Output

* #1 Time: 0:00:49 | Train Loss: 0.7326 | Test Loss: 0.6893 | Train Acc: 54.58% | Test Acc: 60.73% | Gaps: -0.0433 / 6.15% | LR-cls: 0.0001 | LR-bck: 0.0001
* #2 Time: 0:01:39 | Train Loss: 0.6948 | Test Loss: 0.7011 | Train Acc: 57.20% | Test Acc: 54.66% | Gaps: 0.0063 / -2.54% | LR-cls: 0.0001 | LR-bck: 0.0001
* #3 Time: 0:02:28 | Train Loss: 0.6869 | Test Loss: 0.6664 | Train Acc: 58.78% | Test Acc: 65.68% | Gaps: -0.0205 / 6.90% | LR-cls: 0.0001 | LR-bck: 0.0001
* #4 Time: 0:03:18 | Train Loss: 0.6795 | Test Loss: 0.6771 | Train Acc: 60.19% | Test Acc: 58.33% | Gaps: -0.0024 / -1.86% | LR-cls: 0.0001 | LR-bck: 0.0001
* #5 Time: 0:04:07 | Train Loss: 0.6703 | Test Loss: 0.6461 | Train Acc: 62.26% | Test Acc: 70.48% | Gaps: -0.0242 / 8.22% | LR-cls: 0.0001 | LR-bck: 0.0001
* #6 Time: 0:04:56 | Train Loss: 0.6542 | Test Loss: 0.6715 | Train Acc: 65.22% | Test Acc: 56.36% | Gaps: 0.0173 / -8.86% | LR-cls: 0.0001 | LR-bck: 0.0001
* #7 Time: 0:05:45 | Train Loss: 0.6368 | Test Loss: 0.7029 | Train Acc: 66.25% | Test Acc: 47.32% | Gaps: 0.0661 / -18.94% | LR-cls: 0.0001 | LR-bck: 0.0001
* #8 Time: 0:06:34 | Train Loss: 0.6169 | Test Loss: 0.6978 | Train Acc: 68.15% | Test Acc: 73.73% | Gaps: 0.0809 / 5.58% | LR-cls: 0.0001 | LR-bck: 0.0001
* #9 Time: 0:07:23 | Train Loss: 0.5993 | Test Loss: 0.6134 | Train Acc: 71.42% | Test Acc: 62.01% | Gaps: 0.0141 / -9.41% | LR-cls: 0.0001 | LR-bck: 0.0001
* #10 Time: 0:08:15 | Train Loss: 0.5946 | Test Loss: 0.5868 | Train Acc: 71.87% | Test Acc: 73.16% | Gaps: -0.0077 / 1.30% | LR-cls: 0.0001 | LR-bck: 0.0001
* #11 Time: 0:09:04 | Train Loss: 0.5415 | Test Loss: 0.5754 | Train Acc: 77.00% | Test Acc: 68.36% | Gaps: 0.0339 / -8.64% | LR-cls: 5e-05 | LR-bck: 5e-05
* #12 Time: 0:09:53 | Train Loss: 0.5211 | Test Loss: 0.5300 | Train Acc: 77.96% | Test Acc: 78.11% | Gaps: 0.0089 / 0.15% | LR-cls: 5e-05 | LR-bck: 5e-05
* #13 Time: 0:10:42 | Train Loss: 0.5084 | Test Loss: 0.5198 | Train Acc: 79.89% | Test Acc: 79.66% | Gaps: 0.0115 / -0.23% | LR-cls: 5e-05 | LR-bck: 5e-05
* #14 Time: 0:11:31 | Train Loss: 0.4900 | Test Loss: 0.5402 | Train Acc: 80.61% | Test Acc: 71.19% | Gaps: 0.0502 / -9.43% | LR-cls: 5e-05 | LR-bck: 5e-05
* #15 Time: 0:12:20 | Train Loss: 0.4777 | Test Loss: 0.5355 | Train Acc: 82.92% | Test Acc: 70.76% | Gaps: 0.0578 / -12.16% | LR-cls: 5e-05 | LR-bck: 5e-05
* #16 Time: 0:13:09 | Train Loss: 0.4563 | Test Loss: 0.4842 | Train Acc: 83.82% | Test Acc: 80.93% | Gaps: 0.0279 / -2.88% | LR-cls: 5e-05 | LR-bck: 5e-05
* #17 Time: 0:13:58 | Train Loss: 0.4433 | Test Loss: 0.5998 | Train Acc: 85.12% | Test Acc: 60.73% | Gaps: 0.1564 / -24.39% | LR-cls: 5e-05 | LR-bck: 5e-05
* #18 Time: 0:14:47 | Train Loss: 0.4290 | Test Loss: 0.4780 | Train Acc: 87.09% | Test Acc: 84.46% | Gaps: 0.0490 / -2.62% | LR-cls: 5e-05 | LR-bck: 5e-05
* #19 Time: 0:15:36 | Train Loss: 0.4167 | Test Loss: 0.4881 | Train Acc: 86.95% | Test Acc: 75.42% | Gaps: 0.0713 / -11.53% | LR-cls: 5e-05 | LR-bck: 5e-05
* #20 Time: 0:16:25 | Train Loss: 0.3999 | Test Loss: 0.4336 | Train Acc: 88.43% | Test Acc: 86.72% | Gaps: 0.0338 / -1.71% | LR-cls: 5e-05 | LR-bck: 5e-05
* #21 Time: 0:17:14 | Train Loss: 0.3774 | Test Loss: 0.3973 | Train Acc: 90.77% | Test Acc: 87.71% | Gaps: 0.0199 / -3.06% | LR-cls: 2.5e-05 | LR-bck: 2.5e-05
* #22 Time: 0:18:03 | Train Loss: 0.3700 | Test Loss: 0.4230 | Train Acc: 91.43% | Test Acc: 85.03% | Gaps: 0.0530 / -6.40% | LR-cls: 2.5e-05 | LR-bck: 2.5e-05
* #23 Time: 0:18:52 | Train Loss: 0.3651 | Test Loss: 0.4792 | Train Acc: 92.15% | Test Acc: 76.41% | Gaps: 0.1140 / -15.74% | LR-cls: 2.5e-05 | LR-bck: 2.5e-05
* #24 Time: 0:19:42 | Train Loss: 0.3577 | Test Loss: 0.4153 | Train Acc: 92.15% | Test Acc: 84.60% | Gaps: 0.0576 / -7.54% | LR-cls: 2.5e-05 | LR-bck: 2.5e-05
* #25 Time: 0:20:31 | Train Loss: 0.3422 | Test Loss: 0.4273 | Train Acc: 93.63% | Test Acc: 81.50% | Gaps: 0.0851 / -12.13% | LR-cls: 2.5e-05 | LR-bck: 2.5e-05
* #26 Time: 0:21:20 | Train Loss: 0.3357 | Test Loss: 0.3541 | Train Acc: 94.28% | Test Acc: 91.81% | Gaps: 0.0184 / -2.48% | LR-cls: 1.25e-05 | LR-bck: 1.25e-05
* #27 Time: 0:22:09 | Train Loss: 0.3286 | Test Loss: 0.3708 | Train Acc: 95.11% | Test Acc: 89.41% | Gaps: 0.0422 / -5.70% | LR-cls: 1.25e-05 | LR-bck: 1.25e-05
* #28 Time: 0:22:58 | Train Loss: 0.3235 | Test Loss: 0.3502 | Train Acc: 94.46% | Test Acc: 92.51% | Gaps: 0.0267 / -1.94% | LR-cls: 1.25e-05 | LR-bck: 1.25e-05
* #29 Time: 0:23:47 | Train Loss: 0.3277 | Test Loss: 0.3536 | Train Acc: 94.39% | Test Acc: 92.37% | Gaps: 0.0260 / -2.01% | LR-cls: 1.25e-05 | LR-bck: 1.25e-05
* #30 Time: 0:24:36 | Train Loss: 0.3141 | Test Loss: 0.3423 | Train Acc: 95.56% | Test Acc: 92.51% | Gaps: 0.0283 / -3.04% | LR-cls: 1.25e-05 | LR-bck: 1.25e-05

### Notes:
v2.RandomCrop(size=(412, 412)) - used
Dropouts added
Scheduler changed