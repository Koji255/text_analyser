"""
Tasks List:
1. Comand Line Arguments
2. methods.py realisation
3. methods.py integration & making exceptions
4. Custom skull fake loading before results 
"""
import sys
import re
import csv

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
    raise sys.exit("Error 3. Empty or broken file.")

# Here will be custom loading

with open("file_info.csv", "w") as file:
    writer = csv.DictWriter(file, fieldnames=[
                                            "total_letters",
                                            "total_words",
                                            "total_sentences",
                                            "top_10_words",
                                            "letters_frequency",
                                            "words_average_length",
                                            "sentences_average_length",
                                            "shortest_word",
                                            "longest_word",
                                            ])

    writer.writeheader()

    writer.writerow(
        {
        "total_letters": methods.main_statistic(text)["letters"],
        "total_words": methods.main_statistic(text)["words"],
        "total_sentences": methods.main_statistic(text)["sentences"],

        "top_10_words": methods.popular_words(text),

        "letters_frequency": methods.letters_frequency(text),

        "words_average_length": methods.avg_length(text)["words_average_length"],

        "sentences_average_length": methods.avg_length(text)["sentences_average_length"],
        
        "shortest_word": methods.short_long_word(text)["longest"],
        "longest_word": methods.short_long_word(text)["shortest"],
        })