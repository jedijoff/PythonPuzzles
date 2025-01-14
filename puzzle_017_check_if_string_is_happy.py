#!/usr/bin/env python3

def check_if_string_is_happy(string):
    """
    Function checks if a string is happy.

    :param string: a string passed to the function.
    :return: To be happy, when the string is broken into chunks of 3
    or fewer characters, the characters in each chunk must be unique.
    If a chunk of the string is less than three characters the else
    statement will check if the shorter string is happy.
    """
    for i in range(0, len(string), 3):
        if len(set(string[i:i + 3])) == 3:
            return True
        else:
            return len(string[i:]) == len(set(string[i:]))


print(check_if_string_is_happy('abcabcabc'))
print(check_if_string_is_happy('abcabcab'))
print(check_if_string_is_happy('cbcabcaba'))
print(check_if_string_is_happy('cbcabc'))