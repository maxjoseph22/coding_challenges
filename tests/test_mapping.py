from lib.lambda_functions.mapping import *

def test_square_numbers():
    # Given a list of numbers, return their squares
    numbers = [1, 2, 3, 4, 5]
    result = square_numbers(numbers)
    assert result == [1, 4, 9, 16, 25]

def test_uppercase_words():
    # Given a list of words, return the words in uppercase
    words = ["hello", "world", "python"]
    result = uppercase_words(words)
    assert result == ["HELLO", "WORLD", "PYTHON"]

def test_double_numbers():
    # Given a list of numbers, return each number doubled
    numbers = [1, 2, 3, 4]
    result = double_numbers(numbers)
    assert result == [2, 4, 6, 8]

def test_length_of_words():
    # Given a list of words, return their lengths
    words = ["apple", "banana", "cherry"]
    result = length_of_words(words)
    assert result == [5, 6, 6]

def test_add_prefix_to_words():
    # Given a list of words, add the prefix 'pre-' to each word
    words = ["fix", "view", "dict"]
    result = add_prefix_to_words(words)
    assert result == ["pre-fix", "pre-view", "pre-dict"]