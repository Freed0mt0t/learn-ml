# 🗺️ ROADMAP — 模型训练学习双线全景

> 双线并行：**理论线** 你自己跟进度，**实践线** 我们逐个对齐后动手。
>
> 做完一项勾掉 `[x]`。

**进度总览：** 阶段 P1 · 理论 0/28 · 实践 1/15 已对齐

---

# 📐 理论线：从数学到架构

> 每项下面有细分知识点，学完一个勾一个。

## 阶段 T0：预备知识

- [ ] **T0.1 线性代数**
  - 向量与矩阵运算（加减、转置、点积、Hadamard 积）
  - 矩阵乘法与线性变换的几何直觉
  - 范数（L1 / L2 / Frobenius）
  - 特征值 & 特征向量（直觉层面）
  - SVD 分解（知道是什么、干嘛用）

- [ ] **T0.2 微积分**
  - 导数与偏导数
  - 梯度（方向导数的最速方向）
  - 链式法则（反向传播的数学基础）
  - 梯度下降的几何直觉
  - Jacobian & Hessian（了解概念即可）

- [ ] **T0.3 概率与统计**
  - 随机变量 & 概率分布（离散、连续）
  - 期望、方差、协方差
  - 条件概率 & 贝叶斯公式
  - 最大似然估计（MLE）
  - 常见分布：正态、伯努利、分类、Dirichlet

- [ ] **T0.4 信息论基础**
  - 自信息与熵
  - 交叉熵（分类损失函数的来源）
  - KL 散度
  - 困惑度（Perplexity）

---

## 阶段 T1：经典机器学习

- [ ] **T1.1 数据预处理**
  - 标准化 vs 归一化
  - 缺失值处理策略
  - 类别编码（One-Hot、Label、Target Encoding）
  - 数据集划分（train/val/test）
  - 数据泄露问题

- [ ] **T1.2 线性模型**
  - 线性回归：解析解 vs 梯度下降
  - 逻辑回归：sigmoid、决策边界、对数似然
  - 正则化：L1/Lasso vs L2/Ridge vs ElasticNet
  - 多分类：softmax 与交叉熵

- [ ] **T1.3 树模型**
  - 决策树：信息增益、基尼系数、剪枝
  - 随机森林：Bagging、特征随机采样
  - GBDT / XGBoost / LightGBM 原理对比
  - 特征重要性解释

- [ ] **T1.4 SVM & 核方法**
  - 最大间隔原理
  - 对偶问题与核技巧
  - 常用核函数（线性、RBF、多项式）
  - 软间隔与惩罚参数 C

- [ ] **T1.5 聚类 & 降维**
  - K-Means：Lloyd 算法、k 值选择（肘部法）
  - DBSCAN：密度聚类
  - PCA：方差最大化、特征值分解
  - t-SNE vs UMAP：可视化 vs 特征

- [ ] **T1.6 模型评估**
  - 欠拟合 / 过拟合 / 偏差方差权衡
  - 分类指标：准确率、精确率、召回率、F1、ROC/AUC
  - 回归指标：MSE、MAE、R²
  - 交叉验证（k-fold、stratified）
  - 混淆矩阵与错误分析

---

## 阶段 T2：深度学习基础

- [ ] **T2.1 神经网络基础**
  - 感知机 → 多层感知机（MLP）
  - 激活函数：ReLU、GELU、Sigmoid、Tanh 对比
  - 表示学习：隐层在学什么
  - 万能近似定理（直觉）

- [ ] **T2.2 反向传播**
  - 计算图与前向传播
  - 链式法则 → 反向梯度传播
  - 自动微分（autograd）原理
  - 常见梯度问题：消失/爆炸 + 解决方案

- [ ] **T2.3 优化器**
  - SGD vs Mini-batch GD
  - Momentum & Nesterov
  - AdaGrad / RMSProp
  - Adam / AdamW
  - 学习率预热、余弦退火

- [ ] **T2.4 正则化技术**
  - L1/L2 正则化
  - Dropout（训练 vs 推理的区别）
  - Batch Normalization / Layer Normalization
  - Data Augmentation
  - Label Smoothing
  - Early Stopping

- [ ] **T2.5 CNN 卷积神经网络**
  - 卷积层（kernel、stride、padding）
  - 池化层（max vs avg）
  - 感受野（Receptive Field）
  - 经典架构演进：LeNet → AlexNet → VGG → ResNet
  - ResNet 的残差连接原理

- [ ] **T2.6 RNN & 序列模型**
  - RNN 原理与时序展开
  - LSTM：遗忘门、输入门、输出门
  - GRU：重置门、更新门
  - 双向 RNN
  - Attention 的起源（Seq2Seq + 注意力）

