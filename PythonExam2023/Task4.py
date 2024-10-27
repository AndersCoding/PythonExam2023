# Task 4
import random

# Generate a list of 10 random integers between 1 and 50
random_numbers = [random.randint(1, 50) for i in range(10)]

# Function to substitute the square of numbers divisible by 5
def substitute(numbers):
    for i in range(len(numbers)):
        if numbers[i] % 5 == 0:
            numbers[i] = numbers[i] ** 2
    return numbers

# Prints the list before substitution
print("Before substitution, the list is:", random_numbers)

# The substitution function
substituted_numbers = substitute(random_numbers.copy())

# Prints the list after substitution
print("After substitution, the list is:", substituted_numbers)