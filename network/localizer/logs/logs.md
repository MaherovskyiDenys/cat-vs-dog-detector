# Run #1
## Hyper params

```
    for param in backbone.parameters():
        param.requires_grad = False

    # Unfreeze block 4 only to fine tune params
    for param in backbone.block4.parameters():
        param.requires_grad = True
        
    lr = 0.001 / 0.0001
    epochs = 30
    optimizer = optim.Adam([
        {"params": localizer.parameters(), "lr": 0.001, "weight_decay": 1e-3},
        {"params": backbone.block4.parameters(), "lr": 0.0001, "weight_decay": 1e-4}
    ])
    loss = nn.SmoothL1Loss()
        l1 = loss_func(predicted_bboxes, bboxes)
        d_iou = distance_box_iou_loss(pred_xyxy, true_xyxy, reduction="mean")
        loss = 1.0 * d_iou + 0.3 * l1
    scheduler = optim.lr_scheduler.ReduceLROnPlateau(optimizer, mode='max', factor=0.5, patience=3)

```


## Augmentation
```
v2.ToDtype(torch.float32, scale=True),
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

* #1. Time: 0:00:22 | Train Loss: 0.6349 | Test Loss: 0.5759 | Train IoU: 0.4013 | Test IoU: 0.4468 | LR localizer: 0.001  | LR backbone: 0.0001
* #2. Time: 0:00:45 | Train Loss: 0.5830 | Test Loss: 0.6115 | Train IoU: 0.4472 | Test IoU: 0.4108 | LR localizer: 0.001  | LR backbone: 0.0001
* #3. Time: 0:01:07 | Train Loss: 0.5497 | Test Loss: 0.5423 | Train IoU: 0.4773 | Test IoU: 0.4834 | LR localizer: 0.001  | LR backbone: 0.0001
* #4. Time: 0:01:28 | Train Loss: 0.5291 | Test Loss: 0.5601 | Train IoU: 0.4970 | Test IoU: 0.4631 | LR localizer: 0.001  | LR backbone: 0.0001
* #5. Time: 0:01:59 | Train Loss: 0.5087 | Test Loss: 0.5498 | Train IoU: 0.5164 | Test IoU: 0.4787 | LR localizer: 0.001  | LR backbone: 0.0001
* #6. Time: 0:02:25 | Train Loss: 0.5154 | Test Loss: 0.6960 | Train IoU: 0.5106 | Test IoU: 0.3315 | LR localizer: 0.001  | LR backbone: 0.0001
* #7. Time: 0:02:51 | Train Loss: 0.5435 | Test Loss: 0.5040 | Train IoU: 0.4833 | Test IoU: 0.5198 | LR localizer: 0.001  | LR backbone: 0.0001
* #8. Time: 0:03:17 | Train Loss: 0.5135 | Test Loss: 0.5712 | Train IoU: 0.5118 | Test IoU: 0.4573 | LR localizer: 0.001  | LR backbone: 0.0001
* #9. Time: 0:03:41 | Train Loss: 0.5011 | Test Loss: 0.4961 | Train IoU: 0.5233 | Test IoU: 0.5241 | LR localizer: 0.001  | LR backbone: 0.0001
* #10. Time: 0:04:06 | Train Loss: 0.4896 | Test Loss: 0.5151 | Train IoU: 0.5338 | Test IoU: 0.5069 | LR localizer: 0.001  | LR backbone: 0.0001
* #11. Time: 0:04:32 | Train Loss: 0.4858 | Test Loss: 0.5632 | Train IoU: 0.5375 | Test IoU: 0.4545 | LR localizer: 0.001  | LR backbone: 0.0001
* #12. Time: 0:04:58 | Train Loss: 0.4828 | Test Loss: 0.5203 | Train IoU: 0.5408 | Test IoU: 0.4986 | LR localizer: 0.001  | LR backbone: 0.0001
* #13. Time: 0:05:23 | Train Loss: 0.4765 | Test Loss: 0.5696 | Train IoU: 0.5461 | Test IoU: 0.4504 | LR localizer: 0.001  | LR backbone: 0.0001
* #14. Time: 0:05:47 | Train Loss: 0.4593 | Test Loss: 0.4816 | Train IoU: 0.5615 | Test IoU: 0.5374 | LR localizer: 0.0005  | LR backbone: 5e-05
* #15. Time: 0:06:11 | Train Loss: 0.4575 | Test Loss: 0.4780 | Train IoU: 0.5636 | Test IoU: 0.5402 | LR localizer: 0.0005  | LR backbone: 5e-05
* #16. Time: 0:06:35 | Train Loss: 0.4558 | Test Loss: 0.5319 | Train IoU: 0.5656 | Test IoU: 0.4947 | LR localizer: 0.0005  | LR backbone: 5e-05
* #17. Time: 0:06:59 | Train Loss: 0.4597 | Test Loss: 0.5062 | Train IoU: 0.5620 | Test IoU: 0.5103 | LR localizer: 0.0005  | LR backbone: 5e-05
* #18. Time: 0:07:26 | Train Loss: 0.4472 | Test Loss: 0.4389 | Train IoU: 0.5729 | Test IoU: 0.5784 | LR localizer: 0.0005  | LR backbone: 5e-05
* #19. Time: 0:07:51 | Train Loss: 0.4450 | Test Loss: 0.4936 | Train IoU: 0.5744 | Test IoU: 0.5233 | LR localizer: 0.0005  | LR backbone: 5e-05
* #20. Time: 0:08:16 | Train Loss: 0.4471 | Test Loss: 0.4408 | Train IoU: 0.5732 | Test IoU: 0.5757 | LR localizer: 0.0005  | LR backbone: 5e-05
* #21. Time: 0:08:42 | Train Loss: 0.4456 | Test Loss: 0.4970 | Train IoU: 0.5744 | Test IoU: 0.5200 | LR localizer: 0.0005  | LR backbone: 5e-05
* #22. Time: 0:09:07 | Train Loss: 0.4378 | Test Loss: 0.4417 | Train IoU: 0.5811 | Test IoU: 0.5745 | LR localizer: 0.0005  | LR backbone: 5e-05
* #23. Time: 0:09:32 | Train Loss: 0.4248 | Test Loss: 0.4550 | Train IoU: 0.5934 | Test IoU: 0.5604 | LR localizer: 0.00025  | LR backbone: 2.5e-05
* #24. Time: 0:09:56 | Train Loss: 0.4257 | Test Loss: 0.4605 | Train IoU: 0.5929 | Test IoU: 0.5563 | LR localizer: 0.00025  | LR backbone: 2.5e-05
* #25. Time: 0:10:22 | Train Loss: 0.4186 | Test Loss: 0.4427 | Train IoU: 0.5991 | Test IoU: 0.5728 | LR localizer: 0.00025  | LR backbone: 2.5e-05
* #26. Time: 0:10:48 | Train Loss: 0.4175 | Test Loss: 0.4471 | Train IoU: 0.6002 | Test IoU: 0.5691 | LR localizer: 0.00025  | LR backbone: 2.5e-05
* #27. Time: 0:11:12 | Train Loss: 0.4158 | Test Loss: 0.4565 | Train IoU: 0.6022 | Test IoU: 0.5607 | LR localizer: 0.000125  | LR backbone: 1.25e-05
* #28. Time: 0:11:36 | Train Loss: 0.4079 | Test Loss: 0.4440 | Train IoU: 0.6093 | Test IoU: 0.5719 | LR localizer: 0.000125  | LR backbone: 1.25e-05
* #29. Time: 0:12:03 | Train Loss: 0.4031 | Test Loss: 0.4440 | Train IoU: 0.6138 | Test IoU: 0.5716 | LR localizer: 0.000125  | LR backbone: 1.25e-05
* #30. Time: 0:12:28 | Train Loss: 0.4059 | Test Loss: 0.4506 | Train IoU: 0.6110 | Test IoU: 0.5641 | LR localizer: 0.000125  | LR backbone: 1.25e-05

notes:
First run, max IoU: 0.6110 / 0.5784
Model learning but not the best performance

# Run #2
## Hyper params

```
    for param in backbone.parameters():
        param.requires_grad = False

    # Unfreeze block 4 only to fine tune params
    for param in backbone.block4.parameters():
        param.requires_grad = True
        
    lr = 0.001 / 0.0001 / 0.00001
    epochs = 30
    optimizer = optim.Adam([
        {"params": localizer.parameters(), "lr": 0.001, "weight_decay": 1e-3},
        {"params": backbone.block4.parameters(), "lr": 0.0001, "weight_decay": 1e-4}
    ])
    loss = nn.SmoothL1Loss()
        l1 = loss_func(predicted_bboxes, bboxes)
        d_iou = distance_box_iou_loss(pred_xyxy, true_xyxy, reduction="mean")
        loss = 1.0 * d_iou + 0.3 * l1
    scheduler = optim.lr_scheduler.ReduceLROnPlateau(optimizer, mode='max', factor=0.5, patience=3)
```

updates:
on 15 epoch unfreezing block 3
```
if epoch == 15:
    # unfreeze block 3
    for param in backbone.block3.parameters():
        param.requires_grad = True

    optimizer.add_param_group(
        {"params": backbone.block3.parameters(), "lr": 1e-5, "weight_decay": 1e-5}
    )
```

## Augmentation
```
v2.ToDtype(torch.float32, scale=True),
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

