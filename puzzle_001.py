def filter_strings_containing_a(list_of_strings):
    a_list = []
    for word in list_of_strings:
        if 'a' in list(word):
            a_list.append(word)
    return a_list



print(filter_strings_containing_a(['apple', 'banana', 'cherry', 'date', 'elderberry', 'fig', 'grape']))