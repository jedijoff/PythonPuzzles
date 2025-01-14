#!/usr/bin/env python3

def ascii_to_string(ascii_list):
    """
    Function converts a list of ASCII values to a string.

    :param ascii_list: a list of ASCII values passed to the function.
    :return: a string.
    """
    return ''.join([chr(char) for char in ascii_list])


# Example function calls:
print(ascii_to_string([80, 114, 111, 103, 114, 97, 109, 109, 105, 110, 103,
                       32, 112, 117,122, 108, 101, 115, 33]))
print(ascii_to_string([72, 101, 108, 108, 111, 32, 119, 111, 114, 108, 100,
                       33]))
print(ascii_to_string([97, 65]))
