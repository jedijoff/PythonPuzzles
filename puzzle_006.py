def filter_even_length_strings(input_strings):
    """ A function that filters even length strings from a list of strings

    Args:
        input_strings: A list of strings. The list must contain
        a minimum of 1 string
    :return: A list of strings with even length.
    """
    even_length_strings = []
    for word in input_strings:
        if len(word) % 2 == 0:
            even_length_strings.append(word)
    return even_length_strings


# Example function calls:
print(filter_even_length_strings(['apple', 'banana', 'cherry', 'date',
                                  'elderberry', 'fig', 'grape']))
print(filter_even_length_strings(['cat', 'dog', 'elephant', 'fish', 'giraffe',
                                  'hippopotamus', 'iguana']))