import numpy as np
import pandas as pd
import pingouin as pg
from pathlib import Path

criteria = ["completeness","correctness","standards","understandability","terminology"]
EFFECT_SIZE_LABELS = {0.0: "none", 0.2: "small", 0.5: "medium", 0.8: "large"}


def effect_size_label(value: float) -> str:
    abs_d = abs(value)
    for threshold, label in sorted(EFFECT_SIZE_LABELS.items(), reverse=True):
        if abs_d >= threshold:
            return label
    return "none"



repo_root = Path(__file__).resolve().parents[3]
csv_path = repo_root / "results" / "raw_5_criteria" / "human_a1_a2_scores.csv"
scores_df = pd.read_csv(csv_path)

a1 = scores_df[scores_df["judge"] == "A1"][criteria].to_dict(orient="list")
a2 = scores_df[scores_df["judge"] == "A2"][criteria].to_dict(orient="list")


rows = []
for crit in criteria:
    mean_val = np.mean([np.mean(a1[crit]), np.mean(a2[crit])])
    d = pg.compute_effsize(a1[crit], a2[crit], eftype="cohen")
    eff = effect_size_label(d)
    rows.append({"Criterion": crit, "Mean": round(mean_val, 3), "Cohen's d": round(d, 2), "Eff. S.": eff})

df = pd.DataFrame(rows)
print(df.to_string(index=False))
