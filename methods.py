import string
import re


def main():
    return 0


def main_statistic(text):
    """
    letters, words and sentences
    """
    # Will contain dict of results for aesthetic purpose. Ill return it

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


def popular_word(text):
    """
    top 10 most popular words
    """
    pass


def letters_frequency(text):
    """"
    given a dict. Using for loop and count if this letter in loop.count() > 1. Create a KV pair
    """

    frequency = {}

    for letter in string.ascii_lowercase:

        cnt = str(text).count(letter)

        if cnt > 0:
            frequency[letter] = cnt
    
    return frequency


def avg_values():
    pass


def short_long_word(text):
    words = str(text).split()

    for i in range(len(words)):
        words[i] = words[i][:-1] if re.search(r"^.*[,.!?]$", words[1]) else words[i]

    longest_words = [word for word in words if len(word) == len(max(words, key=len))]
    shortest_words = [word for word in words if len(word) == len(min(words, key=len))]

    return {
        "longest": longest_words,
        "shortest": shortest_words,
    }



if __name__ == "__main__":
    main()