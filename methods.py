def main_statistic(text):
    """
    letters, words and sentences
    """
    # Will contain dict of results for aesthetic purpose. Ill return it
    results = {} 

    lcnt, wcnt, scnt = 0, 1, 0

    for letter in text:

        letter = str(letter)

        if letter.isalpha():
            lcnt += 1

        elif letter.isspace():
            wcnt += 1

        elif letter in [".", "!", "?"]:
            scnt += 1



def popular_word():
    """
    top 10 most popular words
    """

def words_frequency():
    pass

if __name__ == "__main__":
    
    
    main()