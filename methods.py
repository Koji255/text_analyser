import string
import re

from collections import Counter

def main():
    return 0


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

    words_count = Counter(words)

    return words_count.most_common(10)



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
    if not (words := re.findall(r"\b[a-z]+\b", str(text), re.IGNORECASE)) or not (sentences := re.findall(r"(?:^|\s)[A-Z].+?[.!?]", str(text))):
        raise BaseException("Error")
    
    words_total_length = sum(len(word) for word in words)
    sentences_total_length = sum(len(sentence) for sentence in sentences)

    return {
        "words_total_length": words_total_length / len(words),
        "sentences_total_lenght": sentences_total_length / len(sentences),
    }



def short_long_word(text):
    """
    Returns dict of the shortest and the longest word/words from text
    """
    # Another, more complex way to get list of words using regex 
    words = str(text).lower().split()

    for i in range(len(words)):
        words[i] = words[i][:-1] if re.search(r"^.*[,.!?]$", words[i]) else words[i]

    longest_words = [word for word in words if len(word) == len(max(words, key=len))]
    shortest_words = [word for word in words if len(word) == len(min(words, key=len))]

    return {
        "longest": longest_words,
        "shortest": shortest_words,
    }



if __name__ == "__main__":
    main()