* #1. Time: 0:00:23 | Train Loss: 0.6405 | Test Loss: 0.6046 | Train IoU: 0.3962 | Test IoU: 0.4226 | LR localizer: 0.001  | LR backbone: 0.0001
* #2. Time: 0:00:45 | Train Loss: 0.5924 | Test Loss: 0.5576 | Train IoU: 0.4380 | Test IoU: 0.4641 | LR localizer: 0.001  | LR backbone: 0.0001
* #3. Time: 0:01:08 | Train Loss: 0.5546 | Test Loss: 0.5275 | Train IoU: 0.4729 | Test IoU: 0.4937 | LR localizer: 0.001  | LR backbone: 0.0001
* #4. Time: 0:01:31 | Train Loss: 0.5317 | Test Loss: 0.5868 | Train IoU: 0.4943 | Test IoU: 0.4329 | LR localizer: 0.001  | LR backbone: 0.0001
* #5. Time: 0:01:53 | Train Loss: 0.5188 | Test Loss: 0.5438 | Train IoU: 0.5066 | Test IoU: 0.4745 | LR localizer: 0.001  | LR backbone: 0.0001
* #6. Time: 0:02:15 | Train Loss: 0.5009 | Test Loss: 0.5324 | Train IoU: 0.5231 | Test IoU: 0.4872 | LR localizer: 0.001  | LR backbone: 0.0001
* #7. Time: 0:02:38 | Train Loss: 0.4980 | Test Loss: 0.5821 | Train IoU: 0.5265 | Test IoU: 0.4371 | LR localizer: 0.001  | LR backbone: 0.0001
* #8. Time: 0:03:03 | Train Loss: 0.4755 | Test Loss: 0.4935 | Train IoU: 0.5462 | Test IoU: 0.5247 | LR localizer: 0.0005  | LR backbone: 5e-05
* #9. Time: 0:03:28 | Train Loss: 0.4711 | Test Loss: 0.4833 | Train IoU: 0.5509 | Test IoU: 0.5348 | LR localizer: 0.0005  | LR backbone: 5e-05
* #10. Time: 0:03:54 | Train Loss: 0.4667 | Test Loss: 0.5207 | Train IoU: 0.5551 | Test IoU: 0.4978 | LR localizer: 0.0005  | LR backbone: 5e-05
* #11. Time: 0:04:18 | Train Loss: 0.4611 | Test Loss: 0.5076 | Train IoU: 0.5600 | Test IoU: 0.5127 | LR localizer: 0.0005  | LR backbone: 5e-05
* #12. Time: 0:04:43 | Train Loss: 0.4634 | Test Loss: 0.4622 | Train IoU: 0.5580 | Test IoU: 0.5566 | LR localizer: 0.0005  | LR backbone: 5e-05
* #13. Time: 0:05:08 | Train Loss: 0.4523 | Test Loss: 0.4929 | Train IoU: 0.5686 | Test IoU: 0.5255 | LR localizer: 0.0005  | LR backbone: 5e-05
* #14. Time: 0:05:33 | Train Loss: 0.4517 | Test Loss: 0.4676 | Train IoU: 0.5683 | Test IoU: 0.5487 | LR localizer: 0.0005  | LR backbone: 5e-05
* #15. Time: 0:05:58 | Train Loss: 0.4411 | Test Loss: 0.4606 | Train IoU: 0.5778 | Test IoU: 0.5588 | LR localizer: 0.0005  | LR backbone: 5e-05
* #16. Time: 0:06:20 | Train Loss: 0.4491 | Test Loss: 0.4778 | Train IoU: 0.5712 | Test IoU: 0.5408 | LR localizer: 0.0005  | LR backbone: 5e-05
* #17. Time: 0:06:45 | Train Loss: 0.4424 | Test Loss: 0.4461 | Train IoU: 0.5771 | Test IoU: 0.5718 | LR localizer: 0.0005  | LR backbone: 5e-05
* #18. Time: 0:07:10 | Train Loss: 0.4399 | Test Loss: 0.4703 | Train IoU: 0.5795 | Test IoU: 0.5469 | LR localizer: 0.0005  | LR backbone: 5e-05
* #19. Time: 0:07:34 | Train Loss: 0.4301 | Test Loss: 0.4888 | Train IoU: 0.5882 | Test IoU: 0.5263 | LR localizer: 0.0005  | LR backbone: 5e-05
* #20. Time: 0:07:59 | Train Loss: 0.4327 | Test Loss: 0.4716 | Train IoU: 0.5857 | Test IoU: 0.5444 | LR localizer: 0.0005  | LR backbone: 5e-05
* #21. Time: 0:08:22 | Train Loss: 0.4277 | Test Loss: 0.4788 | Train IoU: 0.5908 | Test IoU: 0.5361 | LR localizer: 0.0005  | LR backbone: 5e-05
* #22. Time: 0:08:44 | Train Loss: 0.4094 | Test Loss: 0.4518 | Train IoU: 0.6072 | Test IoU: 0.5627 | LR localizer: 0.00025  | LR backbone: 2.5e-05
* #23. Time: 0:09:07 | Train Loss: 0.4094 | Test Loss: 0.4379 | Train IoU: 0.6077 | Test IoU: 0.5785 | LR localizer: 0.00025  | LR backbone: 2.5e-05
* #24. Time: 0:09:30 | Train Loss: 0.4097 | Test Loss: 0.4476 | Train IoU: 0.6071 | Test IoU: 0.5675 | LR localizer: 0.00025  | LR backbone: 2.5e-05
* #25. Time: 0:09:56 | Train Loss: 0.4114 | Test Loss: 0.4799 | Train IoU: 0.6056 | Test IoU: 0.5386 | LR localizer: 0.00025  | LR backbone: 2.5e-05
* #26. Time: 0:10:22 | Train Loss: 0.4052 | Test Loss: 0.4276 | Train IoU: 0.6118 | Test IoU: 0.5896 | LR localizer: 0.00025  | LR backbone: 2.5e-05
* #27. Time: 0:10:49 | Train Loss: 0.4008 | Test Loss: 0.4240 | Train IoU: 0.6151 | Test IoU: 0.5900 | LR localizer: 0.00025  | LR backbone: 2.5e-05
* #28. Time: 0:11:12 | Train Loss: 0.3985 | Test Loss: 0.4453 | Train IoU: 0.6180 | Test IoU: 0.5714 | LR localizer: 0.00025  | LR backbone: 2.5e-05
* #29. Time: 0:11:35 | Train Loss: 0.4013 | Test Loss: 0.4299 | Train IoU: 0.6149 | Test IoU: 0.5826 | LR localizer: 0.00025  | LR backbone: 2.5e-05
* #30. Time: 0:12:01 | Train Loss: 0.3943 | Test Loss: 0.4366 | Train IoU: 0.6209 | Test IoU: 0.5789 | LR localizer: 0.00025  | LR backbone: 2.5e-05

notes:
unfreezing 3rd block def helped with IoU our lr has reached 0.000125 / 1.25e-05. Top IoU 0.6209/0.5900

# Run #3
## Hyper params

```
    for param in backbone.parameters():
        param.requires_grad = False

    # Unfreeze block 4 only to fine tune params
    for param in backbone.block4.parameters():
        param.requires_grad = True
        
    if epoch == 15:
    # unfreeze block 3
    for param in backbone.block3.parameters():
        param.requires_grad = True

    optimizer.add_param_group(
        {"params": backbone.block3.parameters(), "lr": 1e-5, "weight_decay": 1e-5}
    )
        
    lr = 0.001 / 0.0001 / 0.00001
    epochs = 30
    optimizer = optim.Adam([
        {"params": localizer.parameters(), "lr": 0.001, "weight_decay": 1e-3},
        {"params": backbone.block4.parameters(), "lr": 0.0001, "weight_decay": 1e-4}
    ])
    loss = nn.SmoothL1Loss()
        l1 = loss_func(predicted_bboxes, bboxes)
        d_iou = distance_box_iou_loss(pred_xyxy, true_xyxy, reduction="mean")
        loss = 1.0 * d_iou + 0.3 * l1
    scheduler = optim.lr_scheduler.ReduceLROnPlateau(optimizer, mode='max', factor=0.5, patience=3)
```

updates:
remove v2.RandomCrop(size=(224, 224))

## Augmentation
```
v2.ToDtype(torch.float32, scale=True),
v2.Resize((256, 256)),

v2.RandomHorizontalFlip(p=0.5),
v2.ColorJitter(brightness=0.125, contrast=0.125, saturation=0.1),
v2.RandomGrayscale(0.2),
v2.Normalize(
    mean=[0.479, 0.446, 0.395],
    std=[0.262, 0.257, 0.265]
)
```

## Output

