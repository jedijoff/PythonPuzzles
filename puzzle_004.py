#!/usr/bin/env python3

def remove_vowels(input_string):
    """returns a string with all vowels removed.

    :param input_string: a user input string.
    :return: the input string with all vowels removed.
    """
    VOWELS = "aeiou"
    return "".join([chr for chr in input_string if chr.lower() not in vowels])


print(remove_vowels("Apple"))
print(remove_vowels("banana"))
print(remove_vowels("cherry"))
print(remove_vowels("Hello world"))
print(remove_vowels("Echo"))
