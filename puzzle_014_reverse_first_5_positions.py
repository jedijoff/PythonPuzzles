#!/usr/bin/env python3


def reverse_first_5_positions(string):
    """
    Function reverses the first 5 positions of a string or list.

    :param string: a string or list, or tuple passed to the function.
    :return: the string or list or tuple with the first 5 characters or
    positions reversed. If the input string is less than 5 characters, the
    function will return the string reversed.
    """
    return string[4::-1] + string[5:]


# Example function calls:
print(reverse_first_5_positions('hello world'))
print(reverse_first_5_positions('1234567890'))
print(reverse_first_5_positions(['abc', 'def', 'ghi', 'jkl', 'mno', 'pqr',
                                 'stu', 'vwx', 'yz']))
print(reverse_first_5_positions(('abc', 'def', 'ghi', 'jkl', 'mno', 'pqr',)))
print(reverse_first_5_positions('new'))
