"""This file contains functions using comparator logic."""

from typing import Iterable
from nibble import Nibble, Value, get_value


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
    return rear > minimum(side_a, side_b)
