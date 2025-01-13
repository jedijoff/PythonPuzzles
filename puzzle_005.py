def get_longest_string(input_strings):
    longest_str = ''
    for word in input_strings:
        if len(word) > len(longest_str):
            longest_str = word
    return longest_str


print(get_longest_string(['apple', 'banana', 'cherry', 'date', 'elderberry', 'fig', 'grape']))
print(get_longest_string(['cat', 'dog', 'elephant', 'fish', 'giraffe', 'hippopotamus', 'iguana']))