* #1. Time: 0:00:25 | Train Loss: 0.6590 | Test Loss: 0.5644 | Train IoU: 0.3786 | Test IoU: 0.4618 | LR localizer: 0.001  | LR backbone: 0.0001
* #2. Time: 0:00:48 | Train Loss: 0.6031 | Test Loss: 0.6402 | Train IoU: 0.4273 | Test IoU: 0.3907 | LR localizer: 0.001  | LR backbone: 0.0001
* #3. Time: 0:01:11 | Train Loss: 0.5801 | Test Loss: 0.5885 | Train IoU: 0.4487 | Test IoU: 0.4438 | LR localizer: 0.001  | LR backbone: 0.0001
* #4. Time: 0:01:36 | Train Loss: 0.5545 | Test Loss: 0.5110 | Train IoU: 0.4722 | Test IoU: 0.5092 | LR localizer: 0.001  | LR backbone: 0.0001
* #5. Time: 0:02:00 | Train Loss: 0.5266 | Test Loss: 0.5336 | Train IoU: 0.4981 | Test IoU: 0.4910 | LR localizer: 0.001  | LR backbone: 0.0001
* #6. Time: 0:02:25 | Train Loss: 0.5095 | Test Loss: 0.4901 | Train IoU: 0.5136 | Test IoU: 0.5317 | LR localizer: 0.001  | LR backbone: 0.0001
* #7. Time: 0:02:50 | Train Loss: 0.5082 | Test Loss: 0.6386 | Train IoU: 0.5148 | Test IoU: 0.3975 | LR localizer: 0.001  | LR backbone: 0.0001
* #8. Time: 0:03:15 | Train Loss: 0.5243 | Test Loss: 0.4825 | Train IoU: 0.4991 | Test IoU: 0.5404 | LR localizer: 0.001  | LR backbone: 0.0001
* #9. Time: 0:03:39 | Train Loss: 0.5034 | Test Loss: 0.5815 | Train IoU: 0.5191 | Test IoU: 0.4472 | LR localizer: 0.001  | LR backbone: 0.0001
* #10. Time: 0:04:02 | Train Loss: 0.5096 | Test Loss: 0.5164 | Train IoU: 0.5140 | Test IoU: 0.5043 | LR localizer: 0.001  | LR backbone: 0.0001
* #11. Time: 0:04:26 | Train Loss: 0.4824 | Test Loss: 0.4681 | Train IoU: 0.5393 | Test IoU: 0.5533 | LR localizer: 0.001  | LR backbone: 0.0001
* #12. Time: 0:04:49 | Train Loss: 0.4761 | Test Loss: 0.4998 | Train IoU: 0.5447 | Test IoU: 0.5227 | LR localizer: 0.001  | LR backbone: 0.0001
* #13. Time: 0:05:13 | Train Loss: 0.4659 | Test Loss: 0.4609 | Train IoU: 0.5546 | Test IoU: 0.5579 | LR localizer: 0.001  | LR backbone: 0.0001
* #14. Time: 0:05:36 | Train Loss: 0.4606 | Test Loss: 0.4639 | Train IoU: 0.5590 | Test IoU: 0.5543 | LR localizer: 0.001  | LR backbone: 0.0001
* #15. Time: 0:05:59 | Train Loss: 0.4589 | Test Loss: 0.4611 | Train IoU: 0.5601 | Test IoU: 0.5610 | LR localizer: 0.001  | LR backbone: 0.0001
* #16. Time: 0:06:23 | Train Loss: 0.4490 | Test Loss: 0.4425 | Train IoU: 0.5698 | Test IoU: 0.5762 | LR localizer: 0.001  | LR backbone: 0.0001
* #17. Time: 0:06:46 | Train Loss: 0.4462 | Test Loss: 0.4614 | Train IoU: 0.5724 | Test IoU: 0.5585 | LR localizer: 0.001  | LR backbone: 0.0001
* #18. Time: 0:07:09 | Train Loss: 0.4419 | Test Loss: 0.4627 | Train IoU: 0.5763 | Test IoU: 0.5578 | LR localizer: 0.001  | LR backbone: 0.0001
* #19. Time: 0:07:31 | Train Loss: 0.4389 | Test Loss: 0.4474 | Train IoU: 0.5789 | Test IoU: 0.5749 | LR localizer: 0.001  | LR backbone: 0.0001
* #20. Time: 0:07:54 | Train Loss: 0.4261 | Test Loss: 0.4110 | Train IoU: 0.5908 | Test IoU: 0.6077 | LR localizer: 0.001  | LR backbone: 0.0001
* #21. Time: 0:08:17 | Train Loss: 0.4322 | Test Loss: 0.5493 | Train IoU: 0.5852 | Test IoU: 0.4745 | LR localizer: 0.001  | LR backbone: 0.0001
* #22. Time: 0:08:41 | Train Loss: 0.4426 | Test Loss: 0.4854 | Train IoU: 0.5759 | Test IoU: 0.5365 | LR localizer: 0.001  | LR backbone: 0.0001
* #23. Time: 0:09:04 | Train Loss: 0.4320 | Test Loss: 0.4164 | Train IoU: 0.5850 | Test IoU: 0.6037 | LR localizer: 0.001  | LR backbone: 0.0001
* #24. Time: 0:09:26 | Train Loss: 0.4118 | Test Loss: 0.4038 | Train IoU: 0.6038 | Test IoU: 0.6135 | LR localizer: 0.001  | LR backbone: 0.0001
* #25. Time: 0:09:49 | Train Loss: 0.4128 | Test Loss: 0.4174 | Train IoU: 0.6027 | Test IoU: 0.6002 | LR localizer: 0.001  | LR backbone: 0.0001
* #26. Time: 0:10:12 | Train Loss: 0.4057 | Test Loss: 0.4008 | Train IoU: 0.6095 | Test IoU: 0.6162 | LR localizer: 0.001  | LR backbone: 0.0001
* #27. Time: 0:10:35 | Train Loss: 0.3979 | Test Loss: 0.4138 | Train IoU: 0.6163 | Test IoU: 0.6047 | LR localizer: 0.001  | LR backbone: 0.0001
* #28. Time: 0:10:58 | Train Loss: 0.3982 | Test Loss: 0.4007 | Train IoU: 0.6163 | Test IoU: 0.6165 | LR localizer: 0.001  | LR backbone: 0.0001
* #29. Time: 0:11:21 | Train Loss: 0.3888 | Test Loss: 0.4107 | Train IoU: 0.6247 | Test IoU: 0.6078 | LR localizer: 0.001  | LR backbone: 0.0001
* #30. Time: 0:11:44 | Train Loss: 0.3891 | Test Loss: 0.4327 | Train IoU: 0.6243 | Test IoU: 0.5879 | LR localizer: 0.001  | LR backbone: 0.0001

notes:
removing cropping helped with performance model became less generalized lr became static tho. Top IoU 0.6243/0.6165
thoughts:
increase epochs seems model still learning on 30 epoch
try to unfreeze entire model at ~20epoch


# Run #4
## Hyper params

```
    for param in backbone.parameters():
        param.requires_grad = False

    # Unfreeze block 4 only to fine tune params
    for param in backbone.block4.parameters():
        param.requires_grad = True
        
    if epoch == 15:
    # unfreeze block 3
    for param in backbone.block3.parameters():
        param.requires_grad = True

    optimizer.add_param_group(
        {"params": backbone.block3.parameters(), "lr": 1e-5, "weight_decay": 1e-5}
    )
        
    lr = 0.001 / 0.0001 / 0.00001
    epochs = 50
    optimizer = optim.Adam([
        {"params": localizer.parameters(), "lr": 0.001, "weight_decay": 1e-3},
        {"params": backbone.block4.parameters(), "lr": 0.0001, "weight_decay": 1e-4}
    ])
    loss = nn.SmoothL1Loss()
        l1 = loss_func(predicted_bboxes, bboxes)
        d_iou = distance_box_iou_loss(pred_xyxy, true_xyxy, reduction="mean")
        loss = 1.0 * d_iou + 0.5 * l1
    scheduler = optim.lr_scheduler.ReduceLROnPlateau(optimizer, mode='max', factor=0.5, patience=3)
```

updates:
loss = 1.0 * d_iou + 0.3 * l1 > loss = 1.0 * d_iou + 0.5 * l1
epochs = 30 > epochs = 50

## Augmentation
```
v2.ToDtype(torch.float32, scale=True),
v2.Resize((256, 256)),

v2.RandomHorizontalFlip(p=0.5),
v2.ColorJitter(brightness=0.125, contrast=0.125, saturation=0.1),
v2.RandomGrayscale(0.2),
v2.Normalize(
    mean=[0.479, 0.446, 0.395],
    std=[0.262, 0.257, 0.265]
)
```

## Output

