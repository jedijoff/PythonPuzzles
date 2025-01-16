#!/usr/bin/env python3

def xor(input_a, input_b):
    """
    This function calculates the XOR of two binary values.

    This function calculates the XOR of two binary values entered as
    strings. This is the same as the bitwise ^ operator. it will
    accept two binary values of different lengths and return the XOR
    comparison to the length of the shortest string.

    :param: input_a: A binary value as a string.
    :param: input_b: A binary value as a string.
    :return: the XOR of the two binary values as a string.
    """
    # Check the length of input_a and input_b and swap them if necessary
    if len(input_a) > len(input_b):
        input_a, input_b = input_b, input_a
    # This section that does the XOR comparison and returns the result
    result = []
    for i in range(len(input_a)):
        if input_a[i] != input_b[i]:
            result.append("1")
        else:
            result.append("0")
    return "".join(result)


# Example function calls:
print(xor("1010", "1010"))
print(xor("1010", "1011"))
print(xor("110010", "1010"))
print(xor("1010", "110010"))





