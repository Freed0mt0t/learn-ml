# 笔记：Titanic 数据清洗 & EDA

## 数据集
- **来源:** Kaggle Titanic 竞赛
- **规模:** 891 行 × 12 列
- **任务:** 预测乘客是否生还（二分类）

## 学到的 pandas 操作

| 操作 | 代码 | 场景 |
|------|------|------|
| 读 CSV | `pd.read_csv(url)` | 数据加载 |
| 基本信息 | `.info()`, `.describe()`, `.shape` | 初览数据 |
| 缺失值 | `.isna().sum()`, `.isna().mean()` | 发现脏数据 |
| 分组统计 | `.groupby('col').agg()` | 按类别分析 |
| 填充缺失 | `.fillna(value)` | 缺失值处理 |
| 映射编码 | `.map({'a':0, 'b':1})` | 二值编码 |
| One-Hot | `pd.get_dummies()` | 名义变量 |
| 删除列/行 | `.drop(columns=[])` | 去除无用特征 |
| 透视表 | `.pivot_table()` | 交叉分析 |
| 导出 CSV | `.to_csv(path)` | 保存结果 |

## 可视化技巧

| 图表 | 用途 | seaborn/matplotlib |
|------|------|-------------------|
| 饼图 | 比例分布 | `plt.pie()` |
| 柱状图 | 类别对比 | `df.plot(kind='bar')` |
| 直方图 | 数值分布 | `df.hist()` 或 `sns.histplot()` |
| 热力图 | 相关性矩阵 | `sns.heatmap(corr, annot=True)` |
| 箱线图 | 异常值检测 | `df.plot(kind='box')` |
| 分组直方图 | 类别+数值 | `plt.hist(subset, alpha=0.6, label=...)` |

## 踩坑记录
- (记录你遇到的问题)

## 下一步
- 用清洗后的数据做项目 02：手写线性回归
