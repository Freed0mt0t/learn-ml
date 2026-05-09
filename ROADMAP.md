# 🗺️ 学习路线图

> 从零基础到能独立训练模型的全景规划

---

## 阶段 0：环境与工具 🔧

| # | 主题 | 目标 |
|---|------|------|
| 0.1 | Python 环境搭建 | 装好 Python + pip + venv |
| 0.2 | Jupyter 上手 | 会用 notebook 做实验 |
| 0.3 | PyTorch 安装 | GPU/CPU 版 PyTorch 装好并能 `import torch` |
| 0.4 | Git 基础 | clone, commit, push, branch |

---

## 阶段 1：数学地基 📐

> 够用就行，不要深陷推导。理解直觉，会用工具算。

| # | 主题 | 核心概念 |
|---|------|----------|
| 1.1 | 线性代数 | 向量、矩阵、点积、特征值直觉 |
| 1.2 | 微积分 | 导数、梯度、链式法则、梯度下降 |
| 1.3 | 概率与统计 | 分布、期望、贝叶斯、最大似然 |
| 1.4 | 信息论入门 | 熵、交叉熵、KL 散度 |

---

## 阶段 2：经典机器学习 🏛️

| # | 主题 | 实践 |
|---|------|------|
| 2.1 | 数据预处理 | 归一化、缺失值、编码、划分数据集 |
| 2.2 | 线性回归 & 逻辑回归 | 从零实现 + sklearn |
| 2.3 | 决策树 & 随机森林 | 可视化决策边界 |
| 2.4 | SVM | 核方法直觉 |
| 2.5 | K-Means & 降维 | PCA 可视化 |
| 2.6 | 模型评估 | 交叉验证、混淆矩阵、ROC/AUC |

---

## 阶段 3：深度学习基础 🧬

| # | 主题 | 实践 |
|---|------|------|
| 3.1 | 感知机 → 多层网络 | 手写前向传播 |
| 3.2 | 反向传播 | 手算梯度 → PyTorch autograd |
| 3.3 | PyTorch 基础 | Tensor、Dataset、DataLoader |
| 3.4 | 全连接网络实战 | MNIST 手写数字识别 |
| 3.5 | CNN 卷积网络 | CIFAR-10 图像分类 |
| 3.6 | RNN / LSTM | 文本序列预测 |
| 3.7 | 正则化技巧 | Dropout、BatchNorm、Weight Decay |
| 3.8 | 训练技巧大全 | 学习率调度、早停、梯度裁剪 |

---

## 阶段 4：现代架构 ⚡

| # | 主题 | 实践 |
|---|------|------|
| 4.1 | Transformer 原理 | Attention is all you need |
| 4.2 | 预训练模型 | HuggingFace 生态入门 |
| 4.3 | BERT 微调 | 文本分类/情感分析 |
| 4.4 | GPT 家族理解 | Decoder-only 架构 |
| 4.5 | 图像生成入门 | Diffusion 原理 + Stable Diffusion |
| 4.6 | LoRA / QLoRA | 高效微调技术 |

---

## 阶段 5：工程化 & 实战 🏗️

| # | 主题 | 实践 |
|---|------|------|
| 5.1 | 实验管理 | TensorBoard / Wandb |
| 5.2 | 模型部署 | ONNX / TorchScript / FastAPI |
| 5.3 | 分布式训练入门 | DDP、FSDP 概念 |
| 5.4 | MLOps 基础 | 数据版本、模型版本、流水线 |
| 5.5 | 完整项目实战 | 选一个方向做端到端 |

---

## 阶段 6：专精方向 🎯

> 根据兴趣选择一个深入

| 方向 | 关键词 |
|------|--------|
| CV（计算机视觉） | 目标检测、分割、ViT、YOLO |
| NLP（自然语言处理） | RAG、Agent、Prompt Engineering |
| 语音 | ASR、TTS、Whisper |
| 推荐系统 | 协同过滤、双塔、多任务 |
| RL（强化学习） | DQN、PPO、RLHF |

---

## 推荐资源

| 资源 | 类型 | 说明 |
|------|------|------|
| 3Blue1Brown 神经网络 | 视频 | 直观理解神经网络 |
| Andrej Karpathy micrograd | 视频+代码 | 从零实现 autograd |
| d2l.ai (动手学深度学习) | 书+代码 | 中文友好，PyTorch 版 |
| fast.ai | 课程 | 自上而下，先跑起来 |
| HuggingFace Course | 教程 | 预训练模型实战 |
| PyTorch 官方教程 | 文档 | 最权威的 PyTorch 指南 |
