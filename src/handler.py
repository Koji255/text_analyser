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
import time

import cowsay

from methods import *



try:
    if len(sys.argv) != 2:
        raise SystemError()
    
    path = sys.argv[1]

except:
    sys.exit("Error 1. Rerun the program using path to the text file as the first and single comand line argument.")
# Regex to filter the name of the file
sys.exit("Error 2. File extension must be '.txt'") if not re.search(r".+[^/]\.txt$", path) else 0

text = ""
# Reading the file
try:
    with open(path) as file:

        print("Reading the file...")

        for letter in file:
            text += letter

except FileNotFoundError:
    sys.exit("Error 3. Not such a file.")

if not text:
    sys.exit("Error 4. Empty or a broken file.")

print("File has been read successfully! \n")
time.sleep(0.2)

# Selecting work mode
print("Select an option:",
    "+----------------------+",
    "| '1' - Spell the text |",
    "| '2' - Analyse text   |",
    "| '3' - Create a graph |",
    "+----------------------+", sep="\n")

option = ""

while option != "1" and option != "2" and option != "3":
    option = input("Option: ")

# Spelling the text
if option == "1":
    try:
        with open("results/spelled_text.txt", "w") as file:
            print("Spelling the text...")
            time.sleep(0.3)

            # From the dic returned by speller()
            spelled_text = speller(text)["spelled_text"]

            file.write(spelled_text)

            print("Spelling completed succesfully.\n")
            print("Display spelled text?")

            text_display_option = ""

            while text_display_option not in ["y", "n"]:
                text_display_option = input("Option [Y|N]: ").lower()
            
            if text_display_option == "y":
                print(f"\nSpelled text:\n{spelled_text}")
                time.sleep(5)

            print("\n"*50)
            sys.exit(cowsay.dragon("This Was CS50 ♡"))

    except (FileNotFoundError, FileExistsError):
        sys.exit("Error 5. 'results/' directory doesn't found.")

    else:
        sys.exit("Error 6. Failed to spell text.")

# Data dict for the next 2 options
data = {
    "total_stats": total_stats(text),
    "repeatability": repeatability(text),
    "letters_frequency": letters_frequency(text),
    "average_length": average_length(text),
    "short_long_word": short_long_word(text),
}

# Building graphics
if option == "3":
    print("\nSelect a graph to build:",
          "+---------------------------------+",
          "| '1' - Words Frequency (Scatter) |",
          "| '2' - Words Frequency (Bars)    |",
          "| '3' - Misspells Rate  (Pie)     |",
          "+---------------------------------+", sep="\n")
    
    graph_option = ""

    while graph_option not in ["1", "2", "3"]:
        graph_option = input("Option: ")
    
    print("\nPlease, name the file")
    filename = input("Filename: ")

    if graph_option == "1":        
        scatter_graph(x=data["letters_frequency"].keys(),
                      y=data["letters_frequency"].values(),
                      filename=filename, 
                      xlabel="letters",
                      ylabel="frequencies",
                      title="Letter Frequency")

    elif graph_option == "2":
        bars_graph(x=data["letters_frequency"].keys(),
                   y=data["letters_frequency"].values(),
                   filename=filename,
                   xlabel="letters",
                   ylabel="frequencies",
                   title="Letter Frequency")
        
    else:
        pie_graf(vals=[speller(text)["misspeled_words_amount"], data["total_stats"]["words"]],
                 labels=["Misspells", "Correct"],
                 filename=filename,
                 title="Misspelled Words Ratio",)
    
    sys.exit("Graph has been built and saved in 'results/graphs/'.")

# Option 2: Writing text analysis report in 2 files - .txt & .csv 
print("Creating 'info.csv' file...",
      "Preparing for writing into 'info.csv'...", sep="\n")
time.sleep(0.2)
# Writing into csv report
try:
    with open("results/info.csv", "w") as file:

        print("Writing 'info.csv' report...")
        time.sleep(0.3)

        writer = csv.DictWriter(file, fieldnames=[
                                                "total_letters",
                                                "total_words",
                                                "total_sentences",
                                                "top_10_words",
                                                "letters_frequency",
                                                "words_average_length",
                                                "sentences_average_length",
                                                "unique_words",
                                                "shortest_word",
                                                "longest_word",
                                                ])

        writer.writeheader()

        writer.writerow(
            {
            "total_letters": data["total_stats"]["letters"],
            "total_words": data["total_stats"]["words"],
            "total_sentences": data["total_stats"]["sentences"],

            "top_10_words": data["repeatability"]["most_common"],

            "letters_frequency": data["letters_frequency"],

            "words_average_length": data["average_length"]["words_average_length"],
            "sentences_average_length": data["average_length"]["sentences_average_length"],

            "unique_words": data["repeatability"]["unique_words"],
            
            "shortest_word": data["short_long_word"]["shortest"],
            "longest_word": data["short_long_word"]["longest"],
            })
        
        print("Writing into 'info.csv' was completed.\n")
except:
    sys.exit("Error 7. Failed to write 'info.csv' file.")          

# Writing user friendly 'info.txt' report
try:
    print("Writing 'info.txt' report...")
    time.sleep(0.3)

    user_friendly_results = f"""
+===================+
|RESULTS OF ANALYSIS|
+===================+
Total Letters: {data["total_stats"]["letters"]}
Total Words: {data["total_stats"]["words"]}
Total Sentences: {data["total_stats"]["sentences"]}
~~~~~~~~~~~~~~~~~~~~~
Top 10 most popular words: {data["repeatability"]["most_common"]}
~~~~~~~~~~~~~~~~~~~~~
Letter Frequency: {data["letters_frequency"]}
~~~~~~~~~~~~~~~~~~~~~
Words average length: {data["average_length"]["words_average_length"]}
Sentences Average length: {data["average_length"]["sentences_average_length"]}
~~~~~~~~~~~~~~~~~~~~~
Unique Words: {data["repeatability"]["unique_words"]}
~~~~~~~~~~~~~~~~~~~~~
Shortest Word(s): {data["short_long_word"]["shortest"]}
Longest Words(s): {data["short_long_word"]["longest"]}
=====================
"""

    with open("results/info.txt", "w") as file:
        file.write(user_friendly_results)

        print("Writing into 'info.txt' was completed.\n")
        
except:
    sys.exit("Error 8. Failed to write 'info.txt' file.")

print("Work successfully completed.\n", "Display report?", sep="\n")

display_option = ""

while display_option not in ["y", "n"]:
    display_option = input("Option [Y|N]: ").lower()

if display_option == "y":
    print(user_friendly_results)

sys.exit()
