from itertools import combinations
import os
import pandas as pd


def generate_prompt(plantuml_a, plantuml_b, context_file):
    input_dir = 'data'

    # read the context file
    with open(os.path.join(input_dir, context_file), 'r', encoding='utf-8') as file:
        context_content = file.read()

    # read the PlantUML files
    with open(os.path.join(input_dir, plantuml_a), 'r', encoding='utf-8') as file:
        plantuml_a_content = file.read()

    with open(os.path.join(input_dir, plantuml_b), 'r', encoding='utf-8') as file:
        plantuml_b_content = file.read()

    prompt = f"""
    Role: You are a strict evaluator of UML class diagrams written in PlantUML. Compare two candidate diagrams (A and B) against the given Context.
    Context:
    {context_content}
    
    PlantUML result A: 
    {plantuml_a_content}
    
    PlantUML result B: 
    {plantuml_b_content}

    Evaluation rules:
    - Consider only UML class diagram semantics (eg. classes, attributes, associations, multiplicities, generalisation, composition/aggregation). 
    - Ignore layout, styling, skinparams, comments, and notes. 
    - Treat the Context as authoritative; do not invent entities or relationships not present there.

    Decision criteria (in priority order):
    1. Correct domain classes and relationships
    2. Correct associations/multiplicities
    3. Appropriate attributes and types
    4. Terminology alignment
    5. UML class diagram conformance

    Evaluation Scores:
    Assign a score from 1-5 for each criterion when comparing and evaluating the two models. The scoring must strictly adhere to the metrics below, while following the evaluation rules and decision criteria.



    Evaluation Metrics:

    1. Appropriate conceptual classes aligned with the domain

    1 - Very Poor: Classes are mostly incorrect or irrelevant and do not accurately represent the domain.
    2 - Poor: Only a few classes are correct, but the majority of the domain concepts are missing or incorrect. 
    3 - Fair: Some classes are correctly identified, but noticeable misalignments are still present.
    4 - Good: Most classes are correctly identified with only minor misalignments
    5 - Excellent: All classes are correctly identified, fully aligned with the domain. 

    2. Associations/Multiplicities between classes for domain reasoning 
    1 - Very Poor: Associations/multiplicities are largely missing or incorrect, comprising domain reasoning. 
    2 - Poor: Few correct associations/multiplicities with critical relationships missing. 
    3 - Fair: Some associations/multiplicities are correct, but noticeable missing or misrepresentations remain. 
    4 - Good: Most associations/multiplicities are correctly identified with only minor errors. 
    5 - Excellent: All essential associations/multiplicities correctly applied.

    3. Model attributes with appropriate data types
    1 - Very Poor: Attributes and data types are poorly identified and modeled; largely incorrect or irrelevant.
    2 -  Poor: Few attributes are correct with proper types; critical attributes are missing.
    3 - Fair: Some attributes are correct with proper types, but significant attributes are still missing.
    4 - Good: Most attributes are appropriately modeled with proper data types; minor type issues may exist.
    5 - Excellent: All attributes are correctly modeled with appropriate data types.

    4. Consistencies of Terminology with given context
    1 - Very Poor: Terminology is largely inconsistent with the given context 
    2 - Poor: Frequent inconsistencies; critical terms misused or missing. 
    3 - Fair: Some terminology is correct, but noticeable inconsistencies remain. 
    4 - Good: Most terminology aligns with the given context, with minor inconsistencies. 
    5 - Excellent: Terminology is fully consistent with the given context. 

    5. Adherence of UML class diagram standards 
    1 – Very Poor: Poor diagram formation with major UML standards ignored, making it largely incomprehensible.
    2 – Poor: Frequent UML violations; diagram is difficult to interpret.
    3 – Fair: Some UML/PlantUML syntax errors, but major representations are still missing. 
    4 – Good: Minor UML/PlantUML notation errors; overall diagram remains understandable.
    5 – Excellent: Fully adheres to UML/PlantUML syntax, notation, and conventions.


    Return only:
    Winner: A | B 
    Justification: 2–4 concise sentences citing concrete elements from A and B, and includes the scores assigned to the 5 criteria listed above.

    """
    return prompt


lead_text = "pacemaker"
evaluating_datasets = [f'{lead_text}-claude.txt', f'{lead_text}-gemini.txt',
                       f'{lead_text}-gpt5.txt', f'{lead_text}-llama3.1.txt']
context_file = f'{lead_text}.txt'


def generate_prompt_all():
    """Generate all possible combinations of PlantUML files and save prompts to data_fixed folder"""
    output_dir = f'data_fixed/{lead_text}'
    os.makedirs(output_dir, exist_ok=True)

    # generate all combinations
    for plantuml_a, plantuml_b in combinations(evaluating_datasets, 2):
        print(f"Generating prompt for: {plantuml_a} vs {plantuml_b}")

        # gnerate the prompt
        prompt_content = generate_prompt(plantuml_a, plantuml_b, context_file)

        # create output filename
        base_a = os.path.splitext(plantuml_a)[0]
        base_b = os.path.splitext(plantuml_b)[0]
        out_name = f'{base_a} vs {base_b}.txt'
        out_path = os.path.join(output_dir, out_name)

        # save the prompt to file
        with open(out_path, 'w', encoding='utf-8') as file:
            file.write(prompt_content)

        print(f"saved prompt to: {out_path}")


if __name__ == "__main__":
    # generate the combinations CSV

    # generate all prompts and save to data_fixed folder
    generate_prompt_all()

    print("done")
