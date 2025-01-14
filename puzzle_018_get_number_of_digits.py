#!/usr/bin/env python3

def get_number_of_digits(number):
    """
    Function returns the number of digits in a number.

    :param number: a number passed to the function.
    :return: the number of digits in the number.

    NB: The puzzle specified that the function should be
    recursive, and not convert the number to a string,
    so the obvious return len(str(number)) option was
    off the cards.
    """
    if number > 0:
        number = number // 10
        get_number_of_digits(number, count+1)
    else:
        print(count)


get_number_of_digits(1000)
get_number_of_digits(1000000)
get_number_of_digits(10000000)
get_number_of_digits(1234567890)