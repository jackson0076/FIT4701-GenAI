import pandas as pd
from scipy.stats import wilcoxon

criteria = ["completeness","correctness","standards","understandability","terminology"]
df = pd.read_csv("results/raw_5_criteria/grok_mistral_scores.csv")

for judge in ["Grok", "Mistral"]:
    print(f"\n{judge}")
    for crit in criteria:
        scores = df[df["judge"] == judge][crit].to_numpy()
        stat, p = wilcoxon(scores - 3)
        print(f"{crit}: Wilcoxon p={p:.4f}")