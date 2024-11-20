Deadlines: September 17th, 2024 (Team Making) and September 26th, 2024 (Submitting Deliverables)

[submission time is 11:59 pm of the deadline day]

Overview: This course consists of three integrated MPs, i.e., MPs are connected, and what you do in MP1 is required for MP2 and MP3. In the first MP, you will create a team of at most four members with whom you will work on the project. You will also prepare the GitHub repository and Google Colab workspace to prompt an open-source code language model.

Deliverables: Please follow the tasks explained under the “Tasks” section to (1) make your team, (2) set up your GitHub and Google Colab workspace, and (3)  load a Code LLM on Google Colab and prompt it for code synthesis. The deliverables are highlighted in purple under each task with their corresponding points. You should create a GitHub repository and Google Colab notebook, write a code to load/prompt a Code LLM for program synthesis, and write your observation in a progress report.

Grading rubric: Please find the rubric below.

Activity
	

Points

Task 1
	

15 points

Task 2
	

20 points

Task 3
	

20 points

Task 4
	

155 points

Total
	

210 points

Tasks:

<<1- Team Making>>

We expect you to do the project as a team. You can team up with your friends taking the course, the folks sitting next to you in the class (to make new friends!), or whoever you prefer otherwise. Groups should not include more than four people. Members who are part of the team on 09/17 would be considered the final team (unless you got any direction from the instruction team).

Deliverables for Task 1: 

    You should self-sign up for your team using Canvas (deadline 09/17 with no exception):

https://canvas.illinois.edu/courses/48884/assignments/1051187 [10 points]

    Access and copy the progress report template from https://www.overleaf.com/read/zqyfntftqdgx#d9e3c0. You should include the team members' first name, last name, and NetID in your copy of the progress report. [5 points]

Important Note: We highly encourage you to schedule a weekly meeting with your team members to make steady progress on the MPs. While you have time until the deadline, start early and ask for help early! Also note that you are going to use shared GPUs on Google Colab, which may not be available if you start working on the MP a day before the deadline. All team members are expected to work together. If your team member is not contributing, please inform the teaching staff (instructor and TA) by creating a private Campuswire post as soon as possible. The instruction team will try to contact the inactive team members and resolve the issue. Inactive students will lose 50%--100% of the team's grade for the MP.

Important Note: Please be professional and responsible to others. If you want to drop the course, let the team members know immediately, even if you do drop it later. If a team has less than two members, the remaining student should reach out to the instruction team immediately so that we can move them to other teams.  

<<2- Setting Up The Environment>>

We will use GitHub repositories to maintain the code and datasets and Google Colab to access computing resources (GPUs). Please note that Google Colab is a shared resource platform: you can access the resources upon availability. Our instruction team has tested availability at different times, and this should be fine if you plan to do the MPs ahead of deadlines. Given that MPs are available several weeks before the deadline, we accept no excuse for the unavailability of the resources. Alternatively, you can buy resources to ensure their availability (this is not required for MPs).

<<Google Colab>>

Create a Google Colab notebook (you should use your @illinois email). The notebook's name should be CS598JBR-Team-[team number]. For example, if you are Team-2, your repository name would be `CS598JBR-Team-2`. Invite all the team members, the instructor, and TAs to that notebook: reyhaneh@illinois.edu, yangc9@illinois.edu, vp35@illinois.edu

We will use GPUs to load the models. Under the Runtime setting (Runtime -> Change Runtime), you can choose the computing resource (CPU or GPU). Follow the instructions and select the “T4 GPU.” The best practice for avoiding resource loss is to click on the “Disconnect and delete runtime” option under the File menu when you are not using your notebook or change the runtime to “CPU” when you are not loading and prompting the model. Failing to manage resources properly impacts your access to GPUs. We have marked the subtasks that you need GPU to do them. So, release the GPUs for other tasks.

                                                                                     

<<GitHub Repository>>

Create a new private GitHub repo by following the structure of this repository: https://github.com/Intelligent-CAT-Lab/CS598JBR-Team-0

Your repo should be named CS598JBR-Team-[team number]. For example, if you are Team-2, your repository name would be CS598JBR-Team-2.

Update the ReadMe of your repo (do not override the format of ReadMe, but just replace the content):

    List of your team members
    The link to the Google Colab notebook

Invite the instructor and TAs to that repository as collaborators.

    Our GitHub IDs are reyhanslab, lalayang, and vp35-illinois-edu

Copy the contents of the commands.py file under the MP1 directory into your Colab notebook. You must replace the placeholders, such as links to the GitHub repo and NetIDs.

Deliverables for Task 2: 

    Include the links to the GitHub repo and the Google Colab in the progress report. [10 points each, total 20 points]

<<3- Constructing Evaluating Dataset>>

HumanEval is a widely used dataset for evaluating LLMs' code synthesis abilities. It includes 164 Python problem descriptions and ground-truth implementations. To work with this dataset, you must install a series of dependencies. Please set up these dependencies in the notebook by running the setup_dataset.sh script under the MP1 directory of the cloned GitHub repo.

