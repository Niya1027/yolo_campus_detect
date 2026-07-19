from ultralytics import YOLO
# 加载你刚训练完成的校园安全识别最优模型
model = YOLO("weights/best.pt")

# 1. 图片测试（测试1.jpg）
model.predict(source="测试2.jpg", save=True, conf=0.65)
# 2. 视频演示（测试视频1.mp4，弹出实时画面）
#model.predict(source="测试视频2.mp4", save=True, conf=0.65, show=True)

# 3. 电脑摄像头实时检测（答辩现场演示用，注释取消即可）
# model.predict(source=0, save=True, conf=0.5, show=True)