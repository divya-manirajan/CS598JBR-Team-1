**Deadline: October 22nd, 2024**
[Estimated amount of time for finishing this MP: 20 hours]

# Overview:
This milestone aims to explore DeepSeekCoder's programming abilities and craft the prompt that it responds to best on code-related tasks. You will use the unique subset of HumanEval generated in the previous milestone.

# Deliverables:
Please follow the tasks explained under the “Tasks” section. You must upload all the deliverables to your GitHub Repository and submit the progress report in a PDF file on Canvas. The overall list of deliverables is below (more details under each task):
- Your prompts and DeepSeekCoder’s response to your prompts (should be stored on the GitHub repository as instructed)
- Your code/scripts to automatically generate and/or craft the prompts checked into the GitHub repository
- Your reflections on code-related prompt engineering in the progress report

# Grading rubric:
Please find the rubric below.
| Activity                          | Points |
|-----------------------------------|--------|
| Task 1 (code execution reasoning) | 200    |
| Task 2 (test generation)          | 260    |
| Total                             | 460    |

We will use GitHub to maintain the code and datasets and Google Colab to access computing resources (GPUs), which you should already set up in MP1. Please note that Google Colab is a shared resource platform: you can access the resources upon availability. Our instruction team has tested availability at different times, and this should be fine if you plan to do the MPs ahead of deadlines. Given that MPs are available several weeks before the deadline, we accept no excuse for the unavailability of the resources. Alternatively, you can buy resources to ensure their availability (this is not required for MPs) or use alternative resources if you can access them.

Please go to https://github.com/Intelligent-CAT-Lab/CS598JBR-Team-0 and copy the “MP2” directory. Similar to MP1, you should modify some existing files under this directory and upload additional files as a result of performing the task. You should use the same dataset generated in MP1, which includes a unique set of 20 problems for your group. We will use DeepSeekCoder-instruct for MP2 and MP3, which performs better than the base model.

You can read about prompt engineering/crafting/refining at https://docs.cohere.ai/docs/prompt-engineering. Overall, a prompt provides instructions to language models such as DeepSeekCoder for performing a task, and they provide a response that best matches the prompt. Research and practice have shown that providing more relevant context in the prompt can result in better responses. Crafting the prompt and providing the context that results in the best answer is called prompt engineering (also known as prompt crafting or prompt refining). Each model has a specific way of prompting, closely related to how it is pre-trained or instruction-tuned. Read the instructions available on the  DeepSeekCoder GitHub repo carefully to ensure you properly prompt the model. Otherwise, you may observe poor performance in the model.

# Tasks:

## <<1- Code Execution Reasoning>>

You must complete MP2/commands.py and MP2/task_1.py files under the “MP2” directory.

Each program in the HumanEval dataset comes with at least one test input and its corresponding correct output. In this task, you should select only one of the tests per program and do the experiments with that (note that, given a program P, LLMs may correctly predict the output of input X for this program but incorrectly predict the output for another input, Y. Here, we care about improvements as much as you can, and do not compare teams with each other). That is, you have 20 programs and 20 test inputs/expected outputs, which you will use to evaluate the code execution reasoning of LLMs. For example, consider the HumanEval problem 132 ("task_id": "HumanEval/132") that is shown below:
```json
{
  "task_id": "HumanEval/132",
  "prompt": "\ndef is_nested(string):\n    '''\n    Create a function that takes a string as input which contains only square brackets.\n    The function should return True if and only if there is a valid subsequence of brackets \n    where at least one bracket in the subsequence is nested.\n\n    is_nested('[[]]') ➞ True\n    is_nested('[]]]]]]][[[[[]') ➞ False\n    is_nested('[][]') ➞ False\n    is_nested('[]') ➞ False\n    is_nested('[[][]]') ➞ True\n    is_nested('[[]][[') ➞ True\n    '''\n",
  "canonical_solution": "    opening_bracket_index = []\n    closing_bracket_index = []\n    for i in range(len(string)):\n        if string[i] == '[':\n            opening_bracket_index.append(i)\n        else:\n            closing_bracket_index.append(i)\n    closing_bracket_index.reverse()\n    cnt = 0\n    i = 0\n    l = len(closing_bracket_index)\n    for idx in opening_bracket_index:\n        if i < l and idx < closing_bracket_index[i]:\n            cnt += 1\n            i += 1\n    return cnt >= 2\n\n    \n",
  "test": "def check(candidate):\n\n    # Check some simple cases\n    assert candidate('[[]]') == True, \"This prints if this assert fails 1 (good for debugging!)\"\n    assert candidate('[]]]]]]][[[[[]') == False\n    assert candidate('[][]') == False\n    assert candidate(('[]')) == False\n    assert candidate('[[[[]]]]') == True\n    assert candidate('[]]]]]]]]]]') == False\n    assert candidate('[][][[]]') == True\n    assert candidate('[[]') == False\n    assert candidate('[]]') == False\n    assert candidate('[[]][[') == True\n    assert candidate('[[][]]') == True\n\n    # Check some edge cases that are easy to work out by hand.\n    assert candidate('') == False, \"This prints if this assert fails 2 (also good for debugging!)\"\n    assert candidate('[[[[[[[[') == False\n    assert candidate(']]]]]]]]') == False\n\n",
  "entry_point": "is_nested"
}
```
The JSON file for this problem contains (1) task_id, (2) prompt, (3) cannonical_solution, and (4) test. Each test is shown as an assertion, e.g., “assert candidate('[]]]]]]][[[[[]') == False.” You need to randomly select one assertion, extract the inputs (highlighted in yellow) and expected output (highlighted in red), and use it for this task.

