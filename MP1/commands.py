###################################################################
# This is a list of all commands you need to run for MP1 on Colab.
###################################################################

# TODO: Update Your NetIDs in alphabetical order
# DONE: DS 9/01
NetIDs = ["atdoan2", "davids17", "divya7", "pf8"]
NetIDs_str = " ".join(NetIDs)

# TODO: Clone your GitHub repository
# DONE: DS 9/01 -- I left commented out 
# access_token = userdata.get('githubAccessToken')
# ! git clone https://{access_token}@github.com/atdoan2/CS598JBR-Team-1.git
# %cd CS598JBR-Team-1/

# Set up requirements for dataset generation
! bash -x MP1/setup_dataset.sh

# dataset generation
! python3 MP1/dataset_generation.py {NetIDs_str} |& tee dataset_generation.log

# TODO: Replace the file path of selected_humaneval_[seed].jsonl generated in previous step
# DONE: DS 9/01 -- Added seed
seed = "248264623217713294771470079546488913479"
input_dataset = "selected_humaneval_" + seed + ".jsonl"

# Set up requirements for model prompting
! bash -x MP1/setup_models.sh

base_with_quantization = "base_prompt_" + seed + ".jsonl"
instruct_with_quantization = "instruct_prompt_" + seed + ".jsonl"

# Prompt the models
! python3 MP1/model_prompting.py {input_dataset} "deepseek-ai/deepseek-coder-6.7b-base" {base_with_quantization} "True" |& tee base_prompt.log
! python3 MP1/model_prompting.py {input_dataset} "deepseek-ai/deepseek-coder-6.7b-instruct" {instruct_with_quantization} "True" |& tee instruct_prompt.log

# if you want to test run 
# python3 MP1/model_prompting.py selected_humaneval_248264623217713294771470079546488913479.jsonl deepseek-ai/deepseek-coder-6.7b-base test_run.jsonl True


# evaluate the results to get pass@k
! evaluate_functional_correctness {base_with_quantization} |& tee base_evaluate.log
! evaluate_functional_correctness {instruct_with_quantization} |& tee instruct_evaluate.log

%cd ..

# git push all nessacery files (e.g., *jsonl, *log) to your GitHub repository
