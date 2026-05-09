# 项目 01：Python 数据处理流水线

## 数据集
**Kaggle Titanic** — 891 条 × 12 列，含缺失值/类别/数值混合

## 运行

```bash
# 方式 1: 脚本一键运行
cd projects/p01-data-pipeline
python src/main.py

# 方式 2: Jupyter 探索
# 打开 notebooks/eda_notebook.ipynb 逐步运行
```

## 工程结构

```
p01-data-pipeline/
├── README.md              ← 项目说明 & 验收标准
├── requirements.txt       ← 依赖
├── data/
│   └── titanic.csv        ← 原始数据
├── output/
│   └── titanic_clean.csv  ← 清洗后输出
├── notebooks/
│   └── eda_notebook.ipynb ← Jupyter 探索
└── src/
    ├── __init__.py
    ├── load.py            ← 数据加载
    ├── clean.py           ← 清洗流水线
    ├── visualize.py       ← EDA 可视化
    └── main.py            ← 一键运行入口
```

## 验收标准
- [ ] `python src/main.py` 无报错执行完成
- [ ] 每个缺失值列有明确的处理策略
- [ ] 至少 5 张可视化图表
- [ ] 末尾有 200 字以上 EDA 小结