#1. Time: 0:00:25 | Train Loss: 0.6638 | Test Loss: 0.7643 | Train IoU: 0.3784 | Test IoU: 0.3001 | LR localizer: 0.001  | LR backbone: 0.0001
#2. Time: 0:00:48 | Train Loss: 0.5984 | Test Loss: 0.5430 | Train IoU: 0.4346 | Test IoU: 0.4812 | LR localizer: 0.001  | LR backbone: 0.0001
#3. Time: 0:01:12 | Train Loss: 0.5554 | Test Loss: 0.5353 | Train IoU: 0.4731 | Test IoU: 0.4910 | LR localizer: 0.001  | LR backbone: 0.0001
#4. Time: 0:01:36 | Train Loss: 0.5329 | Test Loss: 0.5107 | Train IoU: 0.4937 | Test IoU: 0.5142 | LR localizer: 0.001  | LR backbone: 0.0001
#5. Time: 0:02:00 | Train Loss: 0.5104 | Test Loss: 0.4876 | Train IoU: 0.5144 | Test IoU: 0.5367 | LR localizer: 0.001  | LR backbone: 0.0001
#6. Time: 0:02:22 | Train Loss: 0.4944 | Test Loss: 0.4872 | Train IoU: 0.5288 | Test IoU: 0.5351 | LR localizer: 0.001  | LR backbone: 0.0001
#7. Time: 0:02:45 | Train Loss: 0.4954 | Test Loss: 0.5272 | Train IoU: 0.5278 | Test IoU: 0.5010 | LR localizer: 0.001  | LR backbone: 0.0001
#8. Time: 0:03:07 | Train Loss: 0.5031 | Test Loss: 0.6266 | Train IoU: 0.5216 | Test IoU: 0.4103 | LR localizer: 0.001  | LR backbone: 0.0001
#9. Time: 0:03:32 | Train Loss: 0.4931 | Test Loss: 0.4632 | Train IoU: 0.5303 | Test IoU: 0.5584 | LR localizer: 0.001  | LR backbone: 0.0001
#10. Time: 0:03:58 | Train Loss: 0.4765 | Test Loss: 0.4821 | Train IoU: 0.5458 | Test IoU: 0.5430 | LR localizer: 0.001  | LR backbone: 0.0001
#11. Time: 0:04:20 | Train Loss: 0.4667 | Test Loss: 0.4732 | Train IoU: 0.5547 | Test IoU: 0.5483 | LR localizer: 0.001  | LR backbone: 0.0001
#12. Time: 0:04:42 | Train Loss: 0.4651 | Test Loss: 0.4536 | Train IoU: 0.5558 | Test IoU: 0.5688 | LR localizer: 0.001  | LR backbone: 0.0001
#13. Time: 0:05:04 | Train Loss: 0.4525 | Test Loss: 0.4643 | Train IoU: 0.5674 | Test IoU: 0.5574 | LR localizer: 0.001  | LR backbone: 0.0001
#14. Time: 0:05:26 | Train Loss: 0.4507 | Test Loss: 0.5047 | Train IoU: 0.5692 | Test IoU: 0.5212 | LR localizer: 0.001  | LR backbone: 0.0001
#15. Time: 0:05:49 | Train Loss: 0.4441 | Test Loss: 0.4455 | Train IoU: 0.5750 | Test IoU: 0.5765 | LR localizer: 0.001  | LR backbone: 0.0001
#16. Time: 0:06:12 | Train Loss: 0.4418 | Test Loss: 0.4399 | Train IoU: 0.5769 | Test IoU: 0.5810 | LR localizer: 0.001  | LR backbone: 0.0001
#17. Time: 0:06:35 | Train Loss: 0.4344 | Test Loss: 0.4322 | Train IoU: 0.5840 | Test IoU: 0.5880 | LR localizer: 0.001  | LR backbone: 0.0001
#18. Time: 0:06:57 | Train Loss: 0.4321 | Test Loss: 0.4183 | Train IoU: 0.5862 | Test IoU: 0.6017 | LR localizer: 0.001  | LR backbone: 0.0001
#19. Time: 0:07:20 | Train Loss: 0.4283 | Test Loss: 0.4373 | Train IoU: 0.5896 | Test IoU: 0.5840 | LR localizer: 0.001  | LR backbone: 0.0001
#20. Time: 0:07:43 | Train Loss: 0.4251 | Test Loss: 0.4719 | Train IoU: 0.5920 | Test IoU: 0.5512 | LR localizer: 0.001  | LR backbone: 0.0001
#21. Time: 0:08:06 | Train Loss: 0.4285 | Test Loss: 0.4444 | Train IoU: 0.5892 | Test IoU: 0.5750 | LR localizer: 0.001  | LR backbone: 0.0001
#22. Time: 0:08:29 | Train Loss: 0.4144 | Test Loss: 0.4394 | Train IoU: 0.6022 | Test IoU: 0.5803 | LR localizer: 0.001  | LR backbone: 0.0001
#23. Time: 0:08:52 | Train Loss: 0.3962 | Test Loss: 0.3946 | Train IoU: 0.6186 | Test IoU: 0.6241 | LR localizer: 0.0005  | LR backbone: 5e-05
#24. Time: 0:09:14 | Train Loss: 0.3912 | Test Loss: 0.3990 | Train IoU: 0.6235 | Test IoU: 0.6200 | LR localizer: 0.0005  | LR backbone: 5e-05
#25. Time: 0:09:37 | Train Loss: 0.3899 | Test Loss: 0.3981 | Train IoU: 0.6246 | Test IoU: 0.6213 | LR localizer: 0.0005  | LR backbone: 5e-05
#26. Time: 0:10:01 | Train Loss: 0.3825 | Test Loss: 0.3862 | Train IoU: 0.6312 | Test IoU: 0.6324 | LR localizer: 0.0005  | LR backbone: 5e-05
#27. Time: 0:10:24 | Train Loss: 0.3755 | Test Loss: 0.3821 | Train IoU: 0.6378 | Test IoU: 0.6372 | LR localizer: 0.0005  | LR backbone: 5e-05
#28. Time: 0:10:47 | Train Loss: 0.3771 | Test Loss: 0.3866 | Train IoU: 0.6367 | Test IoU: 0.6325 | LR localizer: 0.0005  | LR backbone: 5e-05
#29. Time: 0:11:10 | Train Loss: 0.3674 | Test Loss: 0.3788 | Train IoU: 0.6452 | Test IoU: 0.6403 | LR localizer: 0.0005  | LR backbone: 5e-05
#30. Time: 0:11:33 | Train Loss: 0.3673 | Test Loss: 0.3806 | Train IoU: 0.6455 | Test IoU: 0.6373 | LR localizer: 0.0005  | LR backbone: 5e-05
#31. Time: 0:11:56 | Train Loss: 0.3686 | Test Loss: 0.3990 | Train IoU: 0.6445 | Test IoU: 0.6214 | LR localizer: 0.0005  | LR backbone: 5e-05
#32. Time: 0:12:19 | Train Loss: 0.3649 | Test Loss: 0.4016 | Train IoU: 0.6478 | Test IoU: 0.6186 | LR localizer: 0.0005  | LR backbone: 5e-05
#33. Time: 0:12:41 | Train Loss: 0.3695 | Test Loss: 0.3935 | Train IoU: 0.6435 | Test IoU: 0.6278 | LR localizer: 0.0005  | LR backbone: 5e-05
#34. Time: 0:13:04 | Train Loss: 0.3514 | Test Loss: 0.3730 | Train IoU: 0.6601 | Test IoU: 0.6459 | LR localizer: 0.00025  | LR backbone: 2.5e-05
#35. Time: 0:13:27 | Train Loss: 0.3510 | Test Loss: 0.3697 | Train IoU: 0.6602 | Test IoU: 0.6477 | LR localizer: 0.00025  | LR backbone: 2.5e-05
#36. Time: 0:13:50 | Train Loss: 0.3392 | Test Loss: 0.3610 | Train IoU: 0.6711 | Test IoU: 0.6559 | LR localizer: 0.00025  | LR backbone: 2.5e-05
#37. Time: 0:14:12 | Train Loss: 0.3426 | Test Loss: 0.3743 | Train IoU: 0.6683 | Test IoU: 0.6435 | LR localizer: 0.00025  | LR backbone: 2.5e-05
#38. Time: 0:14:35 | Train Loss: 0.3411 | Test Loss: 0.3706 | Train IoU: 0.6698 | Test IoU: 0.6468 | LR localizer: 0.00025  | LR backbone: 2.5e-05
#39. Time: 0:14:59 | Train Loss: 0.3398 | Test Loss: 0.3686 | Train IoU: 0.6709 | Test IoU: 0.6495 | LR localizer: 0.00025  | LR backbone: 2.5e-05
#40. Time: 0:15:22 | Train Loss: 0.3382 | Test Loss: 0.3660 | Train IoU: 0.6723 | Test IoU: 0.6526 | LR localizer: 0.00025  | LR backbone: 2.5e-05
#41. Time: 0:15:45 | Train Loss: 0.3310 | Test Loss: 0.3586 | Train IoU: 0.6790 | Test IoU: 0.6591 | LR localizer: 0.000125  | LR backbone: 1.25e-05
#42. Time: 0:16:08 | Train Loss: 0.3261 | Test Loss: 0.3705 | Train IoU: 0.6831 | Test IoU: 0.6479 | LR localizer: 0.000125  | LR backbone: 1.25e-05
#43. Time: 0:16:31 | Train Loss: 0.3330 | Test Loss: 0.3586 | Train IoU: 0.6773 | Test IoU: 0.6588 | LR localizer: 0.000125  | LR backbone: 1.25e-05
#44. Time: 0:16:54 | Train Loss: 0.3257 | Test Loss: 0.3539 | Train IoU: 0.6842 | Test IoU: 0.6631 | LR localizer: 0.000125  | LR backbone: 1.25e-05
#45. Time: 0:17:16 | Train Loss: 0.3288 | Test Loss: 0.3581 | Train IoU: 0.6808 | Test IoU: 0.6590 | LR localizer: 0.000125  | LR backbone: 1.25e-05
#46. Time: 0:17:39 | Train Loss: 0.3286 | Test Loss: 0.3660 | Train IoU: 0.6812 | Test IoU: 0.6514 | LR localizer: 0.000125  | LR backbone: 1.25e-05
#47. Time: 0:18:02 | Train Loss: 0.3212 | Test Loss: 0.3652 | Train IoU: 0.6880 | Test IoU: 0.6524 | LR localizer: 0.000125  | LR backbone: 1.25e-05
#48. Time: 0:18:24 | Train Loss: 0.3170 | Test Loss: 0.3644 | Train IoU: 0.6918 | Test IoU: 0.6538 | LR localizer: 0.000125  | LR backbone: 1.25e-05
#49. Time: 0:18:47 | Train Loss: 0.3243 | Test Loss: 0.3559 | Train IoU: 0.6846 | Test IoU: 0.6619 | LR localizer: 6.25e-05  | LR backbone: 6.25e-06
#50. Time: 0:19:10 | Train Loss: 0.3131 | Test Loss: 0.3525 | Train IoU: 0.6958 | Test IoU: 0.6646 | LR localizer: 6.25e-05  | LR backbone: 6.25e-06

notes:
Learned very important thing data aug for classification != data aug localization
reached top IoU in both datasets


# Run #5
## Hyper params

```
    for param in backbone.parameters():
        param.requires_grad = False

    # Unfreeze block 4 only to fine tune params
    for param in backbone.block4.parameters():
        param.requires_grad = True
        
    if epoch == 15:
    # unfreeze block 3
    for param in backbone.block3.parameters():
        param.requires_grad = True

    optimizer.add_param_group(
        {"params": backbone.block3.parameters(), "lr": 1e-5, "weight_decay": 1e-5}
    )
        
    lr = 0.001 / 0.0001 / 0.00001
    epochs = 50
    optimizer = optim.Adam([
        {"params": localizer.parameters(), "lr": 0.001, "weight_decay": 1e-3},
        {"params": backbone.block4.parameters(), "lr": 0.0001, "weight_decay": 1e-4}
    ])
    loss = nn.SmoothL1Loss()
        l1 = loss_func(predicted_bboxes, bboxes)
        d_iou = distance_box_iou_loss(pred_xyxy, true_xyxy, reduction="mean")
        loss = 1.0 * d_iou + 0.5 * l1
    scheduler = optim.lr_scheduler.ReduceLROnPlateau(optimizer, mode='max', factor=0.5, patience=3)
```

