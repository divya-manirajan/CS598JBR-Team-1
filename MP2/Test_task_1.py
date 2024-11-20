import jsonlines
import json
import random
import re

def read_jsonl(file_path):
    dataset = []
    with jsonlines.open(file_path) as reader:
        for line in reader:
            dataset.append(line)
    return dataset

input_dataset = "MP1/selected_humaneval_248264623217713294771470079546488913479.jsonl"# selected_humaneval_[seed].jsonl
dataset = read_jsonl(input_dataset)

def prompt_model(dataset, vanilla = True):
    input_output_pattern = r"assert\s+candidate\((.*?)\)\s*==\s*(.*)"

    for entry in dataset:
        
        # Extract all inputs from the test cases using regex
        test_inputs = re.findall(input_output_pattern, entry['test'])
        
        if test_inputs:
            # Choose a random input from the extracted list
            random_input, expected_output = random.choice(test_inputs)
            #print(f"Random Input for Task {entry['task_id']}:\n{random_input}")
            prompt = f"""You are an AI programming assistant. You are an AI programming assistant, utilizing the DeepSeek Coder model, developed by DeepSeek Company, and you only answer questions related to computer science.
For politically sensitive questions, security and privacy issues, and other non-computer science questions, you will refuse to answer. 
### Instruction:
If the input is {random_input}, what will the following code return?
The return value prediction must be enclosed between [Output] and [/Output] tags. For example : [Output]prediction[/Output]
{"Think step by step." if not vanilla else ""}
{entry['canonical_solution']}
### Response
"""
        else:
            print(f"No test inputs found for Task {entry['task_id']}")
        
        print("="*40)

        print(f"Task_ID {entry['task_id']}:\nprompt:\n{prompt}\nexpected response: {expected_output}")



prompt_model(dataset)

