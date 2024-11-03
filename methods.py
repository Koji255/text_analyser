import string
import re

from collections import Counter

def main():
    return 0


def main_statistic(text):
    """
    letters, words and sentences
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
    top 10 most popular words
    """
    text = str(text)

    words = re.findall(r"\b[a-z]+\b", text.lower())

    words_count = Counter(words)

    return words_count.most_common(10)



def letters_frequency(text):
    """"
    returns total count of every letter in the text
    """
    frequency = {}

    for letter in string.ascii_lowercase:
        cnt = str(text).lower().count(letter)

        if cnt > 0:
            frequency[letter] = cnt

    return frequency


def avg_length(text):
    
    if not (words := re.findall(r"\b[a-z]+\b", str(text).lower())):
        raise("ValueError!")
    
    total_length = sum(len(word) for word in words)

    return total_length / len(words)



def short_long_word(text):
    """Defines words and returns shortest and longest of them"""

    words = str(text).split()

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