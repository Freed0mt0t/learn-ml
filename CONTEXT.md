# learn-ml — Agent Context

> 每次进入这个工程，先读这个文件。

## 项目摘要

- **目标：** 用户从零基础开始学习模型训练与开发
- **模式：** 双线并行 —— 理论线（用户自驱）+ 实践线（我们对齐后动手）
- **环境：** Docker 一键启动（PyTorch 2.5 + CUDA 12.4 + Jupyter Lab）
- **仓库：** https://github.com/Freed0mt0t/learn-ml
- **创建日期：** 2026-05-09

## 用户画像

- GitHub: `Freed0mt0t`
- 学习风格：偏好动手实践，先跑通再理解
- 环境偏好：用 Docker 省去本地配置

## 当前状态

- **阶段：** 0（对齐实践项目）
- **进度：** 工程骨架已建好，Docker 环境已配置，GitHub 已绑定
- **下一步：** 逐个对齐 PROJECTS.md 中的 15 个实践项目，从 P1 开始

## 项目结构

```
learn-ml/
├── README.md              ← 项目说明（含 Docker 启动指南）
├── AGENTS.md              ← Agent 入口，指向 CONTEXT.md
├── CONTEXT.md             ← 你在看这个
├── ROADMAP.md             ← 双线全景：理论线（28 项）+ 实践线（15 项目）
├── PROJECTS.md            ← 实践项目对齐看板
├── PROGRESS.md            ← 学习日志（每次学完更新）
├── Dockerfile             ← PyTorch 2.5 + CUDA 12.4 镜像
├── docker-compose.yml     ← 容器编排
├── docker-compose.gpu.yml ← GPU 叠加
├── start.sh               ← 一键启动
├── notebooks/             ← Jupyter 实验本
├── scripts/               ← 可复用脚本
├── data/                  ← 数据集（gitignore）
├── models/                ← 训练好的模型
├── notes/                 ← 主题笔记
├── references/            ← 论文/教程书签
└── projects/              ← 实战项目（每个一个子目录）
```

## 工作流

1. **进入项目：** 读 `CONTEXT.md` → `ROADMAP.md` → `PROJECTS.md`
2. **对齐项目：** 选定下一个实践项目 → 与用户对齐目标/产出 → 建目录 → 开始
3. **记录进度：** 完成一项 → 勾掉 ROADMAP / PROJECTS → 写 PROGRESS.md
4. **写笔记：** 新概念写进 `notes/`，形成知识库
5. **写代码：** 实验放 `notebooks/`，可复用放 `scripts/`
6. **定期提交：** 每次学完 `git add -A && git commit && git push`

## 代理行为准则

- 实践项目对齐后才动手，不自作主张
- 每个项目先给最简示例让它跑起来，再扩展
- 用户卡住时，先给提示再给答案
- 每次操作前确认当前 ROADMAP 阶段是否合理
- 鼓励用户把踩的坑记进 PROGRESS.md
- Docker 环境可自行操作，环境问题直接诊断修复

---

*最后更新：2026-05-09*
