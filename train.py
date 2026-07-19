from ultralytics import YOLO

# 加载预训练模型
model = YOLO("yolov8s.pt")

# 训练参数，移除无效class_weights
model.train(
    data="dataset/data.yaml",
    epochs=200,
    batch=2,
    imgsz=640,
    device="cpu",
    patience=0,
    mosaic=1.0,
    amp=False,
    # 合法参数，控制分类损失权重，区间0~1，越大越重视稀有类别
    cls=0.95
)