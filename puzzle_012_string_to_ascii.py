#!/usr/bin/env python3

def string_to_ascii(string):
    """
    Function converts a string to a list of ASCII values.

    :param string: a string passed to the function.
    :return: a list of ASCII values.
    """
    return [ord(char) for char in string]


print(string_to_ascii('hello'))
print(string_to_ascii('world'))
print(string_to_ascii('Python'))
print(string_to_ascii('aA'))