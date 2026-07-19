from ultralytics import YOLO

model_path = "weights/best.pt"
model = YOLO(model_path)

model.predict(
    source="识别2.mp4",   # 改成1代表外接摄像头#e="你的视频全名.mp4代表导入视频#单张图：source="1.jpg"多图=["1.jpg","2.jpg","3.jpg"]
    show=True,
    save=True,
    save_txt=True,
    project="runs/detect",
    name="demo_output"
)
print("采集完成，素材保存在 runs/detect/demo_output")