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
    # Ensure Input_a is the same length or shorter than Input_b,
    # as input_a defines the length of the returned string.
    if len(input_a) >= len(input_b):
        new_a = []
        [str(new_a.append(input_a[i])) for i in range(len(input_b))]
        input_a = "".join(new_a)
    # This section that does the XOR comparison and returns the result:
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





