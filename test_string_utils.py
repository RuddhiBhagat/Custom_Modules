# test_string_utils.py

# Importing functions from the string_utils module
from string_utils import reverse_string, is_palindrome, capitalize_words

# Test the functions
test_string = input("Enter a String that to be reversed: ")
print("Reversed String:", reverse_string(test_string))
print(f"Is '{test_string}' a palindrome?", is_palindrome(test_string))

test_string2 = input("Enter a string that need to capitalized:")
print("Original String:", test_string2)
print("Capitalized Words:", capitalize_words(test_string2))

test_string3 = "racecar"
print(f"Is '{test_string3}' a palindrome?", is_palindrome(test_string3))
