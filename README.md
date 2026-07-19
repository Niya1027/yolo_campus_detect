# yolo_campus_detect
# YOLO校园安全目标识别训练与演示系统
# Campus_Security_YOLO_Detect
基于YOLOv8轻量化模型的校园安防目标检测实训课题

## 项目简介
本项目为人工智能专业课程实训课题，针对校园安防场景痛点：人工监控效率低、无法实时识别危险目标，自主采集校园场景图片搭建数据集，从零完整训练轻量化 YOLOv8 检测模型，实现离线无网络依赖的图片、视频、摄像头实时目标识别流程。
可识别四类目标：安全帽、禁止通行标识、灭火器、校园遗留危险物品，完整配套本地推理演示脚本，开箱即用，适合本科实训、课程作业展示。

### 核心创新点
1. 完全本地离线训练推理，无需云端预训练接口，适配无网络机房实训环境；
2. 轻量化 YOLOv8-s 模型，普通家用电脑 CPU 即可完成训练与实时视频检测；
3. 多模式推理脚本，支持静态图片、本地视频、电脑摄像头三种演示方式；
4. 完整整理训练指标、精度曲线、检测效果图，可直接用于实训报告与答辩 PPT。

### 整体技术栈
| 模块 | 技术实现方案 |
| ---- | ------------ |
| 检测算法 | YOLOv8-s 轻量化目标检测模型 |
| 开发环境 | Windows 10/11，Python3.9 |
| 数据集处理 | MakeSense 本地标注工具，自主校园场景图像数据集 |
| 图像运算 | OpenCV 视频、摄像头画面实时渲染检测框 |
| 训练工具 | Ultralytics YOLO 官方训练框架 |
| 数据记录 | CSV 自动保存训练损失、精度、mAP 全部指标 |

## 仓库目录结构
```
yolo_campus_detect/
├─ weights/
│  └─ best.pt              # 100轮训练最优权重文件
├─ dataset/                # 校园标注数据集
│  ├─ train/               # 训练集images图片 + labels标注txt
│  ├─ val/                 # 验证集images图片 + labels标注txt
│  └─ data.yaml            # 数据集类别、路径配置文件
├─ runs/detect/train/
│  ├─ weights/             # 训练过程权重文件
│  └─ report_img/          # 实训报告专用图表、指标效果图
├─ demo_predict.py         # 图片 / 视频 / 摄像头检测演示脚本
└─ train.py                # 模型完整训练脚本（支持断点续训）
```

## 环境依赖安装
项目运行前需要一次性安装全部Python依赖库，打开终端/PowerShell执行以下命令：
```bash
pip install ultralytics torch torchvision opencv-python numpy matplotlib
```
### 各库作用说明
- ultralytics：YOLOv8 官方训练推理核心框架
- torch、torchvision：深度学习底层运算框架
- opencv-python：摄像头、视频、图像读取与绘制检测框
- numpy：图像像素、训练数值矩阵运算
- matplotlib：自动生成训练损失、精度可视化图表

## 训练核心参数
- 训练轮次 epochs: 100
- 输入图像尺寸 imgsz: 640
- Batch尺寸 batch: 4
- 训练设备：CPU（Intel i7-14650HX）
- 训练总耗时：2.180 小时
- 检测类别共4类：
  0 - 安全帽
  1 - 禁止通行标识
  2 - 灭火器
  3 - 校园遗留危险物品
- 数据集划分：训练集160张，验证集40张，8:2划分
- 模型最终综合精度指标：
  - Precision（整体精确率）: 0.981
  - Recall（整体召回率）: 0.888
  - mAP@0.5: 0.948
  - mAP@0.5-0.95: 0.664

## 运行使用教程
### 1. 模型完整训练
数据集路径已在data.yaml内配置完成，终端直接执行：
```bash
python train.py
```
中中途按 Ctrl+C 可暂停训练；后续接续训练执行命令：
```bash
python train.py resume=True
```

### 2. 本地图片/视频识别演示
修改 demo_predict.py 中 source 参数，填入图片或视频文件路径：
```python
model.predict(source="demo/videos/测试视频2.mp4", save=True, conf=0.5, show=True)
```
运行脚本自动输出带标注检测框的结果文件。

### 3. 摄像头实时检测
source=0 调用电脑内置摄像头，外接摄像头修改为 source=1
```python
model.predict(source=0, save=True, conf=0.5, show=True)
```

## 项目亮点
轻量化 YOLOv8 模型，普通电脑 CPU 即可运行，代码模块化易修改拓展，贴合校园安防实训课题

## 效果展示说明
模型存在少量类别误识别（灭火器与禁止通行标识混淆），原因是两类目标红色视觉特征相近、训练样本同框较多；可通过扩充单类别样本、调高分类损失权重重新训练优化识别精度。
- report_img 文件夹内置全套实训素材：
1. results.png：训练损失、精度变化总曲线
2. BoxF1_curve.png、BoxPR_curve.png：F1 分数、精确率 - 召回率曲线
3. confusion_matrix.png：四分类混淆矩阵
4. val_batch0_pred.jpg：验证集样本检测效果图

## 项目不足与优化改进方案
本模型整体 mAP@0.5 达 0.948，基础识别效果良好，但 mAP@0.5-0.95 仅 0.664，远距离小尺寸安防目标识别精度存在优化空间：
1. 数据集扩充：增加傍晚、逆光、人群遮挡等复杂校园场景图片，均衡安全帽、标识、灭火器、遗留物品四类样本数量；
2. 模型升级：更换 YOLOv8m 中型模型，提升小目标、遮挡物体识别能力；
3. 功能拓展：新增检测报警逻辑，识别到校园遗留危险物品后弹窗提醒；
4. 训练调参：调整学习率、批次大小、多尺度图像增强参数，提升模型多尺寸目标检测鲁棒性。