updates:
v2.Resize((256, 256)) > v2.Resize((384, 384))


## Augmentation
```
v2.ToDtype(torch.float32, scale=True),
v2.Resize((384, 384)),

v2.RandomHorizontalFlip(p=0.5),
v2.ColorJitter(brightness=0.125, contrast=0.125, saturation=0.1),
v2.RandomGrayscale(0.2),
v2.Normalize(
    mean=[0.479, 0.446, 0.395],
    std=[0.262, 0.257, 0.265]
)
```

## Output
#1. Time: 0:00:30 | Train Loss: 0.6553 | Test Loss: 0.5826 | Train IoU: 0.3850 | Test IoU: 0.4460 | LR localizer: 0.001  | LR backbone: 0.0001
#2. Time: 0:01:00 | Train Loss: 0.5833 | Test Loss: 0.5168 | Train IoU: 0.4469 | Test IoU: 0.5064 | LR localizer: 0.001  | LR backbone: 0.0001
#3. Time: 0:01:30 | Train Loss: 0.5473 | Test Loss: 0.5551 | Train IoU: 0.4799 | Test IoU: 0.4750 | LR localizer: 0.001  | LR backbone: 0.0001
#4. Time: 0:02:00 | Train Loss: 0.5269 | Test Loss: 0.4976 | Train IoU: 0.4987 | Test IoU: 0.5246 | LR localizer: 0.001  | LR backbone: 0.0001
#5. Time: 0:02:30 | Train Loss: 0.5124 | Test Loss: 0.5138 | Train IoU: 0.5120 | Test IoU: 0.5108 | LR localizer: 0.001  | LR backbone: 0.0001
#6. Time: 0:02:59 | Train Loss: 0.4986 | Test Loss: 0.5072 | Train IoU: 0.5250 | Test IoU: 0.5160 | LR localizer: 0.001  | LR backbone: 0.0001
#7. Time: 0:03:29 | Train Loss: 0.4918 | Test Loss: 0.5223 | Train IoU: 0.5315 | Test IoU: 0.5039 | LR localizer: 0.001  | LR backbone: 0.0001
#8. Time: 0:04:00 | Train Loss: 0.4781 | Test Loss: 0.4507 | Train IoU: 0.5439 | Test IoU: 0.5683 | LR localizer: 0.001  | LR backbone: 0.0001
#9. Time: 0:04:30 | Train Loss: 0.4654 | Test Loss: 0.5676 | Train IoU: 0.5560 | Test IoU: 0.4613 | LR localizer: 0.001  | LR backbone: 0.0001
#10. Time: 0:05:00 | Train Loss: 0.4648 | Test Loss: 0.5009 | Train IoU: 0.5566 | Test IoU: 0.5213 | LR localizer: 0.001  | LR backbone: 0.0001
#11. Time: 0:05:30 | Train Loss: 0.4548 | Test Loss: 0.4435 | Train IoU: 0.5651 | Test IoU: 0.5759 | LR localizer: 0.001  | LR backbone: 0.0001
#12. Time: 0:06:00 | Train Loss: 0.4529 | Test Loss: 0.4509 | Train IoU: 0.5670 | Test IoU: 0.5703 | LR localizer: 0.001  | LR backbone: 0.0001
#13. Time: 0:06:30 | Train Loss: 0.4497 | Test Loss: 0.4461 | Train IoU: 0.5700 | Test IoU: 0.5739 | LR localizer: 0.001  | LR backbone: 0.0001
#14. Time: 0:07:00 | Train Loss: 0.4414 | Test Loss: 0.4298 | Train IoU: 0.5776 | Test IoU: 0.5923 | LR localizer: 0.001  | LR backbone: 0.0001
#15. Time: 0:07:29 | Train Loss: 0.4315 | Test Loss: 0.4390 | Train IoU: 0.5867 | Test IoU: 0.5793 | LR localizer: 0.001  | LR backbone: 0.0001
#16. Time: 0:08:02 | Train Loss: 0.4401 | Test Loss: 0.5063 | Train IoU: 0.5794 | Test IoU: 0.5166 | LR localizer: 0.001  | LR backbone: 0.0001
#17. Time: 0:08:35 | Train Loss: 0.4488 | Test Loss: 0.5451 | Train IoU: 0.5712 | Test IoU: 0.4840 | LR localizer: 0.001  | LR backbone: 0.0001
#18. Time: 0:09:08 | Train Loss: 0.4322 | Test Loss: 0.4179 | Train IoU: 0.5863 | Test IoU: 0.5999 | LR localizer: 0.001  | LR backbone: 0.0001
#19. Time: 0:09:41 | Train Loss: 0.4102 | Test Loss: 0.4030 | Train IoU: 0.6065 | Test IoU: 0.6138 | LR localizer: 0.001  | LR backbone: 0.0001
#20. Time: 0:10:15 | Train Loss: 0.4228 | Test Loss: 0.4634 | Train IoU: 0.5951 | Test IoU: 0.5597 | LR localizer: 0.001  | LR backbone: 0.0001
#21. Time: 0:10:48 | Train Loss: 0.4210 | Test Loss: 0.3984 | Train IoU: 0.5964 | Test IoU: 0.6194 | LR localizer: 0.001  | LR backbone: 0.0001
#22. Time: 0:11:22 | Train Loss: 0.4022 | Test Loss: 0.4014 | Train IoU: 0.6140 | Test IoU: 0.6156 | LR localizer: 0.001  | LR backbone: 0.0001
#23. Time: 0:11:55 | Train Loss: 0.3967 | Test Loss: 0.3804 | Train IoU: 0.6189 | Test IoU: 0.6360 | LR localizer: 0.001  | LR backbone: 0.0001
#24. Time: 0:12:28 | Train Loss: 0.3946 | Test Loss: 0.3895 | Train IoU: 0.6208 | Test IoU: 0.6275 | LR localizer: 0.001  | LR backbone: 0.0001
#25. Time: 0:13:01 | Train Loss: 0.3905 | Test Loss: 0.3999 | Train IoU: 0.6240 | Test IoU: 0.6182 | LR localizer: 0.001  | LR backbone: 0.0001
#26. Time: 0:13:35 | Train Loss: 0.3910 | Test Loss: 0.3760 | Train IoU: 0.6243 | Test IoU: 0.6402 | LR localizer: 0.001  | LR backbone: 0.0001
#27. Time: 0:14:08 | Train Loss: 0.3839 | Test Loss: 0.3912 | Train IoU: 0.6307 | Test IoU: 0.6272 | LR localizer: 0.001  | LR backbone: 0.0001
#28. Time: 0:14:41 | Train Loss: 0.3900 | Test Loss: 0.3816 | Train IoU: 0.6248 | Test IoU: 0.6354 | LR localizer: 0.001  | LR backbone: 0.0001
#29. Time: 0:15:14 | Train Loss: 0.3811 | Test Loss: 0.3983 | Train IoU: 0.6332 | Test IoU: 0.6178 | LR localizer: 0.001  | LR backbone: 0.0001
#30. Time: 0:15:47 | Train Loss: 0.3761 | Test Loss: 0.3976 | Train IoU: 0.6376 | Test IoU: 0.6203 | LR localizer: 0.001  | LR backbone: 0.0001
#31. Time: 0:16:22 | Train Loss: 0.3649 | Test Loss: 0.3688 | Train IoU: 0.6482 | Test IoU: 0.6456 | LR localizer: 0.0005  | LR backbone: 5e-05
#32. Time: 0:16:56 | Train Loss: 0.3563 | Test Loss: 0.3482 | Train IoU: 0.6559 | Test IoU: 0.6663 | LR localizer: 0.0005  | LR backbone: 5e-05
#33. Time: 0:17:29 | Train Loss: 0.3538 | Test Loss: 0.3679 | Train IoU: 0.6579 | Test IoU: 0.6491 | LR localizer: 0.0005  | LR backbone: 5e-05
#34. Time: 0:18:01 | Train Loss: 0.3516 | Test Loss: 0.3576 | Train IoU: 0.6605 | Test IoU: 0.6572 | LR localizer: 0.0005  | LR backbone: 5e-05
#35. Time: 0:18:34 | Train Loss: 0.3434 | Test Loss: 0.3508 | Train IoU: 0.6676 | Test IoU: 0.6645 | LR localizer: 0.0005  | LR backbone: 5e-05
#36. Time: 0:19:05 | Train Loss: 0.3520 | Test Loss: 0.3448 | Train IoU: 0.6594 | Test IoU: 0.6703 | LR localizer: 0.0005  | LR backbone: 5e-05
#37. Time: 0:19:37 | Train Loss: 0.3445 | Test Loss: 0.3571 | Train IoU: 0.6668 | Test IoU: 0.6584 | LR localizer: 0.0005  | LR backbone: 5e-05
#38. Time: 0:20:08 | Train Loss: 0.3439 | Test Loss: 0.3687 | Train IoU: 0.6672 | Test IoU: 0.6474 | LR localizer: 0.0005  | LR backbone: 5e-05
#39. Time: 0:20:40 | Train Loss: 0.3427 | Test Loss: 0.3640 | Train IoU: 0.6685 | Test IoU: 0.6525 | LR localizer: 0.0005  | LR backbone: 5e-05
#40. Time: 0:21:11 | Train Loss: 0.3446 | Test Loss: 0.3525 | Train IoU: 0.6666 | Test IoU: 0.6623 | LR localizer: 0.0005  | LR backbone: 5e-05
#41. Time: 0:21:43 | Train Loss: 0.3339 | Test Loss: 0.3410 | Train IoU: 0.6768 | Test IoU: 0.6726 | LR localizer: 0.00025  | LR backbone: 2.5e-05
#42. Time: 0:22:16 | Train Loss: 0.3246 | Test Loss: 0.3355 | Train IoU: 0.6848 | Test IoU: 0.6789 | LR localizer: 0.00025  | LR backbone: 2.5e-05
#43. Time: 0:22:48 | Train Loss: 0.3282 | Test Loss: 0.3353 | Train IoU: 0.6817 | Test IoU: 0.6795 | LR localizer: 0.00025  | LR backbone: 2.5e-05
#44. Time: 0:23:21 | Train Loss: 0.3244 | Test Loss: 0.3415 | Train IoU: 0.6856 | Test IoU: 0.6735 | LR localizer: 0.00025  | LR backbone: 2.5e-05
#45. Time: 0:23:52 | Train Loss: 0.3198 | Test Loss: 0.3374 | Train IoU: 0.6902 | Test IoU: 0.6781 | LR localizer: 0.00025  | LR backbone: 2.5e-05
#46. Time: 0:24:25 | Train Loss: 0.3235 | Test Loss: 0.3303 | Train IoU: 0.6862 | Test IoU: 0.6844 | LR localizer: 0.00025  | LR backbone: 2.5e-05
#47. Time: 0:24:56 | Train Loss: 0.3172 | Test Loss: 0.3343 | Train IoU: 0.6920 | Test IoU: 0.6804 | LR localizer: 0.00025  | LR backbone: 2.5e-05
#48. Time: 0:25:28 | Train Loss: 0.3181 | Test Loss: 0.3306 | Train IoU: 0.6912 | Test IoU: 0.6837 | LR localizer: 0.00025  | LR backbone: 2.5e-05
#49. Time: 0:26:00 | Train Loss: 0.3127 | Test Loss: 0.3278 | Train IoU: 0.6965 | Test IoU: 0.6868 | LR localizer: 0.00025  | LR backbone: 2.5e-05
#50. Time: 0:26:31 | Train Loss: 0.3092 | Test Loss: 0.3338 | Train IoU: 0.6995 | Test IoU: 0.6807 | LR localizer: 0.00025  | LR backbone: 2.5e-05

