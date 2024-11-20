import jsonlines
import sys
import torch
from transformers import AutoTokenizer, AutoModelForCausalLM, BitsAndBytesConfig

#####################################################
# Please finish all TODOs in this file for MP1;
# do not change other code/formatting.
#####################################################

def save_file(content, file_path):
    with open(file_path, 'w') as file:
        file.write(content)

def prompt_model(dataset, model_name = "deepseek-ai/deepseek-coder-6.7b-base", quantization = True):
    print(f"Working with {model_name} quantization {quantization}...")
    
    # TODO: download the model
    # davids17: referenced this notebook 
    # https://colab.research.google.com/drive/1ge2F1QSK8Q7h0hn3YKuBCOAS0bK8E0wf?usp=sharing
  
    if quantization:
        # TODO: load the model with quantization
        # davids17: I got this warning message: 
        # The `load_in_4bit` and `load_in_8bit` arguments are deprecated 
        # and will be removed in the future versions. 
        # Please, pass a `BitsAndBytesConfig` object in `quantization_config` argument instead.
        # Made the change to use `quantization_config` argument
        model = AutoModelForCausalLM.from_pretrained(
            pretrained_model_name_or_path=model_name,
            # load_in_4bit=True,
            device_map='auto',
            torch_dtype=torch.bfloat16,
            quantization_config=BitsAndBytesConfig(
                load_in_4bit=True,
                bnb_4bit_compute_dtype=torch.bfloat16,
                bnb_4bit_use_double_quant=True,
                bnb_4bit_quant_type='nf4'
            ),
        )
    else:
        # TODO: load the model without quantization
        model = AutoModelForCausalLM.from_pretrained(
            pretrained_model_name_or_path=model_name,
            load_in_4bit=False,
            torch_dtype=torch.bfloat16,
            device_map='auto'
        )
        
    tokenizer = AutoTokenizer.from_pretrained(model_name)

    # Configure model values - from MP1 instructions
    temperature = 0.00 # 0.0 throws an error
    max_length = 500
    
    results = []
    for case in dataset:
        prompt = case['prompt']
        
        # TODO: prompt the model and get the response
        # Tokenize prompt
        # input = tokenizer(prompt.format(user_question=prompt), return_tensors="pt").to('cuda')
        input = tokenizer(prompt, return_tensors="pt")
        # Generate the response from the model and decode output
        output = model.generate(**input, do_sample=False, max_length=max_length,temperature=temperature)
        response = tokenizer.decode(output[0], skip_special_tokens=True)
        
        print(f"Task_ID {case['task_id']}:\nPrompt:\n{prompt}\nResponse:\n{response}")
        results.append(dict(task_id=case["task_id"], completion=response))
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

if __name__ == "__main__":
    """
    This Python script is to run prompt LLMs for code synthesis.
    Usage:
    `python3 model_prompting.py <input_dataset> <model> <output_file> <if_quantization>`|& tee prompt.log

    Inputs:
    - <input_dataset>: A `.jsonl` file, which should be your team's dataset containing 20 HumanEval problems.
    - <model>: Specify the model to use. Options are "deepseek-ai/deepseek-coder-6.7b-base" or "deepseek-ai/deepseek-coder-6.7b-instruct".
    - <output_file>: A `.jsonl` file where the results will be saved.
    - <if_quantization>: Set to 'True' or 'False' to enable or disable model quantization.
    
    Outputs:
    - You can check <output_file> for detailed information.
    """
    args = sys.argv[1:]
    input_dataset = args[0]
    model = args[1]
    output_file = args[2]
    if_quantization = args[3] # True or False
    
    if not input_dataset.endswith(".jsonl"):
        raise ValueError(f"{input_dataset} should be a `.jsonl` file!")
    
    if not output_file.endswith(".jsonl"):
        raise ValueError(f"{output_file} should be a `.jsonl` file!")
    
    quantization = True if if_quantization == "True" else False
    
    dataset = read_jsonl(input_dataset)
    results = prompt_model(dataset, model, quantization)
    write_jsonl(results, output_file)
