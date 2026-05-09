"""
数据清洗模块。

完整流水线：删除无用列 → 填充缺失值 → 异常值检查 → 类别编码。
"""

import pandas as pd
import numpy as np


def drop_useless_columns(df: pd.DataFrame) -> pd.DataFrame:
    """删除对基础分析无用的列。

    PassengerId: 自增索引
    Name: 基础 EDA 不用
    Ticket: 船票号，信息量低
    """
    cols_to_drop = ["PassengerId", "Name", "Ticket"]
    existing = [c for c in cols_to_drop if c in df.columns]
    if existing:
        df = df.drop(columns=existing)
        print(f"🗑️  已删除: {', '.join(existing)}")
    return df


def drop_high_missing_columns(df: pd.DataFrame, threshold: float = 0.7) -> pd.DataFrame:
    """删除缺失率高于阈值的列。

    Args:
        df: 输入 DataFrame。
        threshold: 缺失率阈值，默认 0.7（70%）。
    """
    for col in df.columns:
        missing_rate = df[col].isna().mean()
        if missing_rate > threshold:
            df = df.drop(columns=[col])
            print(f"🗑️  已删除 {col}（缺失率 {missing_rate:.1%} > {threshold:.0%}）")
    return df


def fill_median(df: pd.DataFrame, columns: list[str]) -> pd.DataFrame:
    """用中位数填充指定列的缺失值。"""
    for col in columns:
        if col in df.columns and df[col].isna().any():
            median_val = df[col].median()
            df[col] = df[col].fillna(median_val)
            print(f"📝 {col}: {df[col].isna().sum() if 'before' in locals() else 0} 个缺失 → 用中位数 {median_val:.1f} 填充")
    return df


def fill_mode(df: pd.DataFrame, columns: list[str]) -> pd.DataFrame:
    """用众数填充指定列的缺失值。"""
    for col in columns:
        if col in df.columns and df[col].isna().any():
            mode_val = df[col].mode()[0]
            df[col] = df[col].fillna(mode_val)
            print(f"📝 {col}: 缺失值 → 用众数 {mode_val} 填充")
    return df


def encode_binary(df: pd.DataFrame, col: str, mapping: dict) -> pd.DataFrame:
    """二值编码。"""
    if col in df.columns:
        df[col] = df[col].map(mapping)
        print(f"🔢 {col}: {mapping}")
    return df


def encode_onehot(
    df: pd.DataFrame, columns: list[str], drop_first: bool = True
) -> pd.DataFrame:
    """One-Hot 编码。"""
    existing = [c for c in columns if c in df.columns]
    if existing:
        df = pd.get_dummies(df, columns=existing, prefix=existing, drop_first=drop_first)
        print(f"🔢 {', '.join(existing)}: One-Hot 编码完成")
    return df


def check_outliers(df: pd.DataFrame, columns: list[str]) -> dict:
    """用 IQR 方法检查异常值。

    Returns:
        dict: {列名: 异常值数量}
    """
    results = {}
    for col in columns:
        if col not in df.columns:
            continue
        Q1 = df[col].quantile(0.25)
        Q3 = df[col].quantile(0.75)
        IQR = Q3 - Q1
        lower = Q1 - 1.5 * IQR
        upper = Q3 + 1.5 * IQR
        outliers = df[(df[col] < lower) | (df[col] > upper)]
        results[col] = len(outliers)
        if len(outliers) > 0:
            print(f"⚠️  {col}: {len(outliers)} 个异常值 (IQR 范围 [{lower:.1f}, {upper:.1f}])")
        else:
            print(f"✅ {col}: 无异常值")
    return results


def clean_pipeline(df: pd.DataFrame) -> pd.DataFrame:
    """执行完整清洗流水线。

    Returns:
        清洗后的 DataFrame。
    """
    print("=" * 50)
    print("🧹 开始数据清洗")
    print("=" * 50)
    print(f"清洗前: {df.shape[0]} 行 × {df.shape[1]} 列, "
          f"缺失值 {df.isna().sum().sum()} 个\n")

    # 1. 删除无用列
    df = drop_useless_columns(df)

    # 2. 删除高缺失列
    df = drop_high_missing_columns(df, threshold=0.7)

    # 3. 填充缺失值
    df = fill_median(df, ["Age"])
    df = fill_mode(df, ["Embarked"])

    # 4. 类别编码
    df = encode_binary(df, "Sex", {"male": 0, "female": 1})
    df = encode_onehot(df, ["Embarked"], drop_first=True)

    # 5. 异常值检查
    print()
    check_outliers(df, ["Age", "Fare", "SibSp", "Parch"])

    print(f"\n清洗后: {df.shape[0]} 行 × {df.shape[1]} 列, "
          f"缺失值 {df.isna().sum().sum()} 个")
    print("=" * 50)
    return df
