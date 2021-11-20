"""This file contains functions using comparator logic."""

from typing import Iterable
from nibble import Nibble, Value, get_value

__all__ = [
    "maximum",
    "minimum",
    "subtract",
    "compare",
    "difference",
    "increment",
    "increment_wrap",
]


def maximum(*values: Iterable[Value]):
    """Return the highest value given."""
    return Nibble(max(*values, key=get_value))


def minimum(a: Value, b: Value):
    """Given two values, return the minimum."""
    return ~maximum(~Nibble(a), ~Nibble(b))


def subtract(rear: Value = 0, side_a: Value = 0, side_b: Value = 0):
    """Perform the same operation as a subtraction comparator."""
    return rear - maximum(side_a, side_b)


def compare(rear: Value = 0, side_a: Value = 0, side_b: Value = 0):
    """Perform the same operation as a comparison comparator."""
    return rear >= minimum(side_a, side_b)


def difference(a: Value, b: Value):
    """Return the difference between the values."""
    m = maximum(a, b)
    return maximum(m - a, m - b)


def increment(a: Value):
    """Adds one to the value. 15 + 1 = 15"""
    return ~(14 - a)


def increment_wrap(a: Value):
    """Adds one to the value. 15 + 1 = 0"""
    if a == 15:
        return Nibble(0)
    return increment(a)
