import random
from data_utils import mean, median, mode

# Generate a random list of numbers
random_numbers = [random.randint(1, 100) for _ in range(20)] 

# Display the generated list
print("Generated List of Numbers:", random_numbers)

print("Mean:", mean(random_numbers))
print("Median:", median(random_numbers))
print("Mode:", mode(random_numbers))
