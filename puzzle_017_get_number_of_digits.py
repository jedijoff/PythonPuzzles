#!/usr/bin/env python3

def get_number_of_digits(number):
    """
    Function returns the number of digits in a number.

    :param number: a number passed to the function.
    :return: the number of digits in the number.
    """
    count = 0
    
    while number > 0:
        count += 1
        number = number // 10

    return count


print(get_number_of_digits(1000))
print(get_number_of_digits(1000000))
print(get_number_of_digits(10000000))
print(get_number_of_digits(1234567890))
