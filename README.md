# 🧠 从0到1：模型训练与开发

> 起点：零基础 | 目标：能独立训练和部署模型

## 快速开始（Docker，零配置）

```bash
# 一行启动（自动检测 GPU）
bash start.sh

# 然后打开浏览器
# Jupyter Lab → http://localhost:8888
```

容器内预装了：Python 3.11、PyTorch 2.5、CUDA 12.4、Jupyter Lab、scikit-learn、transformers、matplotlib 等全套 ML 工具链。

> 手动启动：`docker compose up -d`
> GPU 版本：`docker compose -f docker-compose.yml -f docker-compose.gpu.yml up -d`

## 目录结构

```
learn-ml/
├── README.md              ← 你在看
├── AGENTS.md              ← Agent 入口，指向 CONTEXT.md
├── CONTEXT.md             ← 完整上下文（Agent 必读）
├── ROADMAP.md             ← 全景路线图
├── TODO.md                ← 行动清单（勾了就划掉）
├── PROGRESS.md            ← 学习日志 & 进度追踪
├── Dockerfile             ← Docker 镜像（PyTorch + 全套 ML 工具）
├── docker-compose.yml     ← 容器编排
├── docker-compose.gpu.yml ← GPU 加速覆盖
├── start.sh               ← 一键启动脚本
├── notebooks/             ← Jupyter 实验笔记
├── scripts/               ← 可复用的训练/数据处理脚本
├── data/                  ← 实验数据集（gitignore）
├── models/                ← 训练好的模型 checkpoint
├── notes/                 ← 各主题的学习笔记
├── references/            ← 论文、教程、书签
└── projects/              ← 实战项目（每个一个子目录）
```

## 核心原则

1. **先跑通，再理解** —— 不要被数学卡住，先让代码跑起来
2. **一个项目一个笔记** —— 做完就写，不做完不跳
3. **错误也是进度** —— 把踩的坑记下来
4. **定期回顾** —— 每完成一个阶段，回过头看自己走了多远
