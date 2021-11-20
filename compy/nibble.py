"""This file contains the Nibble class."""

from typing import Union, NoReturn

Value = Union["Nibble", int]


def get_value(value: Value) -> int:
    """Utility function for validating a given number or Nibble."""
    if not isinstance(value, (Nibble, int)):
        raise ValueError("value must be a Nibble or an integer")
    if isinstance(value, Nibble):
        return value.value
    if 0 <= value <= 15:
        return value
    else:
        raise ValueError("value must be between 0 and 15")


class Nibble:
    """Nibble class for storing hexadecimal values.

    Nibble() -> Nibble(0)

    Nibble(value) -> Nibble(value)

    Nibble(Nibble) -> Nibble(Nibble.value)
    """
    def __init__(self, value: Value = 0):
        self.value = value

    def __repr__(self):
        return f"Nibble({self.value})"

    @property
    def value(self) -> int:
        """The value of the Nibble."""
        return self._value

    @value.setter
    def value(self, value: Value) -> None:
        self._value = get_value(value)

    @value.deleter
    def value(self) -> NoReturn:
        raise SyntaxError("attribute 'value' of Nibble cannot be deleted")

    def __bool__(self):
        """All values other than zero are True."""
        return self.value != 0

    def zero(self):
        """Equivalent to 'not bool(self)'."""
        return self.value == 0

    def not_zero(self):
        """Equivalent to 'bool(self)'."""
        return self.value != 0

    def full(self):
        """Equivalent to 'self > 15'."""
        return self.value == 15

    def __eq__(self, other: Value):
        """Equivalent to 'self > other and other > self'."""
        return self > other > self

    def __ne__(self, other: Value):
        """Equivalent to 'not (self > other) or not (other > self)'."""
        return not self == other

    def __gt__(self, other: Value):
        """Perform the same operation as a comparison comparator.

        Self is the rear input, other is the side input.
        """
        return Nibble() if get_value(other) > self.value else self

    def __lt__(self, other: Value):
        """Perform the same operation as a comparison comparator.

        Other is the rear input, self is the side input.
        """
        return Nibble(other) > self

    def __ge__(self, other: Value):
        """Perform the same operation as a comparison comparator.

        Self is the rear input, other is the side input.
        """
        return self > other

    def __le__(self, other: Value):
        """Perform the same operation as a comparison comparator.

        Other is the rear input, self is the side input.
        """
        return self < other

    def __invert__(self):
        """Bitwise NOTs the Nibble.

        This is the same as 15 - Nibble.
        """
        return Nibble(15 - self.value)

    def __sub__(self, other: Value):
        """Perform the same operation as a subtraction comparator.

        Self is the rear input, other is the side input.
        """
        return Nibble(max(0, self.value - get_value(other)))

    def __rsub__(self, other: Value):
        """Perform the same operation as a subtraction comparator.

        Other is the rear input, self is the side input.
        """
        return Nibble(max(0, get_value(other) - self.value))

    def __isub__(self, other: Value):
        """Perform the same operation as a subtraction comparator.

        Self is the rear input, other is the side input.
        """
        self.value = self - other
        return self
