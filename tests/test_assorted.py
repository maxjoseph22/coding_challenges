from lib.lambda_functions.assorted import *
from functools import reduce

def test_filter_palindromes():
    # Given a list of words, filter out only the palindromes
    words = ["madam", "python", "racecar", "hello", "level"]
    result = filter_palindromes(words)
    assert result == ["madam", "racecar", "level"]

def test_map_celsius_to_fahrenheit():
    # Convert a list of temperatures from Celsius to Fahrenheit
    celsius_temps = [0, 25, 100]
    result = map_celsius_to_fahrenheit(celsius_temps)
    assert result == [32, 77, 212]

def test_reduce_find_longest_word():
    # Given a list of words, find the longest word
    words = ["short", "longer", "longest", "tiny"]
    result = reduce_find_longest_word(words)
    assert result == "longest"

def test_filter_numbers_within_range():
    # Filter numbers within a specified range (inclusive)
    numbers = [1, 5, 8, 12, 20, 25]
    result = filter_numbers_within_range(numbers, 5, 20)
    assert result == [5, 8, 12, 20]

def test_map_square_and_convert_to_string():
    # Square each number in the list and return them as strings
    numbers = [1, 2, 3, 4]
    result = map_square_and_convert_to_string(numbers)
    assert result == ["1", "4", "9", "16"]