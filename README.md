# Class Model Generation from Requirements using Large Language Models

### What this repo contains
- `archive` folder that store previous experimental attempts.

- `dataset` folder containing all datasets used in this research, which are open source.

- `five_criteria_assessment` folder where containing: 
  - Prompt template used to generate PlantText diagrams (`prompt_texts/`).

  - Statistical Analysis Approach Script (`human_evaluators_script/`) & (`llm_as_a_judge_script/`).
    - `cohenkappa_1.py` (Grok vs Mistral)
    - `cohenkappa_2.py` (Human A1 vs A2)
    - `cohend_1.py` (Grok vs Mistral)
    - `cohend_2.py` (Human A1 vs A2) 

  - Folders containing the raw five-criteria (RQ2) score CSV files and graphs.

- `llm_model_generation_evaluation` folder where containing: 
  - Script to generate pairwise evaluation prompts for UML class diagrams (`generate_combinations_pairwise.py`).

  - Prompt template used to generate PlantText diagrams (`prompt_texts/`).

  - Folders containing the spearman correlation results, the generated UML model diagrams, pairwise comparision raw and justifications.

- Experiment procedure diagram illustrasting the flow of the experiment.

### Research Flow
The figure below illustrates the overall flow of the research and the experiments conducted.

<p style="position: center">
  <img src="./experiment procedure.png" alt="Experiment Flow"/>  
</p> 


### Setup


```bash
pip install numpy pandas scikit-learn pingouin
```

### Run the scripts
All scripts print results to terminal


#### Generate pairwise evaluation prompts

Minimal usage:
1) Open `generate_combinations_pairwise.py` and set `lead_text` (dataset name).
2) Ensure `data/<lead_text>.txt` (context) and `data/<lead_text>-<model>.txt` (model type) exist.
3) Run:

```bash
python generate_combinations_pairwise.py
```

#### 5 criteria evaluation
```bash
# Cohen's d
python cohend_1.py   # Grok vs Mistral
python cohend_2.py   # Human A1 vs A2

#Agreement with Cohen's Kappa
python cohenkappa_1.py  # Grok vs Mistral
python cohenkappa_2.py  # Human A1 vs A2

#Wilcoxon (Statistical significance tests)
python wilcoxon_1.py  # Grok vs Mistral
python wilcoxon_2.py  # Human A1 vs A2
```



 Prompts are written under `data/processed/<lead_text>/`.

### Prompt templates
- `prompt_texts/uml_model_generation_CoT_prompt.txt`: template to request a PlantUML class diagram from requirements.
- `prompt_texts/evaluation_prompt_best_model.txt`: template for pairwise evaluation of two PlantUML diagrams.
- `prompt_texts/evaluation_prompt_five_criteria.txt`: template for pairwise evaluation between two LLMs.

### Notes
- Binary agreement uses a simple thresholding (scores ≥4 considered acceptable).
- 5 Criteria measured: completeness, correctness, standards, understandability, terminology.


