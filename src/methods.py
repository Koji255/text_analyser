import string
import re

from collections import Counter

import language_tool_python



def main():
    return 0


def speller(text):
    """
    Returns str var of spelled text
    """
    # Connecting to the local server
    tool = language_tool_python.LanguageTool("en")

    # Finding spelling mistakes
    matches = tool.check(text)

    return language_tool_python.utils.correct(text, matches)


def main_statistic(text):
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


def popular_words(text):
    """
    Returns list of 10 most popular word in ASC order
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


def avg_length(text):
    """
    Returns float variable of average of all word's length 
    """
    # Regexes for filtering all words & sentences
    if not (words := re.findall(r"\b[a-z]+\b", str(text), re.IGNORECASE)) or not (sentences := re.findall(r"(?:^|\s)([A-Z].+?)[.!?]", str(text))):
        raise ValueError("Empty or broken file")
    
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

    shortest_words = [word for word in words if len(word) == len(min(words, key=len))]
    longest_words = [word for word in words if len(word) == len(max(words, key=len))]

    return {
        "shortest": shortest_words,
        "longest": longest_words,
    }



if __name__ == "__main__":
    main()