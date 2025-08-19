from functools import reduce

def sum_of_squares(numbers):
    return reduce(lambda acc, x : acc + x ** 2, numbers)

def concatenate_strings(strings):
    return reduce(lambda acc, x : acc + x, strings)

def find_maximum(numbers):
    return reduce(lambda x, y : x if x > y else y, numbers)

def product_of_numbers(numbers):
    return reduce(lambda acc, x : acc * x, numbers)

def find_longest_string(strings):
    return reduce(lambda x, y : x if len(x) > len(y) else y, strings)

#welcome back, let's do this!