---

## 阶段 T3：现代架构

- [ ] **T3.1 Transformer**
  - 自注意力机制（Q、K、V 的含义）
  - 多头注意力（Multi-Head Attention）
  - 位置编码（Sinusoidal / Learned / RoPE）
  - Layer Normalization（Pre-LN vs Post-LN）
  - 残差连接 + FFN
  - Encoder vs Decoder vs Encoder-Decoder

- [ ] **T3.2 预训练范式**
  - 词向量：Word2Vec、GloVe
  - 预训练 + 微调范式
  - BERT：MLM + NSP 预训练
  - GPT：自回归语言模型
  - T5：Text-to-Text 统一框架

- [ ] **T3.3 大规模模型**
  - Scaling Law（参数、数据、算力的关系）
  - 涌现能力（Emergent Abilities）
  - RLHF 流程：SFT → RM → PPO
  - MoE（混合专家）架构概念

- [ ] **T3.4 生成模型**
  - VAE（变分自编码器）
  - GAN（生成对抗网络）原理
  - Diffusion：前向加噪 + 反向去噪
  - Classifier-Free Guidance

- [ ] **T3.5 参数高效微调**
  - LoRA 原理：低秩分解
  - QLoRA：量化 + LoRA
  - Adapter / Prefix Tuning / Prompt Tuning
  - PEFT 库概览

---

## 阶段 T4：工程 & 部署

- [ ] **T4.1 训练工程**
  - 混合精度训练（AMP）
  - 梯度累积
  - 梯度裁剪
  - 分布式训练：DataParallel vs DDP vs FSDP
  - 检查点保存与恢复

- [ ] **T4.2 模型评估 & 调试**
  - 损失曲线分析
  - 过拟合诊断与对策
  - GPU 内存管理
  - Profiling 工具（PyTorch Profiler）

- [ ] **T4.3 模型压缩 & 部署**
  - 量化（INT8/INT4）
  - 剪枝与知识蒸馏
  - ONNX 导出
  - TorchScript
  - vLLM / TensorRT-LLM 推理框架概念

- [ ] **T4.4 MLOps**
  - 实验追踪（TensorBoard / Wandb）
  - 数据版本管理（DVC）
  - 模型注册与版本
  - CI/CD for ML

---

# 🛠️ 实践线：项目驱动

> 每个项目有明确目标、输入输出、技能点。我们逐个对齐后开始。

## 阶段 P1：打地基（2 个项目）

### 项目 1：Python 数据处理流水线

- **目标：** 掌握 numpy/pandas 数据处理，为后续准备
- **输入：** 一个原始 CSV 数据集（脏数据）
- **输出：** 清洗后的数据 + 可视化 EDA 报告
- **技能：** pandas、numpy、matplotlib、数据清洗、缺失值处理
- **文件：** `projects/p01-data-pipeline/`

### 项目 2：手写线性回归（不用 sklearn）

- **目标：** 理解梯度下降和损失函数
- **输入：** 房价数据集（或自定义线性数据）
- **输出：** 拟合曲线图 + MSE 收敛图
- **技能：** 梯度下降实现、损失函数、向量化、可视化
- **文件：** `projects/p02-linear-regression/`

---

## 阶段 P2：经典 ML 实战（4 个项目）

### 项目 3：MNIST 手写数字分类（经典 ML 版）

- **目标：** 用 sklearn 跑通完整 ML 流程
- **输入：** MNIST 数据集
- **输出：** 多模型对比报告（准确率、混淆矩阵、训练时间）
- **技能：** sklearn 全家桶、模型选择、交叉验证
- **文件：** `projects/p03-mnist-sklearn/`

### 项目 4：泰坦尼克生存预测

- **目标：** 特征工程完整流程
- **输入：** Kaggle Titanic 数据集
- **输出：** 预测结果 CSV + 特征重要性分析
- **技能：** 特征工程、缺失值策略、类别编码、集成方法
- **文件：** `projects/p04-titanic/`

### 项目 5：客户分群（RFM + K-Means）

- **目标：** 无监督学习的实际应用
- **输入：** 零售交易数据（可生成或找到公开数据）
- **输出：** 客户分群报告 + PCA 可视化 + 营销建议
- **技能：** RFM 模型、K-Means、PCA、业务洞察
- **文件：** `projects/p05-customer-segmentation/`

### 项目 6：文本情感分类（TF-IDF + 传统分类器）

