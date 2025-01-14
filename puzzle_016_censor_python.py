#!/usr/bin/env python3

def censor_python(string):
    """
    Function censors the word 'Python' with 'X's.

    :param string: a string passed to the function.
    :return: the string with the letters from Python censored.
    """
    python = ['P', 'y', 't', 'h', 'o', 'n']
    for char in string:
        if char in python:
            string = string.replace(char, 'X')
    return string


# Example function call:
print(censor_python("Hello Python! You're my favourite programming language!"))
