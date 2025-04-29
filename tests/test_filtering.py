from lib.lambda_functions.filtering import *

def test_filter_even_numbers():
    # Given a list of numbers, filter out only the even numbers
    numbers = [1, 2, 3, 4, 5, 6]
    result = filter_even_numbers(numbers)
    assert result == [2, 4, 6]

def test_filter_words_starting_with_vowel():
    # Given a list of words, filter out words that start with a vowel
    words = ["apple", "banana", "orange", "umbrella", "grape"]
    result = filter_words_starting_with_vowel(words)
    assert result == ["apple", "orange", "umbrella"]

def test_filter_positive_numbers():
    # Given a list of integers, filter out only the positive numbers
    numbers = [-10, -1, 0, 3, 7, -5]
    result = filter_positive_numbers(numbers)
    assert result == [3, 7]

def test_filter_long_words():
    # Given a list of words, filter out words with more than 5 characters
    words = ["short", "longer", "tiny", "elephant", "big"]
    result = filter_long_words(words)
    assert result == ["longer", "elephant"]

def test_filter_numbers_divisible_by_3():
    # Given a list of integers, filter out numbers divisible by 3
    numbers = [3, 4, 5, 9, 12, 17]
    result = filter_numbers_divisible_by_3(numbers)
    assert result == [3, 9, 12]