- **目标：** NLP 入门 + 文本处理
- **输入：** IMDb 电影评论数据集
- **输出：** 情感二分类模型 + 词云分析
- **技能：** 文本清洗、TF-IDF、Logistic Regression、词云
- **文件：** `projects/p06-sentiment-classifier/`

---

## 阶段 P3：深度学习实战（5 个项目）

### 项目 7：PyTorch 重写 MNIST

- **目标：** PyTorch 入门，对比 sklearn
- **输入：** MNIST（同样的数据，不同的模型）
- **输出：** 训练曲线、98%+ 准确率、与项目 3 对比
- **技能：** PyTorch Dataset/DataLoader、nn.Module、训练循环
- **文件：** `projects/p07-mnist-pytorch/`

### 项目 8：CIFAR-10 图像分类（CNN）

- **目标：** CNN 实战，理解卷积
- **输入：** CIFAR-10 数据集
- **输出：** 85%+ 准确率、特征图可视化、混淆矩阵
- **技能：** CNN、BatchNorm、Data Augmentation、TensorBoard
- **文件：** `projects/p08-cifar10-cnn/`

### 项目 9：文本生成（Char-RNN / LSTM）

- **目标：** 序列模型入门
- **输入：** 莎士比亚文集 / 金庸小说
- **输出：** 生成"莎士比亚风格"文本、perplexity 曲线
- **技能：** LSTM/GRU、词表构建、序列 padding、生成策略
- **文件：** `projects/p09-text-generation/`

### 项目 10：BERT 文本分类微调

- **目标：** 预训练模型微调全流程
- **输入：** 中文情感/新闻分类数据集
- **输出：** BERT 微调模型 + 推理 API
- **技能：** HuggingFace Trainer、tokenizer、微调、评估
- **文件：** `projects/p10-bert-finetune/`

### 项目 11：Stable Diffusion 图像生成探索

- **目标：** 理解扩散模型
- **输入：** 文本 prompt
- **输出：** 图像 + 参数实验对比
- **技能：** Diffusers 库、调度器、CFG、LoRA 加载
- **文件：** `projects/p11-image-generation/`

---

## 阶段 P4：应用实战（2 个项目）

### 项目 12：RAG 问答系统

- **目标：** LLM 应用开发
- **输入：** 一个知识文档集（如公司手册、论文合集）
- **输出：** 可交互的问答 Demo（CLI 或 Web）
- **技能：** LangChain/LlamaIndex、Embedding、向量数据库、RAG 架构
- **文件：** `projects/p12-rag-qa/`

### 项目 13：FastAPI 模型部署

- **目标：** 模型上线完整流程
- **输入：** 之前训练的任意模型
- **输出：** Docker 化 API 服务 + 简单前端
- **技能：** FastAPI、Docker、REST API、ONNX
- **文件：** `projects/p13-model-serving/`

---

## 阶段 P5：综合项目（2 个项目）

### 项目 14：LoRA 微调开源 LLM

- **目标：** 高效微调完整流程
- **输入：** Qwen/ChatGLM 等中文 LLM + 自定义数据集
- **输出：** 微调后模型 + 评测报告
- **技能：** PEFT/LoRA、数据集构建、量化、推理部署
- **文件：** `projects/p14-lora-llm/`

### 项目 15：端到端 ML 项目（自选方向）

- **目标：** 独立完成完整 ML 项目
- **输入/输出：** 自选，覆盖数据处理 → 训练 → 评估 → 部署
- **技能：** 全栈 ML 工程能力
- **文件：** `projects/p15-capstone/`

---

# 📚 推荐资源

| 资源 | 适合阶段 | 类型 | 说明 |
|------|----------|------|------|
| 3Blue1Brown 线性代数 | T0 | 视频 | 几何直觉，B 站有中文 |
| 3Blue1Brown 神经网络 | T2 | 视频 | 深入理解梯度下降与反向传播 |
| d2l.ai 动手学深度学习 | T1-T3 | 书+代码 | PyTorch 版，中文友好 |
| Andrej Karpathy micrograd | T2.2 | 视频+代码 | 从零手写 autograd，经典 |
| fast.ai Practical DL | T2-T3 | 课程 | 自上而下，先跑起来 |
| Stanford CS231n | T2.5 | 课程 | CV 经典课 |
| Stanford CS224n | T2.6 | 课程 | NLP 经典课 |
| HuggingFace Course | T3 | 教程 | HF 生态最佳入门 |
| Lil'Log 博客 | T3 | 文章 | 深入浅出 Transformer 系列 |
| PyTorch 官方教程 | P3+ | 文档 | 最权威 API 指南 |

---

*最后更新：2026-05-09*
