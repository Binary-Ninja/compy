"""This file contains the Nibble class."""


def get_value(value: int) -> int:
    """Utility function for validating a given number or Nibble."""
    if 0 <= int(value) <= 15:
        return value
    else:
        raise ValueError("value must be between 0 and 15 (inclusive)")


class Nibble(int):
    """Nibble class for storing hexadecimal values.

    Nibble() -> Nibble(0)

    Nibble(int) -> Nibble(int)
    """
    def __new__(cls, value=0, *args, **kwargs):
        return super(cls, cls).__new__(cls, get_value(value))

    def __repr__(self):
        return f"Nibble({self})"

    def __str__(self):
        return f"{int(self)}"

    def __bool__(self):
        """All values other than zero are True."""
        return super().__bool__()

    def zero(self):
        """not bool(self)"""
        return not super().__bool__()

    def not_zero(self):
        """bool(self)"""
        return super().__bool__()

    def full(self):
        """self >= 15"""
        return self >= 15

    def __eq__(self, other: int):
        """self >= other and other >= self"""
        return self >= other >= self

    def __ne__(self, other: int):
        """not (self >= other) or not (other >= self)"""
        return not self == other

    def __gt__(self, other: int):
        """self >= other and self != other"""
        return self >= other and self != other

    def __lt__(self, other: int):
        """self <= other and self != other"""
        return self <= other and self != other

    def __ge__(self, other: int):
        """Perform the same operation as a comparison comparator.

        Self is the rear input, other is the side input.
        """
        return self if super().__ge__(get_value(other)) else Nibble(0)

    def __le__(self, other: int):
        """Perform the same operation as a comparison comparator.

        Other is the rear input, self is the side input.
        """
        return other >= self

    def __invert__(self):
        """Bitwise NOTs the Nibble.

        This is the same as 15 - Nibble.
        """
        return Nibble(15 - self)

    def __sub__(self, other: int):
        """Perform the same operation as a subtraction comparator.

        Self is the rear input, other is the side input.
        """
        return Nibble(max(0, super().__sub__(get_value(other))))

    def __rsub__(self, other: int):
        """Perform the same operation as a subtraction comparator.

        Other is the rear input, self is the side input.
        """
        return Nibble(max(0, super().__rsub__(get_value(other))))

    def __isub__(self, other: int):
        """Perform the same operation as a subtraction comparator.

        Self is the rear input, other is the side input.
        """
        return self - other
