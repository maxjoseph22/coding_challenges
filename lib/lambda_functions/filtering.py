def filter_even_numbers(numbers):
    return list(filter(lambda x : x % 2 == 0, numbers))

def filter_words_starting_with_vowel(words):
    vowels = "aeiou"
    return list(filter(lambda x : x[0] in vowels, words))

def filter_positive_numbers(numbers):
    return list(filter(lambda x : x > 0, numbers))

def filter_long_words(words):
    return list(filter(lambda x : len(x) > 5, words))

def filter_numbers_divisible_by_3(numbers):
    return list(filter(lambda x : x % 3 == 0, numbers))