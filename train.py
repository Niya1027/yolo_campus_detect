from ultralytics import YOLO

# 加载轻量化模型yolov8s，速度精度平衡
model = YOLO("yolov8s.pt")

# 训练参数，适配电脑CPU，降低卡顿
model.train(
    data="dataset/data.yaml",
    epochs=100,
    batch=4,
    imgsz=640,
    device="cpu",
    workers=0
)