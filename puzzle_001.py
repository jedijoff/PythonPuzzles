#!/usr/bin/env python3

def filter_strings_containing_a(list_of_strings):
    """returns strings from a list that contain the letter 'a'.

    :param list_of_strings:
    :return: a new list containing only the strings that contain
             the letter 'a'.
    """
    a_list = []
    for word in list_of_strings:
        if 'a' in list(word):
            a_list.append(word)
    return a_list


print(filter_strings_containing_a(['apple', 'banana', 'cherry', 'date', 'elderberry', 'fig', 'grape']))