"""Activity 2 - Workbench check.

Beginner data-science script used to prove that the ``ti2006b-workbench``
conda environment works from VS Code. It reuses the classroom dataset from
Activity 2.6, prints a small summary and saves one chart.

Run from the repository root (with the environment active):

    python activities/02-vscode-anaconda-workbench/workbench_check.py
"""

from pathlib import Path
import sys

import matplotlib

matplotlib.use("Agg")  # save the chart without opening a window
import matplotlib.pyplot as plt
import pandas as pd

ACTIVITY_DIR = Path(__file__).resolve().parent
REPO_ROOT = ACTIVITY_DIR.parents[1]
DATA_FILE = (
    REPO_ROOT
    / "activities"
    / "2.6-github-project-home"
    / "data"
    / "pokemon_go_kanto_candidates.csv"
)
FIGURE_FILE = ACTIVITY_DIR / "evidence" / "attack_vs_bulk.png"

FEATURES = ["attack_index", "bulk_index", "move_coverage_index", "meta_signal_index"]


def main() -> None:
    print(f"Python {sys.version.split()[0]} | pandas {pd.__version__} | "
          f"matplotlib {matplotlib.__version__}")

    df = pd.read_csv(DATA_FILE)
    print(f"Rows: {len(df)}  Columns: {len(df.columns)}")

    # Simple equal-weight score, only to exercise pandas.
    df["mean_score"] = df[FEATURES].mean(axis=1).round(1)
    top5 = df.sort_values("mean_score", ascending=False).head(5)
    print("\nTop 5 by equal-weight mean score:")
    print(top5[["pokemon", "type_1", "mean_score"]].to_string(index=False))

    print("\nDescriptive statistics:")
    print(df[FEATURES].describe().round(1).to_string())

    fig, ax = plt.subplots(figsize=(7, 5))
    ax.scatter(df["bulk_index"], df["attack_index"], color="#2f6db5")
    for _, row in df.iterrows():
        ax.annotate(row["pokemon"], (row["bulk_index"], row["attack_index"]),
                    fontsize=8, xytext=(3, 3), textcoords="offset points")
    ax.set_xlabel("Bulk index")
    ax.set_ylabel("Attack index")
    ax.set_title("Kanto candidates: attack vs. bulk (classroom proxy)")
    ax.grid(alpha=0.3)
    fig.tight_layout()
    FIGURE_FILE.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(FIGURE_FILE, dpi=120)
    print(f"\nChart saved to {FIGURE_FILE.relative_to(REPO_ROOT).as_posix()}")
    print("Workbench environment is ready")


if __name__ == "__main__":
    main()