notes:
by changing size of an image to 384, 384 and simply giving more info to my model 
pushed iou close to 0.685 on test dataset and 0.70 on train

realized that we do not need to shrink an image the way we do in classification because cuts down data that is very important
for localization

if resolution matters a lot then make sense to change pooling layer in my compressor in Localizer
nn.AdaptiveAvgPool2d((7, 7)) > to 10,10 maybe or 12,12


# Run #6
## Hyper params

```
    for param in backbone.parameters():
        param.requires_grad = False

    # Unfreeze block 4 only to fine tune params
    for param in backbone.block4.parameters():
        param.requires_grad = True
        
    if epoch == 15:
        # unfreeze block 3 at 15th epoch
        for param in backbone.block3.parameters():
            param.requires_grad = True

    optimizer.add_param_group(
        {"params": backbone.block3.parameters(), "lr": 1e-5, "weight_decay": 1e-5}
    )
        
    lr = 0.001 / 0.0001 / 0.00001
    epochs = 50
    optimizer = optim.Adam([
        {"params": localizer.parameters(), "lr": 0.001, "weight_decay": 1e-3},
        {"params": backbone.block4.parameters(), "lr": 0.0001, "weight_decay": 1e-4}
    ])
    loss = nn.SmoothL1Loss()
        l1 = loss_func(predicted_bboxes, bboxes)
        d_iou = distance_box_iou_loss(pred_xyxy, true_xyxy, reduction="mean")
        loss = 1.0 * d_iou + 0.5 * l1
    scheduler = optim.lr_scheduler.ReduceLROnPlateau(optimizer, mode='max', factor=0.5, patience=3)
```

updates:
nn.AdaptiveAvgPool2d((10, 10))
self.fc = nn.Sequential(
            nn.Linear(64 * 10 * 10, 512),
            nn.BatchNorm1d(512),
            nn.ReLU(inplace=True),
            nn.Dropout(0.3),
            nn.Linear(512, 4),
            nn.Sigmoid()
        )

if epoch == 20:
    # unfreeze the rest of the model
    for param in backbone.block2.parameters():
        param.requires_grad = True
    for param in backbone.block1.parameters():
        param.requires_grad = True
    for param in backbone.conv.parameters():
        param.requires_grad = True

    optimizer.add_param_group(
        {"params": backbone.block2.parameters(), "lr": 1e-6, "weight_decay": 1e-6},
    )
    optimizer.add_param_group(
        {"params": backbone.block1.parameters(), "lr": 1e-6, "weight_decay": 1e-6},
    )
    optimizer.add_param_group(
        {"params": backbone.conv.parameters(), "lr": 1e-6, "weight_decay": 1e-6},
    )


## Augmentation
```
v2.ToDtype(torch.float32, scale=True),
v2.Resize((384, 384)),

v2.RandomHorizontalFlip(p=0.5),
v2.ColorJitter(brightness=0.125, contrast=0.125, saturation=0.1),
v2.RandomGrayscale(0.2),
v2.Normalize(
    mean=[0.479, 0.446, 0.395],
    std=[0.262, 0.257, 0.265]
)
```

## Output

