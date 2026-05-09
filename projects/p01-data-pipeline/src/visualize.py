"""
数据可视化模块。

生成 EDA 图表：分布图、相关性热力图、交叉分析等。
"""

import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# 全局样式
plt.rcParams.update(
    {
        "font.size": 12,
        "axes.titlesize": 14,
        "figure.dpi": 100,
    }
)
sns.set_style("whitegrid")


def plot_survival_overview(df: pd.DataFrame, save: bool = False) -> None:
    """生还率总览：饼图 + 性别 + 舱位等级。"""
    fig, axes = plt.subplots(1, 3, figsize=(16, 5))

    # 饼图
    surv_counts = df["Survived"].value_counts()
    axes[0].pie(
        surv_counts,
        labels=["死亡", "生还"],
        autopct="%1.1f%%",
        colors=["#e74c3c", "#2ecc71"],
        startangle=90,
    )
    axes[0].set_title("生还率总览")

    # 性别 vs 生还
    surv_sex = df.groupby("Sex")["Survived"].mean()
    surv_sex.plot(kind="bar", ax=axes[1], color=["#3498db", "#e74c3c"])
    axes[1].set_title("各性别生还率")
    axes[1].set_ylabel("生还率")
    axes[1].set_xticklabels(axes[1].get_xticklabels(), rotation=0)

    # 舱位 vs 生还
    surv_pclass = df.groupby("Pclass")["Survived"].mean()
    surv_pclass.plot(
        kind="bar", ax=axes[2], color=["#f39c12", "#9b59b6", "#1abc9c"]
    )
    axes[2].set_title("各舱位等级生还率")
    axes[2].set_ylabel("生还率")
    axes[2].set_xticklabels(["1等", "2等", "3等"], rotation=0)

    plt.tight_layout()
    if save:
        fig.savefig("output/01_survival_overview.png", dpi=150, bbox_inches="tight")
    plt.show()


def plot_numeric_distributions(df: pd.DataFrame, save: bool = False) -> None:
    """数值特征分布直方图。"""
    num_cols = ["Age", "Fare", "SibSp", "Parch"]

    fig, axes = plt.subplots(2, 2, figsize=(14, 10))
    axes = axes.flatten()

    for i, col in enumerate(num_cols):
        if col in df.columns:
            df[col].hist(
                bins=40, ax=axes[i], color="steelblue", edgecolor="white"
            )
            axes[i].axvline(
                df[col].median(),
                color="red",
                linestyle="--",
                label=f"中位数={df[col].median():.1f}",
            )
            axes[i].set_title(f"{col} 分布")
            axes[i].legend()

    plt.tight_layout()
    if save:
        fig.savefig("output/02_numeric_distributions.png", dpi=150, bbox_inches="tight")
    plt.show()


def plot_correlation_heatmap(df: pd.DataFrame, save: bool = False) -> None:
    """数值特征相关性热力图。"""
    corr_cols = ["Survived", "Pclass", "Age", "SibSp", "Parch", "Fare"]
    available = [c for c in corr_cols if c in df.columns]
    corr = df[available].corr()

    fig, ax = plt.subplots(figsize=(8, 6))
    sns.heatmap(
        corr,
        annot=True,
        cmap="RdBu_r",
        center=0,
        fmt=".2f",
        linewidths=0.5,
        square=True,
        ax=ax,
    )
    ax.set_title("特征相关性热力图")
    if save:
        fig.savefig("output/03_correlation_heatmap.png", dpi=150, bbox_inches="tight")
    plt.show()


def plot_age_survival(df: pd.DataFrame, save: bool = False) -> None:
    """年龄分布 × 生还状态。"""
    fig, ax = plt.subplots(figsize=(10, 5))
    for survived, label, color in [
        (0, "死亡", "#e74c3c"),
        (1, "生还", "#2ecc71"),
    ]:
        subset = df[df["Survived"] == survived]["Age"].dropna()
        ax.hist(subset, bins=30, alpha=0.6, label=label, color=color)
    ax.set_xlabel("年龄")
    ax.set_ylabel("人数")
    ax.set_title("年龄分布：生还 vs 死亡")
    ax.legend()
    if save:
        fig.savefig("output/04_age_survival.png", dpi=150, bbox_inches="tight")
    plt.show()


def plot_embarked_survival(df: pd.DataFrame, save: bool = False) -> None:
    """登船港口 × 生还。"""
    if "Embarked" not in df.columns:
        print("⚠️  没有 Embarked 列，跳过")
        return

    emb_clean = df["Embarked"].dropna()

    fig, axes = plt.subplots(1, 2, figsize=(12, 5))

    emb_clean.value_counts().plot(
        kind="bar", ax=axes[0], color=["#3498db", "#e67e22", "#2ecc71"]
    )
    axes[0].set_title("各港口登船人数")
    axes[0].set_xlabel("港口")

    df.groupby("Embarked")["Survived"].mean().plot(
        kind="bar", ax=axes[1], color=["#3498db", "#e67e22", "#2ecc71"]
    )
    axes[1].set_title("各港口生还率")
    axes[1].set_ylabel("生还率")

    plt.tight_layout()
    if save:
        fig.savefig("output/05_embarked_survival.png", dpi=150, bbox_inches="tight")
    plt.show()


def plot_sex_class_survival(df: pd.DataFrame, save: bool = False) -> None:
    """性别 × 舱位等级 × 生还率热力图。"""
    cross = df.pivot_table(
        index="Sex", columns="Pclass", values="Survived", aggfunc="mean"
    )

    fig, ax = plt.subplots(figsize=(8, 5))
    sns.heatmap(cross, annot=True, fmt=".2f", cmap="YlGn", ax=ax)
    ax.set_title("生还率：性别 × 舱位等级")

    if save:
        fig.savefig(
            "output/06_sex_class_survival.png", dpi=150, bbox_inches="tight"
        )
    plt.show()


def run_all_plots(df: pd.DataFrame, save: bool = False) -> None:
    """运行全部 6 张可视化图表。"""
    print("📊 生成可视化图表...\n")
    plot_survival_overview(df, save=save)
    plot_numeric_distributions(df, save=save)
    plot_correlation_heatmap(df, save=save)
    plot_age_survival(df, save=save)
    plot_embarked_survival(df, save=save)
    plot_sex_class_survival(df, save=save)
    print("✅ 全部图表生成完成")
