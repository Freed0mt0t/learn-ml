"""
数据加载模块。

从本地 CSV 读取 Titanic 数据集，返回 DataFrame。
"""

import pandas as pd
from pathlib import Path

# 项目根目录相对于此文件
PROJECT_ROOT = Path(__file__).resolve().parent.parent
DATA_DIR = PROJECT_ROOT / "data"
OUTPUT_DIR = PROJECT_ROOT / "output"

# 列含义速查表
COLUMN_INFO = {
    "PassengerId": "乘客ID",
    "Survived": "是否生还 (0=死亡, 1=生还)",
    "Pclass": "船舱等级 (1/2/3)",
    "Name": "姓名",
    "Sex": "性别",
    "Age": "年龄",
    "SibSp": "同行兄弟姐妹/配偶数",
    "Parch": "同行父母/子女数",
    "Ticket": "船票号码",
    "Fare": "票价",
    "Cabin": "客舱号",
    "Embarked": "登船港口 (C=Cherbourg, Q=Queenstown, S=Southampton)",
}


def load_titanic(filename: str = "titanic.csv") -> pd.DataFrame:
    """加载 Titanic 数据集。

    Args:
        filename: CSV 文件名，默认从 data/ 目录读取。

    Returns:
        pandas DataFrame，891 行 × 12 列。

    Raises:
        FileNotFoundError: 如果 data 目录下找不到该文件。
    """
    filepath = DATA_DIR / filename
    if not filepath.exists():
        raise FileNotFoundError(
            f"找不到数据文件: {filepath}\n请确保 {filename} 在 data/ 目录下。"
        )

    df = pd.read_csv(filepath)
    print(f"📊 加载完成: {df.shape[0]} 行 × {df.shape[1]} 列")
    return df


def print_column_info(df: pd.DataFrame) -> None:
    """打印数据列含义表。"""
    info = []
    for col in df.columns:
        desc = COLUMN_INFO.get(col, "（未知）")
        dtype = str(df[col].dtype)
        info.append({"列名": col, "含义": desc, "类型": dtype})
    return pd.DataFrame(info)
