#!/usr/bin/env python3
def fibonacci_sequence():
  while True:
    try:
      n = int(input("Enter number of terms of the fibonacci sequence: "))

      if n <= 0:
        print("Enter a positive integer")
        continue

      a, b =  0, 1
      print("\nfibonacci_sequence:")
      for _ in range(n):
        print(a, end=" ")
        a, b = b, a + b
        print()
      break

    except ValueError:
      print("Invalid integer, please enter a positive integer")

fibonacci_sequence()
# Fibonacci Sequence Exercise
# TODO: (Read detailed instructions in the Readme file)
# Prompt the user for the number of terms.
# Validate that the input is a positive integer.
# Use a for loop to print the Fibonacci sequence up to that many terms.
