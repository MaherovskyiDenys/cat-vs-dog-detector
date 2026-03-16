# Run #1 - graph.png
## Hyper params

* lr = 1e-4 / 1e-4 / 1e-5
* epochs = 30
* optimizer = optim.AdamW([
        {"params": model.localizer.parameters(), "lr": 1e-04, "weight_decay": 1e-04},
        {"params": model.classifier.parameters(), "lr": 1e-04, "weight_decay": 1e-04},
        {"params": model.backbone.block4.parameters(), "lr": 1e-05, "weight_decay": 1e-04}
    ])
* loss = 1.0 * loss_localizer + 0.5 * loss_classifier

## Augmentation
```
v2.Resize((448, 448)),
# v2.RandomCrop(size=(412, 412)),  # Uncomment when training classifier
v2.RandomHorizontalFlip(p=0.5),
v2.ColorJitter(brightness=0.125, contrast=0.125, saturation=0.1),
v2.RandomGrayscale(0.2),
v2.Normalize(
    mean=[0.479, 0.446, 0.395],
    std=[0.262, 0.257, 0.265]
)
```

# Unfreeze backbone's block 3
if epoch == 5:
    for param in model.backbone.block3.parameters():
        param.requires_grad = True
    optimizer.add_param_group(
        {"params": model.backbone.block3.parameters(), "lr": 1e-05, "weight_decay": 1e-05}
    )

# Unfreeze whole backbone
if epoch == 10:
    for param in model.backbone.block2.parameters():
        param.requires_grad = True
    for param in model.backbone.block1.parameters():
        param.requires_grad = True
    for param in model.backbone.conv.parameters():
        param.requires_grad = True
    optimizer.add_param_group(
        {"params": model.backbone.block2.parameters(), "lr": 1e-05, "weight_decay": 1e-05},
    )
    optimizer.add_param_group(
        {"params": model.backbone.block1.parameters(), "lr": 1e-05, "weight_decay": 1e-05},
    )
    optimizer.add_param_group(
        {"params": model.backbone.conv.parameters(), "lr": 1e-05, "weight_decay": 1e-05},
    )


## Output

