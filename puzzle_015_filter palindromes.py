#!/usr/bin/env python3

def filter_palindromes(list_of_strings):
    """
    Returns strings from a list that are palindromes.

    :param:
        list_of_strings: A list of strings.
    :return:
        a new list containing only the strings that are palindromes.
    """
    palindrome_list = []
    for word in list_of_strings:
        if word == word[::-1]:
            palindrome_list.append(word)
    return palindrome_list


# Example function calls:
print(filter_palindromes(['apple', 'banana', 'civic', 'date', 'racecar']))
