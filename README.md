# Domain Model Generation from Requirements using Generative AI


### What this repo contains
- Prompt template used to generate PlantUML diagrams (`prompt_texts/`).
- Script to generate pairwise evaluation prompts for UML class diagrams (`generate_combinations.py`)


- Data folders with the raw 5-criteria (RQ2) scores and the pairwise comparison stuff (RQ1) (`data/`).

- Evaluation methods for Cohen's k and Cohen's d:
  - `cohenkappa_1.py` (Grok vs Mistral),
   - `cohenkappa_2.py` (Human A1 vs A2)
  - `cohend_1.py` (Grok vs Mistral)
  - `cohend_2.py` (Human A1 vs A2)

### Setup


```bash
pip install numpy pandas scikit-learn pingouin
```

### Run the scripts
All scripts print results to terminal


#### Generate pairwise evaluation prompts

Minimal usage:
1) Open `generate_combinations.py` and set `lead_text` (dataset name).
2) Ensure `data/<lead_text>.txt` (context) and `data/<lead_text>-<model>.txt` (model type) exist.
3) Run:

```bash
python generate_combinations.py
```

#### 5 criteria evaluation stuff
```bash
# Cohen's d
python cohend_1.py   # Grok vs Mistral
python cohend_2.py   # Human A1 vs A2

#Agreement with Cohen's Kappa
python cohenkappa_1.py  # Grok vs Mistral
python cohenkappa_2.py  # Human A1 vs A2
```



 Prompts are written under `data/processed/<lead_text>/`.

### Prompt templates
- `prompt_texts/dataset_prompt1.txt`: template to request a PlantUML class diagram from requirements.
- `prompt_texts/evaluation_prompt2.txt`: template for pairwise evaluation of two PlantUML diagrams.

### Notes
- Binary agreement uses a simple thresholding (scores ≥4 considered acceptable).
- Criteria measured: completeness, correctness, standards, understandability, terminology.


