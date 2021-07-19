def print_upper_words(word_list, letters):

    """ accepts a list of words
    prints each word on a separate line
    in all-caps"""

    for word in word_list:
        for letter in letters:
            if letter.upper() == word[0].upper():
                print(word.upper())

print_upper_words(["hello", "hey", "goodbye", "yo", "yes", "nope"], ["Y", "N"])