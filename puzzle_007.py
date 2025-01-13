#!/usr/bin/env python3

def reverse_elements(list_of_numbers):
    """
    Takes a user list of numbers, as input, returns the list reversed

    :param list_of_numbers: a list of numbers.
    :return: the list, reversed.
    """
    return list_of_numbers[::-1]


# Example function calls
print(reverse_elements([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
print(reverse_elements([10, 9, 8, 7, 6, 5, 4, 3, 2, 1]))
print(reverse_elements([1.97, 2.97, 3.97, 4.97, 5.97, 6.97, 7.97]))
