#!/usr/bin/env python3

# Fibonacci Sequence Exercise
# TODO: (Read detailed instructions in the Readme file)
# Prompt the user for the number of terms.
# Validate that the input is a positive integer.
# Use a for loop to print the Fibonacci sequence up to that many terms.
import math

input_str = input("Enter an integer for fibonacci sequence: ")


def fibonacci(input_int):
    a = 0
    b = 1
    fibonacci_sequence = []
    for i in range(input_int):
        fibonacci_sequence.append(a)
        print(a)
        a, b = b, a + b
        if len(fibonacci_sequence) >= input_int:
            break

try:
    input_int = int(input_str)
    
    if input_int > 0:
        print("Your enter: ", input_int)
        fibonacci(input_int)
    else:
        print("Please enter a positive integer.")

except ValueError:
    print("Invalid input. Please enter a valid integer!")