* #1 Time: 0:00:37 | Train Loss: 0.4375 | Test Loss: 0.4925 | Train Acc: 81.96% | Test Acc: 84.89% | Train CIoU: 0.8170 | Test CIoU: 0.7231 | LR-loc: 0.0001 | LR-cls: 0.0001 | LR-bck: 1e-05
* #2 Time: 0:01:15 | Train Loss: 0.3946 | Test Loss: 0.4742 | Train Acc: 88.74% | Test Acc: 87.15% | Train CIoU: 0.8134 | Test CIoU: 0.7223 | LR-loc: 0.0001 | LR-cls: 0.0001 | LR-bck: 1e-05
* #3 Time: 0:01:52 | Train Loss: 0.3749 | Test Loss: 0.4642 | Train Acc: 90.74% | Test Acc: 87.15% | Train CIoU: 0.8190 | Test CIoU: 0.7265 | LR-loc: 0.0001 | LR-cls: 0.0001 | LR-bck: 1e-05
* #4 Time: 0:02:30 | Train Loss: 0.3679 | Test Loss: 0.4534 | Train Acc: 91.67% | Test Acc: 90.54% | Train CIoU: 0.8188 | Test CIoU: 0.7306 | LR-loc: 0.0001 | LR-cls: 0.0001 | LR-bck: 1e-05
* #5 Time: 0:03:07 | Train Loss: 0.3649 | Test Loss: 0.4608 | Train Acc: 91.98% | Test Acc: 89.27% | Train CIoU: 0.8199 | Test CIoU: 0.7229 | LR-loc: 0.0001 | LR-cls: 0.0001 | LR-bck: 1e-05
* #6 Time: 0:03:48 | Train Loss: 0.3638 | Test Loss: 0.4644 | Train Acc: 91.70% | Test Acc: 90.40% | Train CIoU: 0.8220 | Test CIoU: 0.7146 | LR-loc: 0.0001 | LR-cls: 0.0001 | LR-bck: 1e-05
* #7 Time: 0:04:29 | Train Loss: 0.3477 | Test Loss: 0.4509 | Train Acc: 93.77% | Test Acc: 90.54% | Train CIoU: 0.8246 | Test CIoU: 0.7267 | LR-loc: 0.0001 | LR-cls: 0.0001 | LR-bck: 1e-05
* #8 Time: 0:05:10 | Train Loss: 0.3483 | Test Loss: 0.4464 | Train Acc: 93.46% | Test Acc: 92.09% | Train CIoU: 0.8242 | Test CIoU: 0.7262 | LR-loc: 0.0001 | LR-cls: 0.0001 | LR-bck: 1e-05
* #9 Time: 0:05:50 | Train Loss: 0.3308 | Test Loss: 0.4374 | Train Acc: 93.90% | Test Acc: 93.93% | Train CIoU: 0.8370 | Test CIoU: 0.7378 | LR-loc: 5e-05 | LR-cls: 5e-05 | LR-bck: 5e-06
* #10 Time: 0:06:31 | Train Loss: 0.3244 | Test Loss: 0.4328 | Train Acc: 94.94% | Test Acc: 93.93% | Train CIoU: 0.8403 | Test CIoU: 0.7375 | LR-loc: 5e-05 | LR-cls: 5e-05 | LR-bck: 5e-06
* #11 Time: 0:07:30 | Train Loss: 0.3261 | Test Loss: 0.4375 | Train Acc: 94.70% | Test Acc: 91.95% | Train CIoU: 0.8416 | Test CIoU: 0.7334 | LR-loc: 5e-05 | LR-cls: 5e-05 | LR-bck: 5e-06
* #12 Time: 0:08:29 | Train Loss: 0.3199 | Test Loss: 0.4395 | Train Acc: 95.63% | Test Acc: 94.35% | Train CIoU: 0.8432 | Test CIoU: 0.7320 | LR-loc: 5e-05 | LR-cls: 5e-05 | LR-bck: 5e-06
* #13 Time: 0:09:30 | Train Loss: 0.3218 | Test Loss: 0.4316 | Train Acc: 95.01% | Test Acc: 93.36% | Train CIoU: 0.8413 | Test CIoU: 0.7369 | LR-loc: 5e-05 | LR-cls: 5e-05 | LR-bck: 5e-06
* #14 Time: 0:10:31 | Train Loss: 0.3070 | Test Loss: 0.4326 | Train Acc: 96.49% | Test Acc: 94.35% | Train CIoU: 0.8516 | Test CIoU: 0.7408 | LR-loc: 2.5e-05 | LR-cls: 2.5e-05 | LR-bck: 2.5e-06
* #15 Time: 0:11:31 | Train Loss: 0.2982 | Test Loss: 0.4327 | Train Acc: 96.83% | Test Acc: 93.93% | Train CIoU: 0.8553 | Test CIoU: 0.7353 | LR-loc: 2.5e-05 | LR-cls: 2.5e-05 | LR-bck: 2.5e-06
* #16 Time: 0:12:30 | Train Loss: 0.3018 | Test Loss: 0.4304 | Train Acc: 96.25% | Test Acc: 91.67% | Train CIoU: 0.8551 | Test CIoU: 0.7394 | LR-loc: 2.5e-05 | LR-cls: 2.5e-05 | LR-bck: 2.5e-06
* #17 Time: 0:13:35 | Train Loss: 0.3024 | Test Loss: 0.4300 | Train Acc: 96.25% | Test Acc: 92.09% | Train CIoU: 0.8554 | Test CIoU: 0.7396 | LR-loc: 2.5e-05 | LR-cls: 2.5e-05 | LR-bck: 2.5e-06
* #18 Time: 0:14:34 | Train Loss: 0.2992 | Test Loss: 0.4278 | Train Acc: 96.73% | Test Acc: 94.49% | Train CIoU: 0.8548 | Test CIoU: 0.7381 | LR-loc: 2.5e-05 | LR-cls: 2.5e-05 | LR-bck: 2.5e-06
* #19 Time: 0:15:32 | Train Loss: 0.2943 | Test Loss: 0.4263 | Train Acc: 96.76% | Test Acc: 93.50% | Train CIoU: 0.8592 | Test CIoU: 0.7412 | LR-loc: 1.25e-05 | LR-cls: 1.25e-05 | LR-bck: 1.25e-06
* #20 Time: 0:16:31 | Train Loss: 0.2906 | Test Loss: 0.4270 | Train Acc: 96.94% | Test Acc: 94.35% | Train CIoU: 0.8625 | Test CIoU: 0.7416 | LR-loc: 1.25e-05 | LR-cls: 1.25e-05 | LR-bck: 1.25e-06
* #21 Time: 0:17:30 | Train Loss: 0.2908 | Test Loss: 0.4254 | Train Acc: 97.07% | Test Acc: 93.08% | Train CIoU: 0.8622 | Test CIoU: 0.7418 | LR-loc: 1.25e-05 | LR-cls: 1.25e-05 | LR-bck: 1.25e-06
* #22 Time: 0:18:29 | Train Loss: 0.2898 | Test Loss: 0.4253 | Train Acc: 96.90% | Test Acc: 94.77% | Train CIoU: 0.8624 | Test CIoU: 0.7424 | LR-loc: 1.25e-05 | LR-cls: 1.25e-05 | LR-bck: 1.25e-06
* #23 Time: 0:19:28 | Train Loss: 0.2877 | Test Loss: 0.4333 | Train Acc: 96.94% | Test Acc: 89.12% | Train CIoU: 0.8643 | Test CIoU: 0.7429 | LR-loc: 1.25e-05 | LR-cls: 1.25e-05 | LR-bck: 1.25e-06
* #24 Time: 0:20:27 | Train Loss: 0.2893 | Test Loss: 0.4243 | Train Acc: 96.52% | Test Acc: 93.50% | Train CIoU: 0.8634 | Test CIoU: 0.7421 | LR-loc: 1.25e-05 | LR-cls: 1.25e-05 | LR-bck: 1.25e-06
* #25 Time: 0:21:25 | Train Loss: 0.2874 | Test Loss: 0.4233 | Train Acc: 96.90% | Test Acc: 93.08% | Train CIoU: 0.8649 | Test CIoU: 0.7435 | LR-loc: 1.25e-05 | LR-cls: 1.25e-05 | LR-bck: 1.25e-06
* #26 Time: 0:22:24 | Train Loss: 0.2885 | Test Loss: 0.4239 | Train Acc: 96.83% | Test Acc: 93.64% | Train CIoU: 0.8653 | Test CIoU: 0.7419 | LR-loc: 1.25e-05 | LR-cls: 1.25e-05 | LR-bck: 1.25e-06
* #27 Time: 0:23:24 | Train Loss: 0.2832 | Test Loss: 0.4253 | Train Acc: 97.14% | Test Acc: 91.24% | Train CIoU: 0.8677 | Test CIoU: 0.7445 | LR-loc: 1.25e-05 | LR-cls: 1.25e-05 | LR-bck: 1.25e-06
* #28 Time: 0:24:24 | Train Loss: 0.2847 | Test Loss: 0.4244 | Train Acc: 96.94% | Test Acc: 93.79% | Train CIoU: 0.8673 | Test CIoU: 0.7423 | LR-loc: 1.25e-05 | LR-cls: 1.25e-05 | LR-bck: 1.25e-06
* #29 Time: 0:25:24 | Train Loss: 0.2835 | Test Loss: 0.4251 | Train Acc: 97.31% | Test Acc: 94.07% | Train CIoU: 0.8673 | Test CIoU: 0.7407 | LR-loc: 1.25e-05 | LR-cls: 1.25e-05 | LR-bck: 1.25e-06
* #30 Time: 0:26:27 | Train Loss: 0.2863 | Test Loss: 0.4240 | Train Acc: 96.73% | Test Acc: 93.36% | Train CIoU: 0.8670 | Test CIoU: 0.7419 | LR-loc: 1.25e-05 | LR-cls: 1.25e-05 | LR-bck: 1.25e-06

# Notes
The best/final run. We stop here 
Train/Test Acc: ~96%/94%
Train/Test CIoU: ~0.86/0.74