For “vanilla prompting,” which is the simplest way to ask the model for a task, you can start with the following example (the prompt is highlighted in purple, and the model’s response is highlighted in green):

------

The following program's input from the HumanEval dataset is “[]]]]] [[[[[[]],” and the expected output is “False.” Please see how we formed a prompt with this information.

```
You are an AI programming assistant. You are an AI programming assistant, utilizing the DeepSeek Coder model, developed by DeepSeek Company, and you only answer questions related to computer science. For politically sensitive questions, security and privacy issues, and other non-computer science questions, you will refuse to answer.
### Instruction:
If the string is ‘[]]]]]]][[[[[]’, what will the following code return?
The return value prediction must be enclosed between [Output] and [/Output] tags. For example : [Output]prediction[/Output]

def is_nested(string):
	opening_bracket_index = []
	closing_bracket_index = []
	for i in range(len(string)):
		if string[i] == '[':
			opening_bracket_index.append(i)
		else:
			closing_bracket_index.append(i)
	closing_bracket_index.reverse()
	cnt = 0
	i = 0
	l = len(closing_bracket_index)
	for idx in opening_bracket_index:
		if i < l and idx < closing_bracket_index[i]:
			cnt += 1
			i += 1
	return cnt >= 2

### Response:
```
```
[Output]True[\Output]
```

In the above example, DeepSeekCoder fails to reason about the code execution and correctly predict the output. You should do prompt engineering to improve its performance, i.e., provide more context to see if this can help the model produce a better result. Such contexts include an in-context example, modifying the natural language instruction to help the model better understand the problem, asking the model to reason about the process step by step, etc. Be creative :)

You can see an example of the enhanced prompt below, which asks the model to perform step-by-step reasoning (Chaing of Thought). We can see that just by asking the model to think and solve the problem step by step, it can now predict the output correctly. Note that just asking the model to reason step by step is not enough for many problems, so, you should explore how to improve the prompts in other ways.

