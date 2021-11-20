#!/usr/bin/env python3

from __init__ import *

# Create a basic adder that takes in two nibbles and outputs a nibble and a carry flag.


def add1(a, b):
    return ~(~a - b)


def add2(a, b):
    return maximum(a, b) - maximum(~a, ~b)


def carry(a1, a2):
    return a1.full() and a2


def add(a, b):
    """Add two Nibbles together.

    Takes in two values.
    Returns a tuple of (carry, result).
    """
    a, b = Nibble(a), Nibble(b)  # Convert to Nibbles.
    a1, a2 = add1(a, b), add2(a, b)  # Calculate the intermediate steps.
    return (FULL, a2 - 1) if carry(a1, a2) else (ZERO, a1)  # Final logic.


def main():
    a = int(input("First value? "))
    b = int(input("Second value? "))
    result = add(a, b)
    print(f"Result: {result[1].value} with a carry of {1 if result[0] else 0}.")


if __name__ == "__main__":
    main()
