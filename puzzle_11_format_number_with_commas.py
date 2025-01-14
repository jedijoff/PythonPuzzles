#!/usr/bin/env python3

def format_number_with_commas(number) -> str:
    """
    Function formats a number with commas.

    :param number: a number passed to the function.
    :return: the number formatted with commas.
    """
    return  "{:,}".format(number)


print(format_number_with_commas(1000))
print(format_number_with_commas(1000000))
print(format_number_with_commas(10000000))