* #1. Time: 0:00:31 | Train Loss: 0.6777 | Test Loss: 0.5829 | Train IoU: 0.3664 | Test IoU: 0.4464 | LR localizer: 0.001  | LR backbone: 0.0001
* #2. Time: 0:01:02 | Train Loss: 0.5950 | Test Loss: 0.5691 | Train IoU: 0.4366 | Test IoU: 0.4602 | LR localizer: 0.001  | LR backbone: 0.0001
* #3. Time: 0:01:33 | Train Loss: 0.5601 | Test Loss: 0.5208 | Train IoU: 0.4679 | Test IoU: 0.5045 | LR localizer: 0.001  | LR backbone: 0.0001
* #4. Time: 0:02:06 | Train Loss: 0.5411 | Test Loss: 0.5212 | Train IoU: 0.4862 | Test IoU: 0.5051 | LR localizer: 0.001  | LR backbone: 0.0001
* #5. Time: 0:02:38 | Train Loss: 0.5204 | Test Loss: 0.4988 | Train IoU: 0.5047 | Test IoU: 0.5258 | LR localizer: 0.001  | LR backbone: 0.0001
* #6. Time: 0:03:12 | Train Loss: 0.5115 | Test Loss: 0.4942 | Train IoU: 0.5132 | Test IoU: 0.5296 | LR localizer: 0.001  | LR backbone: 0.0001
* #7. Time: 0:03:44 | Train Loss: 0.4975 | Test Loss: 0.4919 | Train IoU: 0.5265 | Test IoU: 0.5297 | LR localizer: 0.001  | LR backbone: 0.0001
* #8. Time: 0:04:18 | Train Loss: 0.4894 | Test Loss: 0.4894 | Train IoU: 0.5340 | Test IoU: 0.5297 | LR localizer: 0.001  | LR backbone: 0.0001
* #9. Time: 0:04:48 | Train Loss: 0.4727 | Test Loss: 0.4795 | Train IoU: 0.5492 | Test IoU: 0.5431 | LR localizer: 0.001  | LR backbone: 0.0001
* #10. Time: 0:05:19 | Train Loss: 0.4730 | Test Loss: 0.5012 | Train IoU: 0.5488 | Test IoU: 0.5216 | LR localizer: 0.001  | LR backbone: 0.0001
* #11. Time: 0:05:50 | Train Loss: 0.4677 | Test Loss: 0.4528 | Train IoU: 0.5540 | Test IoU: 0.5685 | LR localizer: 0.001  | LR backbone: 0.0001
* #12. Time: 0:06:23 | Train Loss: 0.4542 | Test Loss: 0.4692 | Train IoU: 0.5660 | Test IoU: 0.5532 | LR localizer: 0.001  | LR backbone: 0.0001
* #13. Time: 0:06:56 | Train Loss: 0.4534 | Test Loss: 0.4691 | Train IoU: 0.5671 | Test IoU: 0.5544 | LR localizer: 0.001  | LR backbone: 0.0001
* #14. Time: 0:07:27 | Train Loss: 0.4474 | Test Loss: 0.5626 | Train IoU: 0.5727 | Test IoU: 0.4572 | LR localizer: 0.001  | LR backbone: 0.0001
* #15. Time: 0:07:58 | Train Loss: 0.4447 | Test Loss: 0.4723 | Train IoU: 0.5750 | Test IoU: 0.5486 | LR localizer: 0.001  | LR backbone: 0.0001
* #16. Time: 0:08:33 | Train Loss: 0.4193 | Test Loss: 0.4066 | Train IoU: 0.5979 | Test IoU: 0.6110 | LR localizer: 0.0005  | LR backbone: 5e-05
* #17. Time: 0:09:08 | Train Loss: 0.4121 | Test Loss: 0.3897 | Train IoU: 0.6047 | Test IoU: 0.6288 | LR localizer: 0.0005  | LR backbone: 5e-05
* #18. Time: 0:09:41 | Train Loss: 0.4157 | Test Loss: 0.4854 | Train IoU: 0.6015 | Test IoU: 0.5412 | LR localizer: 0.0005  | LR backbone: 5e-05
* #19. Time: 0:10:16 | Train Loss: 0.4119 | Test Loss: 0.3883 | Train IoU: 0.6056 | Test IoU: 0.6290 | LR localizer: 0.0005  | LR backbone: 5e-05
* #20. Time: 0:10:51 | Train Loss: 0.3951 | Test Loss: 0.3976 | Train IoU: 0.6201 | Test IoU: 0.6196 | LR localizer: 0.0005  | LR backbone: 5e-05
* #21. Time: 0:11:39 | Train Loss: 0.3908 | Test Loss: 0.4018 | Train IoU: 0.6240 | Test IoU: 0.6150 | LR localizer: 0.0005  | LR backbone: 5e-05
* #22. Time: 0:12:27 | Train Loss: 0.3904 | Test Loss: 0.4160 | Train IoU: 0.6249 | Test IoU: 0.6021 | LR localizer: 0.0005  | LR backbone: 5e-05
* #23. Time: 0:13:14 | Train Loss: 0.3867 | Test Loss: 0.4053 | Train IoU: 0.6277 | Test IoU: 0.6125 | LR localizer: 0.0005  | LR backbone: 5e-05
* #24. Time: 0:14:01 | Train Loss: 0.3763 | Test Loss: 0.3710 | Train IoU: 0.6374 | Test IoU: 0.6447 | LR localizer: 0.00025  | LR backbone: 2.5e-05
* #25. Time: 0:14:48 | Train Loss: 0.3619 | Test Loss: 0.3749 | Train IoU: 0.6506 | Test IoU: 0.6421 | LR localizer: 0.00025  | LR backbone: 2.5e-05
* #26. Time: 0:15:35 | Train Loss: 0.3588 | Test Loss: 0.3620 | Train IoU: 0.6534 | Test IoU: 0.6539 | LR localizer: 0.00025  | LR backbone: 2.5e-05
* #27. Time: 0:16:23 | Train Loss: 0.3544 | Test Loss: 0.3628 | Train IoU: 0.6578 | Test IoU: 0.6526 | LR localizer: 0.00025  | LR backbone: 2.5e-05
* #28. Time: 0:17:12 | Train Loss: 0.3547 | Test Loss: 0.3566 | Train IoU: 0.6573 | Test IoU: 0.6591 | LR localizer: 0.00025  | LR backbone: 2.5e-05
* #29. Time: 0:18:00 | Train Loss: 0.3584 | Test Loss: 0.3611 | Train IoU: 0.6538 | Test IoU: 0.6542 | LR localizer: 0.00025  | LR backbone: 2.5e-05
* #30. Time: 0:18:48 | Train Loss: 0.3542 | Test Loss: 0.3479 | Train IoU: 0.6579 | Test IoU: 0.6674 | LR localizer: 0.00025  | LR backbone: 2.5e-05
* #31. Time: 0:19:36 | Train Loss: 0.3486 | Test Loss: 0.3514 | Train IoU: 0.6629 | Test IoU: 0.6643 | LR localizer: 0.00025  | LR backbone: 2.5e-05
* #32. Time: 0:20:24 | Train Loss: 0.3479 | Test Loss: 0.3614 | Train IoU: 0.6641 | Test IoU: 0.6553 | LR localizer: 0.00025  | LR backbone: 2.5e-05
* #33. Time: 0:21:13 | Train Loss: 0.3413 | Test Loss: 0.3602 | Train IoU: 0.6698 | Test IoU: 0.6563 | LR localizer: 0.00025  | LR backbone: 2.5e-05
* #34. Time: 0:22:00 | Train Loss: 0.3440 | Test Loss: 0.3562 | Train IoU: 0.6671 | Test IoU: 0.6589 | LR localizer: 0.00025  | LR backbone: 2.5e-05
* #35. Time: 0:22:48 | Train Loss: 0.3310 | Test Loss: 0.3456 | Train IoU: 0.6794 | Test IoU: 0.6691 | LR localizer: 0.000125  | LR backbone: 1.25e-05
* #36. Time: 0:23:38 | Train Loss: 0.3248 | Test Loss: 0.3483 | Train IoU: 0.6854 | Test IoU: 0.6661 | LR localizer: 0.000125  | LR backbone: 1.25e-05
* #37. Time: 0:24:28 | Train Loss: 0.3301 | Test Loss: 0.3446 | Train IoU: 0.6804 | Test IoU: 0.6705 | LR localizer: 0.000125  | LR backbone: 1.25e-05
* #38. Time: 0:25:16 | Train Loss: 0.3254 | Test Loss: 0.3372 | Train IoU: 0.6845 | Test IoU: 0.6783 | LR localizer: 0.000125  | LR backbone: 1.25e-05
* #39. Time: 0:26:05 | Train Loss: 0.3267 | Test Loss: 0.3376 | Train IoU: 0.6834 | Test IoU: 0.6781 | LR localizer: 0.000125  | LR backbone: 1.25e-05
* #40. Time: 0:26:53 | Train Loss: 0.3245 | Test Loss: 0.3345 | Train IoU: 0.6856 | Test IoU: 0.6804 | LR localizer: 0.000125  | LR backbone: 1.25e-05
* #41. Time: 0:27:42 | Train Loss: 0.3223 | Test Loss: 0.3441 | Train IoU: 0.6879 | Test IoU: 0.6716 | LR localizer: 0.000125  | LR backbone: 1.25e-05
* #42. Time: 0:28:32 | Train Loss: 0.3186 | Test Loss: 0.3334 | Train IoU: 0.6912 | Test IoU: 0.6814 | LR localizer: 0.000125  | LR backbone: 1.25e-05
* #43. Time: 0:29:21 | Train Loss: 0.3175 | Test Loss: 0.3303 | Train IoU: 0.6920 | Test IoU: 0.6847 | LR localizer: 0.000125  | LR backbone: 1.25e-05
* #44. Time: 0:30:10 | Train Loss: 0.3145 | Test Loss: 0.3385 | Train IoU: 0.6942 | Test IoU: 0.6754 | LR localizer: 0.000125  | LR backbone: 1.25e-05
* #45. Time: 0:30:59 | Train Loss: 0.3096 | Test Loss: 0.3342 | Train IoU: 0.6997 | Test IoU: 0.6803 | LR localizer: 0.000125  | LR backbone: 1.25e-05
* #46. Time: 0:31:47 | Train Loss: 0.3082 | Test Loss: 0.3378 | Train IoU: 0.7004 | Test IoU: 0.6772 | LR localizer: 0.000125  | LR backbone: 1.25e-05
* #47. Time: 0:32:37 | Train Loss: 0.3141 | Test Loss: 0.3322 | Train IoU: 0.6948 | Test IoU: 0.6828 | LR localizer: 0.000125  | LR backbone: 1.25e-05
* #48. Time: 0:33:26 | Train Loss: 0.3084 | Test Loss: 0.3277 | Train IoU: 0.7007 | Test IoU: 0.6875 | LR localizer: 6.25e-05  | LR backbone: 6.25e-06
* #49. Time: 0:34:15 | Train Loss: 0.3122 | Test Loss: 0.3350 | Train IoU: 0.6973 | Test IoU: 0.6801 | LR localizer: 6.25e-05  | LR backbone: 6.25e-06
* #50. Time: 0:35:04 | Train Loss: 0.3094 | Test Loss: 0.3317 | Train IoU: 0.6999 | Test IoU: 0.6828 | LR localizer: 6.25e-05  | LR backbone: 6.25e-06

notes:
model significantly more stable, learning very steadily also reached highest IoU on train dataset 0.7007
lr drops multiple times during training but i think drops too much then it's too small to learn something from it


# Run #7 - graph.png
## Hyper params

```
    lr = 1e-04 / 1e-04
    epochs = 50
    loss = ops.complete_box_iou_loss(true_xyxy, pred_xyxy).mean()
    optimizer = optim.AdamW([
        {"params": localizer.parameters(), "lr": 1e-04, "weight_decay": 1e-03},
        {"params": backbone.block4.parameters(), "lr": 1e-04, "weight_decay": 1e-03}
    ])
    scheduler = optim.lr_scheduler.MultiStepLR(optimizer, milestones=[15, 25, 35, 45], gamma=0.5) - New
```


## Augmentation
```
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
```

## Output

