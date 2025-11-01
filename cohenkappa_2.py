import numpy as np
import pandas as pd
from pathlib import Path
from sklearn.metrics import cohen_kappa_score, confusion_matrix

criteria = ["completeness","correctness","standards","understandability","terminology"]

#load scores
csv_path = Path(__file__).resolve().parent / "data" / "raw_5_criteria" / "human_a1_a2_scores.csv"
scores_df = pd.read_csv(csv_path)

a1 = scores_df[scores_df["judge"] == "A1"][criteria].to_numpy().flatten()
a2 = scores_df[scores_df["judge"] == "A2"][criteria].to_numpy().flatten()


#acceptable = 1, unacceptable = 0
def to_binary(x):
    return np.where(x >= 4, 1, 0)

a1_bin = to_binary(a1)
a2_bin = to_binary(a2)

#cohen kappa
kappa = cohen_kappa_score(a1_bin, a2_bin)
agree = (a1_bin == a2_bin).mean()

print(f"Binary Cohen's Kappa (1–3 vs 4–5): {kappa:.3f}")
