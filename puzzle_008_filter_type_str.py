#!/usr/bin/env python3

def filter_type_str(input_list):
    """
    Takes a list of elements, returns a list of only the string elements

    :param:
        input_list: a list of various elements.
    :return:
        a list of all elements that are strings.
    """
    return [i for i in input_list if type(i) == str]


# Example function calls:
print(filter_type_str([1, 2, 3, 'a', 'b', 'c', 4, '5', 6]))
print(filter_type_str([1, 2, 3, 4, 5, 6]))
print(filter_type_str(['a', 'b', 'c']))
print(filter_type_str([]))
print(filter_type_str(['a', 1, (1, 'a'), 'b', 2, 'c', 3, ['cat', 1, '@']]))