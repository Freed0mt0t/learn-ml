# 项目 01：Python 数据处理流水线

## 目标
掌握 numpy/pandas 数据处理，跑通一条完整的「脏数据 → 清洗 → EDA → 干净数据」流水线。

## 数据集
**Kaggle Titanic（泰坦尼克号乘客数据）** — 经典的脏数据集
- 含缺失值（Age、Cabin、Embarked）
- 数值 + 类别 + 文本混合
- 891 条训练数据，12 个特征

## 你将要做的

| 步骤 | 内容 | 技能 |
|------|------|------|
| 1. 加载 | 从 CSV 读数据，查看基本结构 | `pd.read_csv`, `.info()`, `.head()` |
| 2. 探查 | 统计摘要、缺失值分析、分布检查 | `.describe()`, `.isna()`, `value_counts()` |
| 3. 可视化 | 分布图、相关性、类别 vs 数值 | matplotlib, seaborn |
| 4. 清洗 | 填充缺失值、处理异常值、编码类别 | `.fillna()`, One-Hot, Label Encoding |
| 5. 导出 | 保存干净数据 | `.to_csv()` |

## 产出
- `eda_notebook.ipynb` — 完整 EDA & 数据清洗 notebook
- `output/titanic_clean.csv` — 清洗后的数据
- 一份 EDA 小结（写在 notebook 末尾 Markdown 里）

## 验收标准
- [ ] 每个缺失值列都有明确的处理策略并执行
- [ ] 至少 5 张可视化图表（分布、相关、对比）
- [ ] notebook 从头到尾可执行，无报错
- [ ] 末尾有 200 字以上的 EDA 小结
