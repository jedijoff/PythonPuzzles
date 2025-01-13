def filter_even_length_strings(input_strings):
    even_length_strings = []
    for word in input_strings:
        if len(word) % 2 == 0:
            even_length_strings.append(word)
    return even_length_strings


print(filter_even_length_strings(['apple', 'banana', 'cherry', 'date', 'elderberry', 'fig', 'grape']))
print(filter_even_length_strings(['cat', 'dog', 'elephant', 'fish', 'giraffe', 'hippopotamus', 'iguana']))
