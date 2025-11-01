import pandas as pd
from scipy.stats import wilcoxon
from pathlib import Path

criteria = ["completeness","correctness","standards","understandability","terminology"]
repo_root = Path(__file__).resolve().parents[3]
csv_path = repo_root / "results" / "raw_5_criteria" / "grok_mistral_scores.csv"
df = pd.read_csv(csv_path)

for judge in ["Grok", "Mistral"]:
    print(f"\n{judge}")
    for crit in criteria:
        scores = df[df["judge"] == judge][crit].to_numpy()
        stat, p = wilcoxon(scores - 3)
        print(f"{crit}: Wilcoxon p={p:.4f}")