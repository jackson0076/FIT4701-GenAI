import numpy as np
import pandas as pd
from pathlib import Path
from sklearn.metrics import cohen_kappa_score, confusion_matrix

criteria = ["completeness","correctness","standards","understandability","terminology"]


repo_root = Path(__file__).resolve().parents[3]
csv_path = repo_root / "results" / "raw_5_criteria" / "grok_mistral_scores.csv"
scores_df = pd.read_csv(csv_path)


#flatten scores
grok = scores_df[scores_df["judge"] == "Grok"][criteria].to_numpy().flatten()
mistral = scores_df[scores_df["judge"] == "Mistral"][criteria].to_numpy().flatten()

#
def to_binary(x):
    return np.where(x >= 4, 1, 0)

grok_bin = to_binary(grok)
mistral_bin = to_binary(mistral)

#cohen kappa
kappa = cohen_kappa_score(grok_bin, mistral_bin)
agree = (grok_bin == mistral_bin).mean()

print(f"Binary Cohen's Kappa (1-3 vs 4-5): {kappa:.3f}")

