# yolo_campus_detect
## 项目名称
基于YOLO的校园安全目标识别模型训练与演示项目

## 项目简介
本项目基于YOLO轻量化目标检测算法，针对校园场景完成行人、电动车、危险区域遗留物品等安全目标识别，支持本地图片、视频、摄像头实时推理演示。

## 开发环境
- 系统：Windows / Ubuntu 20.04
- 框架：PyTorch
- 算法：YOLOv5 / YOLOv8
- 依赖：OpenCV、NumPy、Matplotlib

## 目录结构
```
yolo_campus_detect/
├── datasets/ # 校园场景数据集、标注文件
├── models/ # 预训练权重文件
├── runs/ # 训练日志、推理输出图片
├── scripts/ # 训练、实时检测推理代码
├── config/ # 数据集、训练参数配置文件
└── README.md
```

## 运行步骤
1. 安装依赖
```bash
pip install torch torchvision opencv-python
```

2. 模型训练
```bash
python train.py
```

3. 摄像头实时识别演示
```bash
python detect_camera.py
```

## 核心功能
1. 校园场景自定义数据集训练，实现行人、非机动车、遗留物品检测；
2. 支持图片、视频离线检测与摄像头实时识别；
3. 识别结果自动保存，便于实训报告使用。

## 项目亮点
轻量化模型，普通电脑即可运行，代码模块化，易于修改拓展，贴合校园安防实训主题。
