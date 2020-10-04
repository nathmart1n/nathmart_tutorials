"""
Intro to python exercises shell code
"""

def is_odd(x):
    if ((x % 2) == 0):
        return True
    else:
        return False


def is_palindrome(word):
    return word == word[::-1]


def only_odds(numlist):
    """
    returns a list of numbers that are odd from numlist
    ex: only_odds([1, 2, 3, 4, 5, 6]) -> [1, 3, 5]
    """
    return [num for num in numlist if num % 2 == 0]


def count_words(text):
    """
    return a dictionary of {word: count} in the text
    words should be split by spaces (and nothing else)
    words should be converted to all lowercase
    ex: count_words("How much wood would a woodchuck chuck"
                    " if a woodchuck could chuck wood?")
        ->
        {'how': 1, 'much': 1, 'wood': 1, 'would': 1, 'a': 2, 'woodchuck': 2,
        'chuck': 2, 'if': 1, 'could': 1, 'wood?': 1}
    """
    word_dict = {}
    words = text.split()

    for word in words:
        if word not in word_dict.keys():
            word_dict[word] == 1
        else:
            word_dict += 1