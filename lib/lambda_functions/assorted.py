from functools import reduce


def filter_palindromes(words):
    return list(filter(lambda x : x[::-1] == x, words))

def map_celsius_to_fahrenheit(celcius_temps):
    return list(map(lambda x : x * 9/5 + 32, celcius_temps))

def reduce_find_longest_word(words):
    return reduce(lambda x, y : x if len(x) > len(y) else y, words)

def filter_numbers_within_range(numbers, lower, upper):
    return list(filter(lambda x : x >= lower and x <= upper, numbers))

def map_square_and_convert_to_string(numbers):
    return list(map(lambda x : str(x ** 2), numbers))