Each team will work on a unique dataset of 20 problems from the HumanEval dataset. We have developed a script that takes the NetID of all group members as input and selects a unique subset of HumanEval that the team should work on. This script (dataset_generation.py) is under the MP1 directory of the cloned GitHub repo. The commands.py file already contains the command to run this script; all you need to do is replace NetIDs.

Execution of this script generates a log file (dataset_generation.log) as well as the dataset of 20 problems you need to work with in all MPs as a form of JSON file (selected_humaneval_[seed].jsonl). Each team's seed number is unique and generated based on the given NetIDs.

Deliverables for Task 3: 

    Upload the following files to your GitHub repo under the MP1 directory:

    selected_humaneval_[seed].jsonl (your file name should include the generated seed number) [10 points]
    dataset_generation.log [10 points]

Important Note: Modifying the generated subset or using another team's seed number is plagiarism. Students plagiarizing will lose all MP1 points and receive a one-letter grade drop.

Important Note: We have an automated grading script. If you fail to follow the instructions, the autograder will give you ZERO. We do not accept re-grading if you fail to follow the instructions.

<<4- Code LLM Loading and Prompting>>

We will use DeepSeekCoder-6.7b-base and DeepSeekCoder-6.7b-instruct as the Code LLM in all MPs. Get familiar with the DeepSeekCoder model at https://github.com/deepseek-ai/DeepSeek-Coder. Using this model requires installing several dependencies. Please set up these dependencies in the notebook by running the setup_models.sh script under the MP1 directory of the clones GitHub repo.

After installing the dependencies, you can start loading the Code LLM for inference/prompting. To that end, you must complete the model_prompting.py file under the MP1 at the specified placeholders. Do not change the name of the methods, the input-output format of the file, or model names, as this can interfere with our autograder.

4.1- Downloading and loading the model on the GPU (needs GPU): Colab GPUs are not big enough to load a 7B model like DeepSeekCoder. To that end, we will use QLoRA, a quantization technique that enables loading large models into smaller computing resources by modifying the model’s precision. Read the instructions provided in the ReadMe of the QLoRA GitHub repository and implement the code for downloading (find the comment #TODO: download the model) and loading the model with (find the comment #TODO: load the model with quantization) and without (find the comment #TODO: load the model without quantization) quantization in the model_prompting.py at the places identified by the comments in the code. You should use “temperature 0” as a model setting. Otherwise, we cannot reproduce your results using our autograder, and you will lose points. We also do not require you to run experiments “without quantization.” However, you can try to see what happens if you load a model without quantization on a notebook. You can use the max_length value as 500 and torch_dtype as torch.bfloat16.

4.2- Prompting the model (needs GPU): After loading the model, you should prompt the model under the following settings:

    Load DeepSeekCoder-6.7b-base with quantization to synthesize all 20 problems in your dataset.
    Load DeepSeekCoder-6.7b-instruct with quantization to synthesize all 20 problems in your dataset.

Follow the HumanEval ReadMe instructions to understand the dataset's structure and how to prompt a given model for code synthesis. Implement the code to prompt the Code LLM in the model_prompting.py (find the comment #TODO: prompt the model and get the response). After finishing the implementation, you can use the commands provided to load and prompt the model under the mentioned setting, which will provide you with two JSON files: base_prompt_[seed].jsonl (results of loading and prompting the base model) and instruct_prompt_[seed].jsonl (results of loading and prompting the instruction-tuned model). It also generates two log files: base_prompt.log and instruct_prompt.log.

4.3- Evaluating the model response: After getting the model response for synthesizing 20 problems, you should run the generated code against existing tests in the HumanEval benchmark. This can be done by running the last series of provided commands in the commands.py file, which provides two outputs (base_prompt.jsonl_results.jsonl and instruct_prompt.jsonl_results.jsonl) and two log files (base_evaluate.log and instruct_evaluate.log). You will see the pass@k number for the entire dataset and an individual verdict for a problem in the dataset, i.e., whether the synthesized code passes the existing tests or not. 

Deliverables for Task 4: 

    Upload the following files to your GitHub repo under the MP1 directory:

    base_prompt_[seed].jsonl (your file name should include the generated seed number) [10 points]
    base_prompt.jsonl_results.jsonl (your file name should include the generated seed number) [20 points]
    instruct_prompt_[seed].jsonl (your file name should include the generated seed number) [10 points]
    instruct_prmpt.jsonl_results.jsonl (your file name should include the generated seed number) [20 points]
    base_prompt.log [10 points]
    instruct_prompt.log [10 points] 
    base_evaluate.log [10 points]
    instruct_evaluate.log [10 points]

    Update section MP1 of the progress report with the following information:

    What is pass@k metric? [5 points]
    pass@1 values under the two different settings [5 points each, total 10 points]
    A table showing the pairwise comparison of the pass/fail result for each of the 20 programs in your dataset under two different settings [40 points]

Validation script: We have designed a validation script to ensure that you have followed the instructions and preserved the naming and structure of the files. Passing the validation script only shows that our grading script could proceed to grading, and you will not get a 0 if you change the naming and structure. You may pass the validation script but not get all the MP points. You can use validate.py script under the MP1 directory of the clones GitHub repo to validate the structure of the deliverables.

