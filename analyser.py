"""
Tasks List:
1. Comand Line Arguments
2. methods.py realisation
3. methods.py integration & making exceptions
4. Custom skull fake loading before results 
"""
import sys
import methods



try:
    path = sys.argv[1]

except:
    sys.exit("Please rerun the programm and enter path to the file as first comand line argument: 'python3 analyser.py your_path'")
# Possibly use regex
sys.exit("File must be in .txt format.") if path[-4:] != ".txt" else 0

text = ""

try:
    with open(path) as file:
        for letter in file:
            text += letter

except:
    sys.exit("No such a file or file extension is not '.txt'")

print(methods.avg_length(text))