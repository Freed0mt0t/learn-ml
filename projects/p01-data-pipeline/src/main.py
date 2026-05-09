"""
主入口：一键运行完整数据处理流水线。

用法:
    cd projects/p01-data-pipeline
    python src/main.py
"""

import sys
from pathlib import Path

import pandas as pd

# 确保能找到 src 包
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from src.load import load_titanic, print_column_info, OUTPUT_DIR
from src.clean import clean_pipeline
from src.visualize import run_all_plots


def main():
    print("=" * 60)
    print("🚢 P01: Titanic 数据处理流水线")
    print("=" * 60)
    print()

    # ── 1. 加载 ──
    print("📥 [1/4] 加载数据...")
    df = load_titanic()
    print()

    # ── 2. 初览 ──
    print("📋 [2/4] 数据初览...")
    print(f"\n列信息:")
    print(print_column_info(df).to_string(index=False))
    print(f"\n缺失值:")
    missing = df.isna().sum()
    missing_pct = (missing / len(df) * 100).round(2)
    missing_info = pd.DataFrame({"缺失数": missing, "缺失率(%)": missing_pct})
    print(missing_info[missing_info["缺失数"] > 0].to_string())
    print()

    # ── 3. EDA 可视化 ──
    print("📊 [3/4] EDA 可视化（清洗前）...")
    run_all_plots(df, save=False)
    print()

    # ── 4. 清洗 ──
    print("🧹 [4/4] 数据清洗...")
    df_clean = clean_pipeline(df)
    print()

    # ── 5. 导出 ──
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    output_path = OUTPUT_DIR / "titanic_clean.csv"
    df_clean.to_csv(output_path, index=False)
    size_kb = output_path.stat().st_size / 1024
    print(f"✅ 清洗数据已导出: {output_path} ({size_kb:.1f} KB)")
    print(f"   行数: {len(df_clean)}, 列数: {len(df_clean.columns)}")
    print()

    # ── 总结 ──
    print("=" * 60)
    print("🎉 流水线执行完成！")
    print(f"   原始: {891} 行 × 12 列")
    print(f"   清洗后: {len(df_clean)} 行 × {len(df_clean.columns)} 列")
    print(f"   缺失值: {df_clean.isna().sum().sum()} 个（全部已处理）")
    print("=" * 60)


if __name__ == "__main__":
    main()
