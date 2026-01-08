# Task 1: Read a File and Handle Errors

try:
    with open("sample.txt", "r") as file:
        for index, line in enumerate(file, start=1):
            print(f"Line {index}: {line.strip()}")
           
except FileNotFoundError:
    print("Error: The file 'sample.txt' does not exist.")