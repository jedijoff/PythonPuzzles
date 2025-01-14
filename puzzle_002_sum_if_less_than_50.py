#!/usr/bin/env python3

def sum_if_less_than_50(num_1, num_2):
    """
    returns the sum of two numbers if the sum is less than 50.

    :param num_1: assigned the first number passed to the function.
    :param num_2: assigned the second number passed to the function.
    :return: the sum of the numbers, if that is less than 50.
    """
    if num_1 + num_2 < 50:
        return num_1 + num_2
    else:
        return None


# Example function calls:
print(sum_if_less_than_50(10, 5))
print(sum_if_less_than_50(20, 20))
print(sum_if_less_than_50(30, 20))
print(sum_if_less_than_50(30, 30))