```
You are an AI programming assistant. You are an AI programming assistant, utilizing the DeepSeek Coder model, developed by DeepSeek Company, and you only answer questions related to computer science. For politically sensitive questions, security and privacy issues, and other non-computer science questions, you will refuse to answer.
### Instruction:
If the string is ‘[]]]]]]][[[[[]’, what will the following code return?
The return value prediction must be enclosed between [Output] and [/Output] tags. For example : [Output]prediction[/Output].
Reason step by step to solve the problem.

def is_nested(string):
	opening_bracket_index = []
	closing_bracket_index = []
	for i in range(len(string)):
		if string[i] == '[':
			opening_bracket_index.append(i)
		else:
			closing_bracket_index.append(i)
	closing_bracket_index.reverse()
	cnt = 0
	i = 0
	l = len(closing_bracket_index)
	for idx in opening_bracket_index:
		if i < l and idx < closing_bracket_index[i]:
			cnt += 1
			i += 1
	return cnt >= 2

### Response:
```
```
For the string '[]]]]]]][[[[[]', the function will first identify the indices of the opening and closing brackets as follows:
opening_bracket_index = []
closing_bracket_index = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
Then it will check if the indices of the closing brackets are greater than the indices of the opening brackets. The result will be:
False, False, False, False, False, False, False, False, False, False, False, False
Since there are no True values in the result, the function will return False.
So, the return value of the function is [Output]False[/Output].
```
To automate the experiments, you should write a script to compare the output predicted by the LLM with the expected one (it exists in the HumanEval dataset) and store the result as a True/False in the deliverable JSON file for each problem with a key value “is_correct.” Your automation script should parse the HumanEval dataset file generated in MP1 and extract the program code, inputs, and the expected output. It then replaces placeholders in the prompt with this information. For example, you can create a prompt template similar to the example below for the vanilla prompting mentioned above. That is, your script can replace [INPUTS] and [PROGRAM] with the values you extract from the dataset, and also compare the predicted output with the extracted ground truth.

```
You are an AI programming assistant. You are an AI programming assistant, utilizing the DeepSeek Coder model, developed by DeepSeek Company, and you only answer questions related to computer science. For politically sensitive questions, security and privacy issues, and other non-computer science questions, you will refuse to answer.
### Instruction:
If the string is [INPUTS], what will the following code return?
The return value prediction must be enclosed between [Output] and [/Output] tags. For example : [Output]prediction[/Output].
[PROGRAM]

### Response:
```

### Deliverables for Task 1:
You should save all the results into JSONL files: task_1_{seed_value}_vanilla.jsonl (this is for storing the vanilla prompting results) and task_1_{seed_value}_crafted.jsonl (this is for storing the results after prompt crafting). Each problem is an item in your JSONL file, for which you should store (1) the prompt, (2) the model’s response, and the “is_correct” value. You also need to upload the log files generated into the GitHub repo. Explicit deliverables to be uploaded on the GitHub are:

- `task_1.py` (place it under the “MP2” directory on your repo) [40 points] -- DONE
- `task_1_{seed_value}_vanilla.jsonl` [20 points, 1 point per each problem] -- DONE
- `task_1_{seed_value}_crafted.jsonl` [60 points, 3 points per each problem] -- DONE
- `task_1_vanilla.log` [10 points] -- CONFIRM LOCATION
- `task_1_crafted.log` [10 points] -- CONFIRM LOCATION
- Update section MP2 of the progress report with the following information (please create a subsection for MP2-Task1):
  - To what extent can DeepSeekCoder reason about code execution? Report the success rate (calculate the success rate as the number of programs that LLM correctly predicts their output divided by 20 (the total number of programs in your experiments)) of the prompt crafting here. [20 points]-
  - What factor impacts the model's performance, i.e.,  when it can and cannot (you can explore the presence of specific programming constructs in the code, complex logic operations, nested constructs, etc.)? [20 points]
  - What changes to the vanilla prompt help the model to perform better on the task? Please also include a table showing the pairwise comparison of “is_correct” values per each program for vanilla prompting and prompt crafting (have a table where each row shows the values for “is_correct” from vanilla prompting and prompt crafting) [20 points]

## <<2- Test Generation>>

You must complete MP2/commands.py and MP2/task_2.py files under the “MP2” directory

The goal of this task is to generate unit tests with high coverage. We do not want to limit LLMs to the number of tests they should generate. However, you can specifically ask them to generate “N” number of tests if your experiments show this to be helpful, where you concretely mention the value of “N” in the prompt. You can also ask the LLM to generate tests that cover all possible values to exercise execution paths for the given program. For the vanilla prompting, you can use the example below (note that using the keywords “pytest” and “test suite” ensures that the LLM gives you a code that you can execute easily):

