"""This file contains functions using comparator logic."""

from nibble import Nibble

__all__ = [
    "maximum",
    "minimum",
    "subtract",
    "compare",
    "difference",
    "increment",
    "increment_wrap",
]


def maximum(*values: int):
    """Return the highest value given."""
    return Nibble(max(*values))


def minimum(a: int, b: int):
    """Given two values, return the minimum."""
    return ~maximum(~Nibble(a), ~Nibble(b))


def subtract(rear: int = 0, side_a: int = 0, side_b: int = 0):
    """Perform the same operation as a subtraction comparator."""
    return Nibble(rear) - maximum(side_a, side_b)


def compare(rear: int = 0, side_a: int = 0, side_b: int = 0):
    """Perform the same operation as a comparison comparator."""
    return Nibble(rear) >= minimum(side_a, side_b)


def difference(a: int, b: int):
    """Return the difference between the values."""
    m = maximum(a, b)
    return maximum(m - a, m - b)


def increment(a: int):
    """Adds one to the value. 15 + 1 = 15"""
    return ~(14 - Nibble(a))


def increment_wrap(a: int):
    """Adds one to the value. 15 + 1 = 0"""
    if a >= 15:
        return Nibble(0)
    return increment(a)
