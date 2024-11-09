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

from methods import *
import skull



try:
    if len(sys.argv) != 2:
        raise SystemError()
    
    path = sys.argv[1]

except:
    sys.exit("Error 1. Rerun the program using path to the text file as the first and single comand line argument.")
# Regex to filter the name of the file
sys.exit("Error 2. File extension must be '.txt'") if not re.search(r".+[^/]\.txt$", path) else 0

text = ""

try:
    with open(path) as file:

        print("Reading file...")

        for letter in file:
            text += letter

except FileNotFoundError:
    sys.exit("Error 3. Not such a file.")

if not text:
    sys.exit("Error 4. Empty or broken file.")

print("File has been read successfully! \n")
time.sleep(0.5)

# Selecting work mode
print("Select an option:",
    "+----------------------+",
    "| '1' - Analyse text   |",
    "| '2' - Spell the text |",
    "+----------------------+", sep="\n")

option = ""

while option != "1" and option != "2":
    option = input("Option: ")
# For speller option
if option == "2":
    try:
        with open("results/spelled_text.txt", "w") as file:
            """Speller here"""
            print("Spelling the text...")
            time.sleep(0.5)

            spelled_text = speller(text)

            file.write(spelled_text)
            
            # skull.skull_loading()

            skull.skull_congrats(message="Text succesfully spelled")

            print("Display spelled text?")

            if input("Option [Y|N]: ") in "yY":
                print(f'\nSpelled text:\n{spelled_text}')
            sys.exit()

    except (FileNotFoundError, FileExistsError):
        sys.exit("Error 5. 'results/' directory doesn't found.")

    else:
        sys.exit("Error 6. Failed to spell text.")


print("Creating 'info.csv' file...",
      "Preparing for writing into 'info.csv'...", sep="\n")

data = {
    "total_stats": total_stats(text),
    "repeatability": repeatability(text),
    "letters_frequency": letters_frequency(text),
    "average_length": average_length(text),
    "short_long_word": short_long_word(text),
}

try:
    print("Writing 'info.csv' report...\n")
    time.sleep(0.5)
    
    with open("results/info.csv", "w") as file:
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
        
        print("Writing was done.\n")
except:
    sys.exit("Error 7. Failed to write 'info.csv' file")          


try:
    print("Writing 'info.txt' report...\n")
    time.sleep(0.5)
    
    with open("results/info.txt", "w") as file:
        # Skull Loading
        # skull.skull_loading()

        file.write(
            f"""
            +===================+
            |RESULTS OF ANALYSIS|
            +===================+
            |Total Letters: {data["total_stats"]["letters"]}
            |Total Words: {data["total_stats"]["words"]}
            |Total Sentences: {data["total_stats"]["sentences"]}
            |~~~~~~~~~~~~~~~~~
            |Top 10 most popular words: {data["repeatability"]["most_common"]}
            |~~~~~~~~~~~~~~~~~
            |Letter Frequency: {data["letters_frequency"]}
            |~~~~~~~~~~~~~~~~~
            |Words average length: {data["average_length"]["words_average_length"]}
            |Sentences Average length: {data["average_length"]["sentences_average_length"]}
            |~~~~~~~~~~~~~~~~~
            |Unique Words: {data["repeatability"]["unique_words"]}
            |~~~~~~~~~~~~~~~~~
            |Shortest Word(s): {data["short_long_word"]["shortest"]}
            |Longest Words(s): {data["short_long_word"]["longest"]}
            +-----------------
            """)
except:
    sys.exit("Error 8. Failed to write 'info.txt' file")


skull.skull_congrats()