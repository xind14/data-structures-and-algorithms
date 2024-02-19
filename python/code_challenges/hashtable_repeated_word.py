from data_structures.hashtable import Hashtable

def first_repeated_word(input_string):
    hashtable = Hashtable()

    words = [word.strip(string.punctuation) for word in input_string.lower().split()]

    for word in words:
        if hashtable.get(word):
            return word
        else:
            hashtable.set(word, True)

    return None

import string


