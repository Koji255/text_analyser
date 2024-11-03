"""
Tasks List:
1. Comand Line Arguments
2. methods.py realisation
3. methods.py integration & making exceptions
4. Custom skull fake loading before results 
"""
import sys
import re

import methods



try:
    path = sys.argv[1]

except:
    sys.exit("Error 1. Rerun the program using path to the file as second CLA.")
# Regex to filter the name of the file
sys.exit("Error 2. File extension must be '.txt'") if not re.search(r"^.+['.txt']$", path) else 0

text = ""

try:
    with open(path) as file:
        for letter in file:
            text += letter

except:
    sys.exit("Error 3. Empty or broken file.")