```
You are an AI programming assistant. You are an AI programming assistant, utilizing the DeepSeek Coder model, developed by DeepSeek Company, and you only answer questions related to computer science. For politically sensitive questions, security and privacy issues, and other non-computer science questions, you will refuse to answer.
### Instruction:
Generate a pytest test suite for the following code.
Only write unit tests in the output and nothing else.
def is_nested(string):
	opening_bracket_index = []
	closing_bracket_index = []
	for i in range(len(string)):
		if string[i] == '[':
			opening_bracket_index.append(i)
		else:
			closing_bracket_index.append(i)
	closing_bracket_index.reverse()
	cnt = 0
	i = 0
	l = len(closing_bracket_index)
	for idx in opening_bracket_index:
		if i < l and idx < closing_bracket_index[i]:
			cnt += 1
			i += 1
	return cnt >= 2

### Response:
```
```
import pytest

def test_no_brackets():
	assert is_nested("no brackets here") == False

def test_single_pair():
	assert is_nested("[]") == False

def test_two_pairs_nested():
	assert is_nested("[[]]") == True

def test_two_pairs_not_nested():
	assert is_nested("[][]") == False

def test_multiple_pairs_nested():
	assert is_nested("[[[]]]") == True

def test_multiple_pairs_not_nested():
	assert is_nested("[][][]") == False

def test_mixed_nested_and_not_nested():
	assert is_nested("[[]][]") == True

def test_unbalanced_brackets():
	assert is_nested("[[[]]") == False

def test_empty_string():
	assert is_nested("") == False

def test_nested_with_other_characters():
	assert is_nested("[a[b]c]") == True

def test_not_nested_with_other_characters():
	assert is_nested("[a][b]c") == False
```
After the model generates a Python test suite (if the model does not generate a test class with multiple tests, you can parse the response and create it yourself), you should run the tests to check if they pass or fail (assuming that you save the model’s response into a file ID_test.py for a given program, use the command `pytest ID_test.py` to execute the tests generated by the model). You should also generate test coverage. To get the coverage of the generated tests, you can use the command `pytest --cov ID_test.py --cov-report json:MP2/Coverage/ID_report.json`. This will save the coverage report (ID_report.json) under your repo's MP2/Coverage path. When using the initial prompt, test coverage may not be that high, and you should improve the prompt to generate higher coverage test suites.


### Deliverables for Task 2:

You should save all the results into JSON files: task_2_{seed_value}_vanilla.jsonl (this is for storing the vanilla prompting results) and task_2_{seed_value}_crafted.jsonl (this is for storing the results after prompt crafting). Each problem is an item in your JSON file, for which you should store (1) the prompt, (2) the model’s response, and the “is_correct” value. You also need to upload the log files generated into the GitHub repo. Explicit deliverables to be uploaded on the GitHub are:
- `task_2.py` (place it under the “MP2” directory on your repo) [40 points]
- `task_2_{seed_value}_vanilla.jsonl` [20 points, 1 point per each problem]
- `task_2_{seed_value}_crafted.jsonl` [60 points, 3 points per each problem]
- `task_2_vanilla.log` [10 points]
- `task_2_crafted.log` [10 points]
- 20 coverage reports named “ID_test.json,” where ID is the “task_id” of the program from the HumanEval dataset [40 points]
- Update section MP2 of the progress report with the following information (please create a subsection for MP2-Task2):
  - To what extent can DeepSeekCoder produce reasonable unit tests for a given code snippet? Report the percentage of generated unit tests that pass or fail (have a table where each row shows (1) the total number of generated tests, (2) the number of tests that pass, and (3) the number of tests that fail per program) [20 points]
  - What are the reasons for test failures, if you observe any? For the cases in which there are no test failures, can you confidently say the program is bug-free? You may look into the coverage of the tests to support your conclusions  [20 points]
  - What changes to the vanilla prompt help the model to perform better on the task? Please include a table showing the pairwise comparison of test suite coverage values per each program for vanilla prompting and prompt crafting (have a table where each row shows the coverage results from vanilla prompting and prompt crafting) [20 points]
  - Do you observe any relationship between code reasoning and test generation, or specifically, generating tests that pass? Please elaborate and ideally, perform a correlation analysis. [20 points]

# Validation script:
We have designed a validation script to ensure that you have followed the instructions and preserved the naming and structure of the files. Passing the validation script only shows that our grading script could proceed to grading, and you will not get a 0 if you change the naming and structure. You may pass the validation script but not get all the MP points. You can use validate.py script under the MP2 directory of the clones GitHub repo to validate the structure of the deliverables. Use main as the branch name.
