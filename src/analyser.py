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
# time.sleep(1)

print("Creating 'info.csv' file...")
# time.sleep(5)

print("Preparing for writing into 'info.csv'...")
# time.sleep(3)

data = {
    "total_letters": main_statistic(text)["letters"],
    "total_words": main_statistic(text)["words"],
    "total_sentences": main_statistic(text)["sentences"],
    "top_10_words": popular_words(text)["most_common"],
    "letters_frequency": letters_frequency(text),
    "words_average_length": avg_length(text)["words_average_length"],
    "sentences_average_length": avg_length(text)["sentences_average_length"],
    "unique_words": popular_words(text)["unique_words"],
    "shortest_word": short_long_word(text)["shortest"],
    "longest_word": short_long_word(text)["longest"],
}

try:
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
            "total_letters": data["total_letters"],
            "total_words": data["total_words"],
            "total_sentences": data["total_sentences"],

            "top_10_words": data["top_10_words"],

            "letters_frequency": data["letters_frequency"],

            "words_average_length": data["words_average_length"],
            "sentences_average_length": data["sentences_average_length"],

            "unique_words": data["unique_words"],
            
            "shortest_word": data["shortest_word"],
            "longest_word": data["longest_word"],
            })
        
        print("Report in 'info.csv' loaded.\n")
        time.sleep(0.5)
        print("Preparing for writing 'info.txt' report")
        time.sleep(3)
    
    with open("results/info.txt", "w") as file:

        # Skull Loading
        skull.skull_loading()

        file.write(
            f"""
            +===================+
            |RESULTS OF ANALYSIS|
            +===================+
            |Total Letters: {data["total_letters"]}
            |Total Words: {data["total_words"]}
            |Total Sentences: {data["total_sentences"]}
            |~~~~~~~~~~~~~~~~~
            |Top 10 most popular words: {data["top_10_words"]}
            |~~~~~~~~~~~~~~~~~
            |Letter Frequency: {data["letters_frequency"]}
            |~~~~~~~~~~~~~~~~~
            |Words average length: {data["words_average_length"]}
            |Sentences Average length: {data["sentences_average_length"]}
            |~~~~~~~~~~~~~~~~~
            |Unique Words: {data["unique_words"]}
            |~~~~~~~~~~~~~~~~~
            |Shortest Word(s): {data["shortest_word"]}
            |Longest Words(s): {data["longest_word"]}
            +-----------------
            """)
        
except:
    sys.exit("Failed to write 'info.csv' file")


with open("results/spelled_text.txt", "w") as file:
    """Speller here"""
    file.write(speller(text))

print("""
     CONGRADULATIONS!
         ______
      .-"      "-.
     /            \\
    |              |
    |,  .-.  .-.  ,|
    | )(_o/  \\o_)( |
    |/     /\\     \\|
    (_     ^^     _)
     \\__ \\____/ __/
      |          |
      \\          /
       `--------`
        
       WORK DONE!
    """)