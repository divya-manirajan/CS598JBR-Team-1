import jsonlines
import sys
import torch
from transformers import AutoTokenizer, AutoModelForCausalLM, BitsAndBytesConfig
import random
import re
import ast

#####################################################
# Please finish all TODOs in this file for MP2;
#####################################################
def save_file(content, file_path):
    with open(file_path, "w") as file:
        file.write(content)


def make_prompts(dataset, vanilla=True):
    """Handles the creation of the prompts given the dataset with logic to use vanilla/detailed prompting.

    Args:
        dataset: The object that contains the data needed to parse through for prompt engineering.
        vanilla: Boolean value to determine whether to use vanilla prompting or not.

    Returns:
        Object with the the task_id, the updated prompt, response, and is_correct to be handled by the LLM.
    """
    res = []

    input_pattern = re.compile(r"assert\s*?(?:not)?\s+candidate\((.*?)\)")
    random.seed(42)

    for entry in dataset:
        test_inputs = input_pattern.findall(entry["test"])
        random_input, random_example = random.sample(test_inputs, 2)
        solution = entry["prompt"] + entry["canonical_solution"]

        if entry["task_id"] == "HumanEval/132" and random_input == "('[]'":
            random_input = "('[]')"

        if entry["task_id"] == "HumanEval/132" and random_example == "('[]'":
            random_example = "('[]')"

        if entry["task_id"] == "HumanEval/55":
            matches = re.findall(
                r"assert\s+candidate\((.*?)\)\s*==\s*(.*)", entry["test"]
            )
            random_match, second_match = random.sample(matches, 2)
            random_input = random_match[0]
            expected_output = random_match[1]
            random_example = second_match[0]
            example_output = second_match[1]

        else:
            exec(solution)
            expected_output = eval(entry["entry_point"] + "(" + str(random_input) + ")")
            example_output = eval(
                entry["entry_point"] + "(" + str(random_example) + ")"
            )

        solution_without_docstring = re.sub(
            r'("""|\'\'\')\s*.*?\s*("""|\'\'\')', "", solution, flags=re.DOTALL
        )

        if vanilla:
            prompt = f"""If the input is {random_input}, what will the following code return? {solution_without_docstring} Enclose your prediction between [Output] and [/Output] tags like so: [Output]prediction[/Output]\n\n"""
        else:
            prompt = (
                f"You are an AI programming assistant, utilizing the DeepSeek Coder model, developed by DeepSeek Company.\n\n"
                f"## Instructions:\n"
                f"Please perform the following steps below.\n"
                f"1. Using the provided function and input, read through the entire function and input text carefully.\n"
                f"2. Walk through step-by-step the thoughts of each line in the function.\n"
                f"3. Your response must ALWAYS include predicted output at the END, which must ALWAYS be enclosed between "
                f"[Output][/Output] tags like so: [Output]prediction[/Output]. Inside the [Output][/Output] tag, the response "
                f"should not include any new line or extra spaces than what the prediction needs.\n\n"
                f"##Function: {solution}\n\n"
                f"##Input: {random_input}\n\n"
                f"##Response: "
            )

        res.append(
            {
                "task_id": entry["task_id"],
                "prompt": prompt,
                "response": None,
                "is_correct": None,
                "expected_output": expected_output,
            }
        )
    return res


def prompt_model(
    dataset, model_name="deepseek-ai/deepseek-coder-6.7b-instruct", vanilla=True
):
    print(f"Working with {model_name} prompt type {vanilla}...")
    # TODO: download the model - DONE
    # TODO: load the model with quantization - DONE
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForCausalLM.from_pretrained(
        pretrained_model_name_or_path=model_name,
        load_in_4bit=True,
        device_map="auto",
        torch_dtype=torch.bfloat16,
        quantization_config=BitsAndBytesConfig(
            load_in_4bit=True,
            bnb_4bit_compute_dtype=torch.bfloat16,
            bnb_4bit_use_double_quant=True,
            bnb_4bit_quant_type="nf4",
        ),
    )

    results = []
    prompts = make_prompts(dataset, vanilla)
    for prompt in prompts:
        model_input = tokenizer(prompt["prompt"], return_tensors="pt").to("cuda")
        # TODO: prompt the model and get the response - DONE
        output = model.generate(
            **model_input,
            do_sample=False,
            max_new_tokens=1000,
            # stop_strings=["[/Output]"],
            # tokenizer=tokenizer,
        )
        response = tokenizer.decode(output[0], skip_special_tokens=True)

        # TODO: process the response and save it to results - DONE
        output = re.findall(r"\[Output\](.*?)\[/Output\]", response, re.DOTALL)
        if output:
            formatted_output = str(output[-1]).strip("\n ")
            verdict = formatted_output == str(prompt["expected_output"]) or str(
                # Try swapping single and double quotes.
                formatted_output.translate({34: 39, 39: 34})
            ) == str(prompt["expected_output"])
        else:
            raise ValueError(f"{response} is naughty.")

        print(
            f"Task_ID {prompt['task_id']}:\nprompt:\n{prompt['prompt']}\nresponse:\n{response[len(prompt['prompt']):-1]}\nparsed output:\n{output[-1]}\nexpected_output:\n{prompt['expected_output']}\nis_correct:\n{verdict}"
        )
        results.append(
            {
                "task_id": prompt["task_id"],
                "prompt": prompt["prompt"],
                "response": response[len(prompt["prompt"]) : -1],
                "is_correct": verdict,
            }
        )

    return results


def read_jsonl(file_path):
    dataset = []
    with jsonlines.open(file_path) as reader:
        for line in reader:
            dataset.append(line)
    return dataset


def write_jsonl(results, file_path):
    with jsonlines.open(file_path, "w") as f:
        for item in results:
            f.write_all([item])


def accuracy(results):
    """Compute proportion of results that are correct."""
    total_count = len(results)
    correct_count = 0

    for result in results:
        if result["is_correct"]:
            correct_count += 1

    return correct_count / total_count


if __name__ == "__main__":
    """
    This Python script is to run prompt LLMs for code synthesis.
    Usage:
    `python3 Task_1.py <input_dataset> <model> <output_file> <if_vanilla>`|& tee prompt.log

    Inputs:
    - <input_dataset>: A `.jsonl` file, which should be your team's dataset containing 20 HumanEval problems.
    - <model>: Specify the model to use. Options are "deepseek-ai/deepseek-coder-6.7b-base" or "deepseek-ai/deepseek-coder-6.7b-instruct".
    - <output_file>: A `.jsonl` file where the results will be saved.
    - <if_vanilla>: Set to 'True' or 'False' to enable vanilla prompt

    Outputs:
    - You can check <output_file> for detailed information.
    """
    args = sys.argv[1:]
    input_dataset = args[0]
    model = args[1]
    output_file = args[2]
    if_vanilla = args[3]  # True or False

    if not input_dataset.endswith(".jsonl"):
        raise ValueError(f"{input_dataset} should be a `.jsonl` file!")

    if not output_file.endswith(".jsonl"):
        raise ValueError(f"{output_file} should be a `.jsonl` file!")

    vanilla = True if if_vanilla == "True" else False

    dataset = read_jsonl(input_dataset)
    results = prompt_model(dataset, model, vanilla)

    print("Accuracy:", accuracy(results))

    write_jsonl(results, output_file)
