import jsonlines
import json
import csv
import subprocess


def read_jsonl(file_path):
    dataset = []
    with jsonlines.open(file_path) as reader:
        for line in reader: 
            dataset.append(line)
    return dataset

input_dataset = 'MP2/selected_humaneval_248264623217713294771470079546488913479.jsonl'
dataset = read_jsonl(input_dataset)

def coverage_per_task(vanilla):
    for entry in dataset:
        report_path = f"MP2/Coverage/{vanilla}/{entry['task_id'].replace('HumanEval/', '')}_report.json"
        solution_file_path = f"MP2/Testing_Info/{vanilla}/Task_{entry['task_id'].replace('HumanEval/', '')}_solution.py"

        # Open the report file and load its JSON content
        with open(report_path, 'r') as file:
            content = json.load(file)  # Load JSON data

        # Extract the percent_covered value from the nested structure
        percent_covered = content['files'][solution_file_path]['summary']['percent_covered']
        if (percent_covered == 0):
            print(f"{vanilla} -- Task: {entry['task_id']} coverage: {percent_covered}")

        #print(report_path)

        #MP2\Coverage\False\21_report.json

# coverage_per_task(True)
# coverage_per_task(False)


def pass_and_fail_tests(vanilla):
    # Open the output file in write mode
    with open("MP2/pass_fail_tests.txt", "a") as log_file:
        for entry in dataset:
            test_path = f"MP2/Testing_Info/{vanilla}/{entry['task_id'].replace('HumanEval/', '')}_test.py"
            
            print(f"Running pytest for {test_path}")
            # Capture the result and output
            result = subprocess.run(['pytest', test_path], capture_output=True, text=True)
            
           
            
            # Write the result to the log file
            log_file.write(f"Running pytest for {test_path}\n")
            log_file.write(result.stdout if result.stdout else "No output\n")
            log_file.write(result.stderr if result.stderr else "No errors\n")
            log_file.write("****************************\n")

  
# pass_and_fail_tests(True)
# pass_and_fail_tests(False)


def coverage_comparison_per_task():

  with open ("MP2/coverage_comparison_results", 'w') as output_file:
    for entry in dataset:
        vanilla_report_path = f"MP2/Coverage/True/{entry['task_id'].replace('HumanEval/', '')}_report.json"
        crafted_report_path = f"MP2/Coverage/False/{entry['task_id'].replace('HumanEval/', '')}_report.json"

        vanilla_solution_file_path = f"MP2/Testing_Info/True/Task_{entry['task_id'].replace('HumanEval/', '')}_solution.py"
        crafted_solution_file_path = f"MP2/Testing_Info/False/Task_{entry['task_id'].replace('HumanEval/', '')}_solution.py"

        # Open the report file and load its JSON content
        with open(vanilla_report_path, 'r') as file:
            vanilla_content = json.load(file)  # Load JSON data

        # Open the report file and load its JSON content
        with open(crafted_report_path, 'r') as file:
            crafted_content = json.load(file)  # Load JSON data

        # Extract the percent_covered value from the nested structure
        vanilla_percent_covered = vanilla_content['files'][vanilla_solution_file_path]['summary']['percent_covered']
        crafted_percent_covered = crafted_content['files'][crafted_solution_file_path]['summary']['percent_covered']
        output_file.write(f"{entry['task_id']} -- Vanilla: {vanilla_percent_covered}||Crafted: {crafted_percent_covered} \n")
        print(f"{entry['task_id']} -- Vanilla: {vanilla_percent_covered}||Crafted: {crafted_percent_covered}")

coverage_comparison_per_task()
