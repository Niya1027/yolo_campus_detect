# yolo_campus_detect
# YOLO校园安全目标识别训练与演示系统
# Campus_Security_YOLO_Detect
基于YOLOv8轻量化模型的校园安防目标检测实训课题

## 项目简介
本项目为人工智能专业课程实训课题，针对校园安防场景痛点：人工监控效率低、无法实时识别危险目标，自主采集校园场景图片搭建数据集，从零完整训练轻量化YOLOv8检测模型，实现离线无网络依赖的图片、视频、摄像头实时目标识别流程。
可识别三类目标：校园行人、电动车/自行车、地面遗留杂物，完整配套本地推理演示脚本，开箱即用，适合本科实训、课程作业展示。

## 环境安装
1. 创建Python虚拟环境（推荐Python 3.9版本）
2. 一键安装项目全部依赖库
```bash
pip install ultralytics opencv-python numpy matplotlib

### 核心创新点
1. 完全本地离线训练推理，无需云端预训练接口，适配无网络机房实训环境；
2. 轻量化YOLOv8模型，普通家用电脑CPU即可完成训练与实时视频检测；
3. 多模式推理脚本，支持静态图片、本地视频、电脑摄像头三种演示方式；
4. 完整整理训练指标、精度曲线、检测效果图，可直接用于实训报告与答辩PPT。

### 整体技术栈
| 模块 | 技术实现方案 |
| ---- | ------------ |
| 检测算法 | YOLOv8轻量化目标检测模型 |
| 开发环境 | Windows / Ubuntu 20.04，Python3.9 |
| 数据集处理 | MakeSense本地标注工具，自主校园场景图像数据集 |
| 图像运算 | OpenCV 视频、摄像头画面实时渲染检测框 |
| 训练工具 | Ultralytics YOLO官方训练框架 |
| 数据记录 | CSV自动保存训练损失、精度、mAP全部指标 |

## 仓库目录结构
```
yolo_campus_detect/
├─ weights/
│  └─ best.pt              # 200轮训练最优权重文件
├─ dataset/                # 校园标注数据集（train/val 图片 + 标签）
├─ runs/detect/train-8/
│  └─ report_img/        # 提取自训练缓存runs/detect/train-8，存放实训报告图表、指标曲线
├─ demo_predict.py         # 图片 / 视频 / 摄像头检测演示脚本
├─ train.py                # 模型完整训练脚本
└─ data.yaml               # 数据集类别、路径配置文件
```

## 训练核心参数
- 训练轮次 epochs: 200
- 输入图像尺寸 imgsz: 640
- 检测类别：3类（pedestrian行人、bike非机动车、sundries遗留杂物）
- 模型精度指标：
  - Precision（精确率）: 0.4134
  - Recall（召回率）: 0.47246
  - mAP@0.5: 0.20312

## 运行使用教程
### 1. 模型重新训练
修改train.py内数据集路径后，终端执行：
```bash
python train.py
```

### 2. 本地视频识别演示
修改demo_predict.py 中 source 为视频文件路径：
```python
model.predict(source="你的视频.mp4")
```
运行脚本即可输出带检测框的结果视频

### 3. 摄像头实时检测
修改参数 source=0 调用电脑内置摄像头，若使用外接摄像头则改为 source=1
```python
model.predict(source=0)
```

## 效果展示说明
report_img 文件夹内置全套实训素材：
1. results.png：训练损失、精度变化总曲线
2. BoxF1_curve、BoxPR_curve：F1分数、精度召回曲线
3. confusion_matrix.png：三分类混淆矩阵
4. val_batch0_pred.jpg：验证集样本检测效果图

## 项目不足与优化改进方案
本模型mAP@0.5指标仅0.20312，识别精度偏低，存在明显优化空间：
1. 数据集扩充：增加傍晚、雨天、人群密集等复杂校园场景图片，平衡行人、非机动车、遗留杂物三类样本数量；
2. 模型升级：更换YOLOv8s中大型模型，提升复杂目标识别能力；
3. 功能拓展：新增检测报警逻辑，识别到地面遗留杂物后弹窗提示；
4. 训练调参：调整学习率、批次大小，优化训练参数，减少模型欠拟合问题。