* #1 Time: 0:00:39 | Train Loss: 0.5622 | Test Loss: 0.4907 | Train CIoU: 0.4378 | Test CIoU: 0.5093 | LR-loc: 0.0001 | LR-bck: 0.0001
* #2 Time: 0:01:16 | Train Loss: 0.4851 | Test Loss: 0.4652 | Train CIoU: 0.5149 | Test CIoU: 0.5348 | LR-loc: 0.0001 | LR-bck: 0.0001
* #3 Time: 0:01:53 | Train Loss: 0.4558 | Test Loss: 0.5080 | Train CIoU: 0.5442 | Test CIoU: 0.4920 | LR-loc: 0.0001 | LR-bck: 0.0001
* #4 Time: 0:02:31 | Train Loss: 0.4311 | Test Loss: 0.4052 | Train CIoU: 0.5689 | Test CIoU: 0.5948 | LR-loc: 0.0001 | LR-bck: 0.0001
* #5 Time: 0:03:09 | Train Loss: 0.4091 | Test Loss: 0.3857 | Train CIoU: 0.5909 | Test CIoU: 0.6143 | LR-loc: 0.0001 | LR-bck: 0.0001
* #6 Time: 0:03:46 | Train Loss: 0.3935 | Test Loss: 0.3755 | Train CIoU: 0.6065 | Test CIoU: 0.6245 | LR-loc: 0.0001 | LR-bck: 0.0001
* #7 Time: 0:04:25 | Train Loss: 0.3825 | Test Loss: 0.4217 | Train CIoU: 0.6175 | Test CIoU: 0.5783 | LR-loc: 0.0001 | LR-bck: 0.0001
* #8 Time: 0:05:02 | Train Loss: 0.3720 | Test Loss: 0.3699 | Train CIoU: 0.6280 | Test CIoU: 0.6301 | LR-loc: 0.0001 | LR-bck: 0.0001
* #9 Time: 0:05:39 | Train Loss: 0.3614 | Test Loss: 0.3658 | Train CIoU: 0.6386 | Test CIoU: 0.6342 | LR-loc: 0.0001 | LR-bck: 0.0001
* #10 Time: 0:06:16 | Train Loss: 0.3518 | Test Loss: 0.3513 | Train CIoU: 0.6482 | Test CIoU: 0.6487 | LR-loc: 0.0001 | LR-bck: 0.0001
* #11 Time: 0:06:54 | Train Loss: 0.3461 | Test Loss: 0.3696 | Train CIoU: 0.6539 | Test CIoU: 0.6304 | LR-loc: 0.0001 | LR-bck: 0.0001
* #12 Time: 0:07:32 | Train Loss: 0.3386 | Test Loss: 0.3486 | Train CIoU: 0.6614 | Test CIoU: 0.6514 | LR-loc: 0.0001 | LR-bck: 0.0001
* #13 Time: 0:08:10 | Train Loss: 0.3283 | Test Loss: 0.3370 | Train CIoU: 0.6717 | Test CIoU: 0.6630 | LR-loc: 0.0001 | LR-bck: 0.0001
* #14 Time: 0:08:47 | Train Loss: 0.3271 | Test Loss: 0.3645 | Train CIoU: 0.6729 | Test CIoU: 0.6355 | LR-loc: 0.0001 | LR-bck: 0.0001
* #15 Time: 0:09:25 | Train Loss: 0.3185 | Test Loss: 0.3666 | Train CIoU: 0.6815 | Test CIoU: 0.6334 | LR-loc: 0.0001 | LR-bck: 0.0001
* #16 Time: 0:10:06 | Train Loss: 0.3016 | Test Loss: 0.3430 | Train CIoU: 0.6984 | Test CIoU: 0.6570 | LR-loc: 5e-05 | LR-bck: 5e-05
* #17 Time: 0:10:47 | Train Loss: 0.2902 | Test Loss: 0.3128 | Train CIoU: 0.7098 | Test CIoU: 0.6872 | LR-loc: 5e-05 | LR-bck: 5e-05
* #18 Time: 0:11:28 | Train Loss: 0.2862 | Test Loss: 0.3112 | Train CIoU: 0.7138 | Test CIoU: 0.6888 | LR-loc: 5e-05 | LR-bck: 5e-05
* #19 Time: 0:12:08 | Train Loss: 0.2746 | Test Loss: 0.3161 | Train CIoU: 0.7254 | Test CIoU: 0.6839 | LR-loc: 5e-05 | LR-bck: 5e-05
* #20 Time: 0:12:48 | Train Loss: 0.2681 | Test Loss: 0.3222 | Train CIoU: 0.7319 | Test CIoU: 0.6778 | LR-loc: 5e-05 | LR-bck: 5e-05
* #21 Time: 0:13:47 | Train Loss: 0.2730 | Test Loss: 0.3052 | Train CIoU: 0.7270 | Test CIoU: 0.6948 | LR-loc: 5e-05 | LR-bck: 5e-05
* #22 Time: 0:14:46 | Train Loss: 0.2652 | Test Loss: 0.3230 | Train CIoU: 0.7348 | Test CIoU: 0.6770 | LR-loc: 5e-05 | LR-bck: 5e-05
* #23 Time: 0:15:44 | Train Loss: 0.2566 | Test Loss: 0.2884 | Train CIoU: 0.7434 | Test CIoU: 0.7116 | LR-loc: 5e-05 | LR-bck: 5e-05
* #24 Time: 0:16:43 | Train Loss: 0.2503 | Test Loss: 0.3061 | Train CIoU: 0.7497 | Test CIoU: 0.6939 | LR-loc: 5e-05 | LR-bck: 5e-05
* #25 Time: 0:17:42 | Train Loss: 0.2486 | Test Loss: 0.2950 | Train CIoU: 0.7514 | Test CIoU: 0.7050 | LR-loc: 5e-05 | LR-bck: 5e-05
* #26 Time: 0:18:41 | Train Loss: 0.2273 | Test Loss: 0.2748 | Train CIoU: 0.7727 | Test CIoU: 0.7252 | LR-loc: 2.5e-05 | LR-bck: 2.5e-05
* #27 Time: 0:19:40 | Train Loss: 0.2196 | Test Loss: 0.2800 | Train CIoU: 0.7804 | Test CIoU: 0.7200 | LR-loc: 2.5e-05 | LR-bck: 2.5e-05
* #28 Time: 0:20:39 | Train Loss: 0.2141 | Test Loss: 0.2718 | Train CIoU: 0.7859 | Test CIoU: 0.7282 | LR-loc: 2.5e-05 | LR-bck: 2.5e-05
* #29 Time: 0:21:39 | Train Loss: 0.2098 | Test Loss: 0.2708 | Train CIoU: 0.7902 | Test CIoU: 0.7292 | LR-loc: 2.5e-05 | LR-bck: 2.5e-05
* #30 Time: 0:22:39 | Train Loss: 0.2068 | Test Loss: 0.2883 | Train CIoU: 0.7932 | Test CIoU: 0.7117 | LR-loc: 2.5e-05 | LR-bck: 2.5e-05
* #31 Time: 0:23:40 | Train Loss: 0.2056 | Test Loss: 0.2648 | Train CIoU: 0.7944 | Test CIoU: 0.7352 | LR-loc: 2.5e-05 | LR-bck: 2.5e-05
* #32 Time: 0:24:41 | Train Loss: 0.2001 | Test Loss: 0.2733 | Train CIoU: 0.7999 | Test CIoU: 0.7267 | LR-loc: 2.5e-05 | LR-bck: 2.5e-05
* #33 Time: 0:25:41 | Train Loss: 0.1953 | Test Loss: 0.2677 | Train CIoU: 0.8047 | Test CIoU: 0.7323 | LR-loc: 2.5e-05 | LR-bck: 2.5e-05
* #34 Time: 0:26:43 | Train Loss: 0.1921 | Test Loss: 0.2632 | Train CIoU: 0.8079 | Test CIoU: 0.7368 | LR-loc: 2.5e-05 | LR-bck: 2.5e-05
* #35 Time: 0:27:43 | Train Loss: 0.1929 | Test Loss: 0.2688 | Train CIoU: 0.8071 | Test CIoU: 0.7312 | LR-loc: 2.5e-05 | LR-bck: 2.5e-05
* #36 Time: 0:28:42 | Train Loss: 0.1816 | Test Loss: 0.2584 | Train CIoU: 0.8184 | Test CIoU: 0.7416 | LR-loc: 1.25e-05 | LR-bck: 1.25e-05
* #37 Time: 0:29:41 | Train Loss: 0.1773 | Test Loss: 0.2598 | Train CIoU: 0.8227 | Test CIoU: 0.7402 | LR-loc: 1.25e-05 | LR-bck: 1.25e-05
* #38 Time: 0:30:41 | Train Loss: 0.1751 | Test Loss: 0.2659 | Train CIoU: 0.8249 | Test CIoU: 0.7341 | LR-loc: 1.25e-05 | LR-bck: 1.25e-05
* #39 Time: 0:31:42 | Train Loss: 0.1715 | Test Loss: 0.2570 | Train CIoU: 0.8285 | Test CIoU: 0.7430 | LR-loc: 1.25e-05 | LR-bck: 1.25e-05
* #40 Time: 0:32:43 | Train Loss: 0.1710 | Test Loss: 0.2549 | Train CIoU: 0.8290 | Test CIoU: 0.7451 | LR-loc: 1.25e-05 | LR-bck: 1.25e-05
* #41 Time: 0:33:42 | Train Loss: 0.1679 | Test Loss: 0.2536 | Train CIoU: 0.8321 | Test CIoU: 0.7464 | LR-loc: 1.25e-05 | LR-bck: 1.25e-05
* #42 Time: 0:34:43 | Train Loss: 0.1661 | Test Loss: 0.2539 | Train CIoU: 0.8339 | Test CIoU: 0.7461 | LR-loc: 1.25e-05 | LR-bck: 1.25e-05
* #43 Time: 0:35:46 | Train Loss: 0.1659 | Test Loss: 0.2526 | Train CIoU: 0.8341 | Test CIoU: 0.7474 | LR-loc: 1.25e-05 | LR-bck: 1.25e-05
* #44 Time: 0:36:47 | Train Loss: 0.1643 | Test Loss: 0.2557 | Train CIoU: 0.8357 | Test CIoU: 0.7443 | LR-loc: 1.25e-05 | LR-bck: 1.25e-05
* #45 Time: 0:37:47 | Train Loss: 0.1597 | Test Loss: 0.2550 | Train CIoU: 0.8403 | Test CIoU: 0.7450 | LR-loc: 1.25e-05 | LR-bck: 1.25e-05
* #46 Time: 0:38:48 | Train Loss: 0.1571 | Test Loss: 0.2557 | Train CIoU: 0.8429 | Test CIoU: 0.7443 | LR-loc: 6.25e-06 | LR-bck: 6.25e-06
* #47 Time: 0:39:48 | Train Loss: 0.1562 | Test Loss: 0.2520 | Train CIoU: 0.8438 | Test CIoU: 0.7480 | LR-loc: 6.25e-06 | LR-bck: 6.25e-06
* #48 Time: 0:40:49 | Train Loss: 0.1529 | Test Loss: 0.2550 | Train CIoU: 0.8471 | Test CIoU: 0.7450 | LR-loc: 6.25e-06 | LR-bck: 6.25e-06
* #49 Time: 0:41:48 | Train Loss: 0.1512 | Test Loss: 0.2540 | Train CIoU: 0.8488 | Test CIoU: 0.7460 | LR-loc: 6.25e-06 | LR-bck: 6.25e-06
* #50 Time: 0:42:46 | Train Loss: 0.1504 | Test Loss: 0.2570 | Train CIoU: 0.8496 | Test CIoU: 0.7430 | LR-loc: 6.25e-06 | LR-bck: 6.25e-06

## Notes:
See new localizer/model.py for a new model structure

Localizer model was too simple. I have increased complexity of a model by adding more layers. It started to generalize much better.
Highest test CIoU was reached 0.7430 and train CIoU 0.8496 - see graph.png

Also commented this line in loader.py # v2.RandomCrop(size=(412, 412)),  # Uncomment when training classifier

