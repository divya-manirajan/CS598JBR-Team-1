import jsonlines
import sys
import torch
from transformers import AutoTokenizer, AutoModelForCausalLM, BitsAndBytesConfig
import os
import utils

#####################################################
# Please finish all TODOs in this file for MP3/task_1;
#####################################################

def save_file(content, file_path):
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(content)

def prompt_model(dataset, model_name = "deepseek-ai/deepseek-coder-6.7b-instruct", 
                 vanilla = True, 
                 LOCAL = False, 
                 ANALYSIS_ONLY = False,
                 run_size = 1):
    global java_dataset # meh...
    print(f"Working with {model_name} prompt type is vanilla = {vanilla}...")
    
    # TODO: download the model ==> DONE
    # TODO: load the model with quantization ==> DONE
    if not LOCAL:
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
    else:
        # we use ollama locally for testing
        pass
        
    results = []
    for entry in dataset[:run_size]:
        # TODO: create prompt for the model ==> DONE
        # Tip : Use can use any data from the dataset to create 
        #       the prompt including prompt, canonical_solution, test, etc.
        
        print("------------------------")
        # Load prompt from text file

        prompt, DELIMS = utils.get_prompt(entry, vanilla, task = 1)
        
        # TODO: prompt the model and get the response ==> DONE
        if not LOCAL:
            model_input = tokenizer(prompt, return_tensors="pt").to("cuda")
            output = model.generate(
                **model_input,
                do_sample=False,
                max_new_tokens=1024,
                temperature=0.0,
                # stop_strings=["[/Output]"],
                # tokenizer=tokenizer,
            )
            response = tokenizer.decode(output[0], skip_special_tokens=True)
        else:
            response = ollama.generate(model='deepseek-coder:6.7b', prompt=prompt)['response']
        
        # we need to get the extract the java from the response and save to a file
        java_main = utils.get_java_code(response, java_dataset, entry, DELIMS, vanilla)
        java_dir = f'java/{entry["task_id"]}/'
        save_file(java_main, java_dir+'Main.java')
        java_run_result = utils.run_java(java_dir)
        compile_result = java_run_result[0]
        run_result = java_run_result[1]
        java_output = utils.java_output(entry["task_id"], compile_result, run_result)
        save_file(java_output, java_dir+'output.log')
        
        # TODO: process the response and save it to results ==> DONE
        verdict = java_run_result[1].returncode == 0
        compiled = compile_result.returncode == 0
        ran = run_result.returncode == 0

        print(f"Task_ID {entry['task_id']}:\n \
              prompt:\n{prompt}\n \
              response: \n {response}\n \
              java_code: \n{java_main}\n \
              compile_result: \n{compile_result}\n \
              run_result: \n{run_result}\n \
              is_expected:\n{verdict} \n \
              End of Task_ID {entry['task_id']}\n")
        results.append({
            "task_id": entry["task_id"],
            "prompt": prompt,
            "response": response,
            "java_code": java_main,
            "compiled": compiled,
            "ran": ran,
            "is_correct": verdict
        })
        
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
    This Python script is to run prompt LLMs for code translation.
    Usage:
    `python3 task_1.py <input_dataset> <model> <output_file> <if_vanilla>`|& tee prompt.log

    Inputs:
    - <input_dataset>: A `.jsonl` file, which should be your team's dataset containing 20 HumanEval problems.
    - <model>: Specify the model to use. Options are "deepseek-ai/deepseek-coder-6.7b-base" or "deepseek-ai/deepseek-coder-6.7b-instruct".
    - <output_file>: A `.jsonl` file where the results will be saved.
    - <if_vanilla>: Set to 'True' or 'False' to enable vanilla prompt
    
    Outputs:
    - You can check <output_file> for detailed information.
    """
    # LOCAL = True, this will run ollama
    # 
    # ANALYSIS_ONLY = True, run analysis only, and not run the model prompt
    # (use output file from previous run)
    #
    # RUN_SIZE = x, run only x+1 entry for testing
    
    # hard coding these for now
    ANALYSIS_ONLY = False
    seed = "248264623217713294771470079546488913479"
    input_java_dataset = "selected_humanevalx_java_" + seed + ".jsonl"
    
    args = sys.argv[1:]
    LOCAL = False
    print(args)
    try:
        input_dataset = args[0]
    except:
        LOCAL = True
        import ollama
        input_python_dataset = "selected_humanevalx_python_" + seed + ".jsonl"
        input_dataset = input_python_dataset
        output_file = "LOCAL_run_task_1.jsonl"
        model = "Ollama Local deepseek-coder:6.7b"
        if_vanilla = "True"
    else:
        model = args[1]
        output_file = args[2]
        if_vanilla = args[3] # True or False

    # correct dir when running without being called by script
    if "MP3" not in os.getcwd(): 
        os.chdir('MP3')   
    if not input_dataset.endswith(".jsonl"): raise ValueError(f"{input_dataset} should be a `.jsonl` file!")
    if not output_file.endswith(".jsonl"): raise ValueError(f"{output_file} should be a `.jsonl` file!")
    
    vanilla = True if if_vanilla == "True" else False
    
    dataset       = read_jsonl(input_dataset)
    java_dataset  = read_jsonl(input_java_dataset)
    
    RUN_SIZE = 1 # run 1 for testing
    RUN_SIZE = len(dataset) # run all
    
    # create directories for java main class files
    # only needed to run once
    # had to hand make java/HumanEval directory first
    # for entry in dataset:
    #    os.mkdir(f'java/{entry["task_id"]}')
    
    results = prompt_model(dataset, model, vanilla, LOCAL, ANALYSIS_ONLY, RUN_SIZE)
    print("Accuracy:", utils.accuracy(results))
    write_jsonl(results, output_file)
