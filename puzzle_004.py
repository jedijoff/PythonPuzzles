def reove_vowels(input_string):
    vowels = "aeiou"
    return "".join([char for char in input_string if char not in vowels])


print(reove_vowels("apple"))
print(reove_vowels("banana"))
print(reove_vowels("cherry"))
print(reove_vowels("Hello world"))