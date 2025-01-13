def sum_if_less_than_50(num_1, num_2):
    if num_1 + num_2 < 50:
        return num_1 + num_2
    else:
        return None


print(sum_if_less_than_50(10, 5))
print(sum_if_less_than_50(20, 20))
print(sum_if_less_than_50(30, 20))
print(sum_if_less_than_50(30, 30))
