# test_my_utils.py

from my_utils.math_utils import is_prime
from my_utils.string_utils import count_vowels

# Test the is_prime function
number = 29
print(f"Is {number} prime? {is_prime(number)}")

# Test the count_vowels function
text = "Hello, World!"
print(f"The number of vowels in '{text}' is: {count_vowels(text)}")
