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

    for letter in "a-z":

        cnt = str(text).count(letter)

        if cnt > 1:
            frequency[letter: cnt]
    
    return frequency

def avg_values():
    pass

def short_long_word(text):
    #use split and min max

if __name__ == "__main__":   
    main()