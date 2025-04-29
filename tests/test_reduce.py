from functools import reduce
from lib.lambda_functions.reduce import *

def test_sum_of_squares():
    # Calculate the sum of squares of numbers in the list
    numbers = [1, 2, 3, 4]
    result = sum_of_squares(numbers)
    assert result == 30  # 1^2 + 2^2 + 3^2 + 4^2 = 30

def test_concatenate_strings():
    # Concatenate a list of strings into one long string
    strings = ["hello", "world", "python"]
    result = concatenate_strings(strings)
    assert result == "helloworldpython"

def test_find_maximum():
    # Find the maximum number in the list
    numbers = [3, 7, 2, 9, 4]
    result = find_maximum(numbers)
    assert result == 9

def test_product_of_numbers():
    # Calculate the product of all numbers in the list
    numbers = [1, 3, 5, 7]
    result = product_of_numbers(numbers)
    assert result == 105  # 1 * 3 * 5 * 7 = 105

def test_find_longest_string():
    # Find the longest string in a list
    strings = ["short", "longer", "lengthiest", "tiny"]
    result = find_longest_string(strings)
    assert result == "lengthiest"