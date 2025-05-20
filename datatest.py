from itertools import combinations
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

def export_csv(df):
    df.to_csv('combinations.csv', index=False)


participants = ['gpt4o', 'claude', 'gemini 2.0', 'llama2']
combinations_df = generate_combinations(participants)

print(combinations_df)
export_csv(combinations_df)