def filter_type_str(input_list):
    return [i for i in input_list if type(i) == str]


print(filter_type_str([1, 2, 3, 'a', 'b', 'c', 4, 5, 6]))
print(filter_type_str([1, 2, 3, 4, 5, 6]))
print(filter_type_str(['a', 'b', 'c']))
print(filter_type_str([]))