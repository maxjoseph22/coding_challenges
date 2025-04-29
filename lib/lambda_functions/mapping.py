def square_numbers(numbers):
    return list(map(lambda x : x ** 2, numbers))

def uppercase_words(words):
    return list(map(lambda x : x.upper(), words))

def double_numbers(numbers):
    return list(map(lambda x : x * 2, numbers))

def length_of_words(words):
    return list(map(lambda x : len(x), words))

def add_prefix_to_words(words):
    return list(map(lambda x : "pre-" + x, words))