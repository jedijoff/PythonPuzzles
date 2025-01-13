#!/usr/bin/env python3

def get_longest_string(input_strings):
    """ A function that returns the longest string from a list of strings

    Args:
        input_strings: A list of strings. The list must contain
        a minimum of 1 string
    :return: The longest string from the list.
    """
    longest_str = ''
    for word in input_strings:
        if len(word) > len(longest_str):
            longest_str = word
    return longest_str


# Example function calls:
print(get_longest_string(['apple', 'banana', 'cherry', 'date',
                          'elderberry', 'fig', 'grape']))
print(get_longest_string(['cat', 'dog', 'elephant', 'fish',
                          'giraffe', 'hippopotamus', 'iguana']))