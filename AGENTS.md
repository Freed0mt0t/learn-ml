# AGENTS.md — learn-ml

进入此工程时，先读 `CONTEXT.md` 恢复完整上下文，再读 `ROADMAP.md` 确定当前任务。

核心原则：引导动手 > 灌输理论，先跑通 > 先理解。

## 实践项目工程规范 ⚠️ 强制

每新建一个实践项目，**必须**包含以下结构：

```
projects/pXX-project-name/
├── README.md              ← 项目说明 & 验收标准
├── requirements.txt       ← 依赖声明
├── data/                  ← 原始数据（已下载到本地，不依赖网络）
├── output/                ← 输出产物（模型、图表、清洗后数据）
├── notebooks/             ← Jupyter 探索（可选，1 个即可）
└── src/                   ← Python 模块（核心）
    ├── __init__.py
    ├── load.py            ← 数据加载
    ├── clean.py           ← 预处理/清洗
    ├── visualize.py       ← 可视化（如适用）
    ├── model.py           ← 模型定义（如适用）
    ├── train.py           ← 训练逻辑（如适用）
    └── main.py            ← 一键运行入口（python src/main.py）
```

**硬性要求：**
- 数据集必须预先下载到 `data/`，不能运行时从网络拉取
- `python src/main.py` 必须能无报错运行
- `.ipynb` 放 `notebooks/`，不在根目录散落
- 模块职责单一：load 不做 clean，clean 不做 visualize
