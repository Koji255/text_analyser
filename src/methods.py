import sys
import string
import re

from collections import Counter

import matplotlib.pyplot as plt
from spellchecker import SpellChecker



def main():
    return 0


def speller(text):
    """Returns str variable of spelled text"""
    # Contains all spell checking functionality
    spell = SpellChecker()
    # SpellChecker works only with iterable objects
    words = str(text).split()
    # Finds all misspeled words from the list
    misspeled_words = spell.unknown(words)

    for i, word in enumerate(words):
        # If word is misspeled and not a reduction
        if word in misspeled_words and not re.search(
            fr"\b{word.capitalize()}\b", text):
            # Most likely word spell option
            spelled_word = spell.correction(word)

            if not spelled_word:
                continue

            prefix, suffix = "", ""
            # Handles first symbol of word
            if word[0] in ["'", '"']:
                prefix = word[0]
                word = word[1:]
            # Handles last symbol of word
            if word[-1] in string.punctuation:
                suffix = word[-1]
                word = word[:-1]

            words[i] = f"{prefix}{spelled_word}{suffix}"

    return " ".join(words)


def bars_graph(x, y, filename, xlabel, ylabel, title):
    try:
        # Cut user file's extenion if exists and extract with group(1)
        if not (filename := re.search(r"^([^.]+?)(?:[.].*)?$", filename).group(1)):
            raise AttributeError
        
    except AttributeError: 
        sys.exit("Error 9. Invalid filename.")

    # plt graph's style settings
    with plt.style.context("dark_background"):
        plt.bar(x, y, label="Frequency")
        
        plt.xlabel(xlabel, color="w")
        plt.ylabel(ylabel, color="w")
        plt.title(title, color="w")

        try:
            plt.savefig(f"results/graphs/{filename}.svg")

        except:
            sys.exit(f"Error 10. Failed to save graphic using path results/graphs/{filename}.svg")

    return 0


def scatter_graph(x, y, filename, xlabel, ylabel, title):
    try:
        if not (filename := re.search(r"^([^.]+?)(?:[.].*)?$", filename).group(1)):
            raise AttributeError
        
    except AttributeError: 
        sys.exit("Error 9. Invalid filename.")

    with plt.style.context("dark_background"):
        plt.scatter(x, y, label="Frequency")
        
        plt.xlabel(xlabel, color="w")
        plt.ylabel(ylabel, color="w")
        plt.title(title, color="w")

        try:
            plt.savefig(f"results/graphs/{filename}.svg")

        except:
            sys.exit(f"Error 10. Failed to save graphic using path results/graphs/{filename}.svg")
            
    return 0


def total_stats(text):
    """
    Returns dict of cnt of letters, words & sentences
    """
    lcnt, wcnt, scnt = 0, 1, 0

    for letter in text:

        letter = str(letter)

        if letter.isalpha():
            lcnt += 1

        elif letter.isspace():
            wcnt += 1

        elif letter in [".", "!", "?"]:
            scnt += 1

    return {
        "letters": lcnt,
        "words": wcnt,
        "sentences": scnt,
    }


def repeatability(text):
    """
    Returns list of 10 most popular word & * unique words
    """
    # Regex that returns all words excluding punctuation symbols.
    words = re.findall(r"\b[a-z]+\b", str(text), re.IGNORECASE)

    # Returns dict with K as a word and V as a count
    words_count = Counter(words)

    unique_words = []

    # Multiple unpacking
    for word, count in words_count.items():
        if count == 1:
            unique_words.append(word)
    

    return {
        "most_common": words_count.most_common(10),
        "unique_words": unique_words,
    }



def letters_frequency(text):
    """"
    Returns dict of count of every letter in the text excluding letters with value 0.
    """
    frequency = {}

    for letter in string.ascii_lowercase:
        cnt = str(text).lower().count(letter)

        if cnt > 0:
            frequency[letter] = cnt

    return frequency


def average_length(text):
    """
    Returns float variable of average of all word's length 
    """
    # Regexes for filtering all words & sentences
    if not (words := re.findall(r"\b[a-z]+\b", str(text), re.IGNORECASE)) or not (sentences := re.findall(r"(?:^|\s)([A-Z].+?)([.!?]|$)", str(text))):
        sys.exit("Error 4. Empty or broken file")
    
    words_total_length = sum(len(word) for word in words)
    sentences_total_length = sum(len(sentence) for sentence in sentences)

    return {
        "words_average_length": round((words_total_length / len(words)), 2),
        "sentences_average_length": round((sentences_total_length / len(sentences)), 2),
    }



def short_long_word(text):
    """
    Returns dict of the shortest and the longest word/words from text
    """
    # Another, more complex way to get list of words using regex 
    words = re.findall(r"\b[a-z]+\b", str(text), re.IGNORECASE)

    # Finding shortest word length excluding article "a"
    min_length = max(2, len(min(words, key=len)))
    shortest_words = [word for word in words if len(word) == min_length]
    longest_words = [word for word in words if len(word) == len(max(words, key=len))]

    return {
        "shortest": shortest_words,
        "longest": longest_words,
    }



if __name__ == "__main__":
    main()