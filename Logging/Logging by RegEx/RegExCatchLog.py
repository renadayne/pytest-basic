import random
import re

def read_random_lines(file_path, min_lines, max_lines):
    with open(file_path, 'r') as file:
        lines = file.readlines()
        
        num_lines = random.randint(min_lines, max_lines)
        selected_lines = random.sample(lines, num_lines)
        
        for line in selected_lines:
            logs = "[2023-08-30 04:40:07,352][getStarted.py:47][Sample][Dummy-4] Logging"
            logs_in_file = line.strip()
            pattern = r"\[([^]]+)\]\[([^]]+)\]\[([^]]+)\]\[([^]]+)\] ([^ ]+)"

            matches = re.findall(pattern, logs_in_file)
            for match in matches:
                fName_lineno = match[1]
                func_name = match[2]
                log_message = match [4]
                if(re.findall("getStarted.py", fName_lineno) and re.findall("Sample", func_name)): 
                    print(f"{fName_lineno} {func_name} {log_message}")
        print(num_lines)
file_path = r"C:\Users\Asus\Downloads\logging_sample_file.txt"
min_lines = 10
max_lines = 50

read_random_lines(file_path, min_lines, max_lines)

