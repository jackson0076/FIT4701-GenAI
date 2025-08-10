from itertools import combinations
import os
import pandas as pd

def generate_combinations(models):
    combinations_list = []
    for host in models:
        others = [p for p in models if p != host]
        for p1, p2 in combinations(others, 2):
            combinations_list.append([host, p1, p2])
    # Create dataframe
    df = pd.DataFrame(combinations_list, columns=['LLM Judge', 'Model 1', 'Model 2'])   
    return df

def export_combinations_csv(df):
    df.to_csv('combinations.csv', index=False)

def generate_prompt(context, modelfile_a, modelfile_b):
    input_dir = 'data'
    with open(os.path.join(input_dir, context), 'r', encoding='utf-8') as file:
        context_read = file.read()
    with open(os.path.join(input_dir, modelfile_a), 'r', encoding='utf-8') as file:
        modelfile_a_read = file.read()
    with open(os.path.join(input_dir, modelfile_b), 'r', encoding='utf-8') as file:
        modelfile_b_read = file.read()

    prompt = f"""
    Context: {context_read}

    PlantUML result A: {modelfile_a_read}

    PlantUML result B: {modelfile_b_read}

    Which PlantUML result better reflects the context based on the following
    criteria:
    − Uses appropriate conceptual classes aligned with the domain
    − Applies essential associations that must be preserved for domain
    reasoning or system behavior
    − Models attributes with appropriate data types, avoiding design−specific
    details
    − Uses terminology consistent with the given context
    − Adheres to UML class diagram standards

    Please indicate whether Result A or B is more accurate overall, and briefly
    explain your reasoning. Provide your answer with a score of 1−100.
"""
    output_dir = 'data_fixed'
    os.makedirs(output_dir, exist_ok=True)
    base_a = os.path.splitext(os.path.basename(modelfile_a))[0]
    base_b = os.path.splitext(os.path.basename(modelfile_b))[0]
    out_name = f'{base_a} vs {base_b}.txt'
    out_path = os.path.join(output_dir, out_name)

    with open(out_path, 'w', encoding='utf-8') as file:
        file.write(prompt)

    return out_path


def generate_prompt_all():
    for model_a, model_b in combinations(participants, 2):
        context_path =CONTEXT_FILE
        model_a_path = file_participants[model_a]
        model_b_path = file_participants[model_b]
        print(context_path, model_a_path, model_b_path)
        generate_prompt(context_path, model_a_path, model_b_path)




'''
CUSTOMISE EVERYTHING HERE
mostly just change the context file and the file_participants dict, since we will vary the datasets
'''
participants = ['ChatGPT GPT-4o', 'Claude 3.7 Sonnet', 'Gemini 2.0 Flash', 'Llama 3.2']

file_participants = {
    'ChatGPT GPT-4o': 'gpt 4.0 g04.txt',
    'Claude 3.7 Sonnet': 'claude g04.txt',
    'Gemini 2.0 Flash': 'gemini 2.0 g04.txt',
    'Llama 3.2': 'llama 3.2 g04.txt'
}

CONTEXT_FILE = 'context g04.txt'
combinations_df = generate_combinations(participants)

#generate_prompt('context g04.txt', 'gpt 4.0 g04.txt', 'claude g04.txt')
generate_prompt_all()