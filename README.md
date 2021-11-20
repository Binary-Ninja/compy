# compy
A python library for working with combinational logic for Minecraft's redstone comparators.

The standard for computing in Minecraft is with binary logic. However, by utilizing redstone signal
strength, analog hexadecimal computers are possible. These are a very different flavor from their binary
cousins, and hexadecimal circuits can be extremely compact and fast in comparison. However, it can be
more difficult to create complex logic circuits and keep track of all the signals. `compy` was designed
to make hexadecimal computing easier by smoothing the design process of hexadecimal circuits.

## Installation
`compy` is designed to be a playground package, so it is recommended to install from source. Just clone
the repository and start designing!

## Usage
The intended way to use this package is by playing around in the code itself.
There is an adder circuit that comes with the package in `__main__.py`. Simply run the package as you
would a python file and the `__main__.py` file will be executed.
```shell
python compy
```
Depending on your system, you may need to replace `python` with `python3` when executing this way.

Inside the package itself there are two main modules, `nibble.py` and `functions.py`. `nibble.py`
contains the class that represents a single hexadecimal digit. This class has some basic functionality.
Read the included documentation strings to figure out what it can do. `functions.py` is for more advanced
circuits wrapped into functions, so they can be reused. Everything in the modules is carefully designed
to be possible with redstone. The more complex circuits can be broken down into smaller steps, allowing
great modularity in design.

### Tutorial
```python
from compy import *

ZERO == Nibble(0) # True
FULL == Nibble(15) # True
```
When importing `compy` as a package, the Nibble class and all functions from `functions.py` will be
exported. Additionally, two Nibbles named `ZERO` and `FULL` are exported with the values `0` and `15`
respectively.

The backbone of `compy` is the `Nibble` class. A nibble can be created in the following ways.
```python
from compy import *

a = Nibble() # Default value is zero.
b = Nibble(5) # Create Nibble with signal strength 5.
c = Nibble(b) # Create Nibble with value of another Nibble.
print(c) # Output: "Nibble(5)"
```
Nibbles can be compared and subtracted according to comparator rules.
```python
from compy import *

a = Nibble(10)
b = Nibble(15)
print(b - a) # Comparator subtract. The left operand is the rear input. Output: "Nibble(5)"
print(b >= a) # Comparator comparison. The left operand is the rear input. Output: "Nibble(15)"
print(b <= a) # Equivalent to a >= b. Output: "Nibble(0)"
```
Nibbles also support in-place subtraction with the `-=` operator.

The `>=` operator performs a rich comparison, returning a nibble value.
If `a` is larger than `b`, the expression will return `Nibble(0)`, otherwise it will return `Nibble(b)`.

To simulate comparators with three inputs, use the `compare` and `subtract` functions in `functions.py`.

Nibbles have more convenience functions built in.
```python
from compy import *

a = Nibble(15)

print(bool(a)) # All non-zero Nibbles are considered truthy. Output: "True"
print(a.not_zero()) # Same as "bool(a)". Output: "True"
print(a.zero()) # Same as "not bool(a)". Output: "False"
print(a.full()) # True if a == 15. Equivalent to a >= 15. Output: "True"

print(a == 10) # Equivalent to a >= 10 and 10 >= a. Output: "False"
print(a != 10) # Equivalent to not (a >= 10) or not (10 >= a). Output: True""

print(a > 10) # Equivalent to a >= 10 and a != 10. Output: "True"
print(a < 10) # Equivalent to a <= 10 and a != 10. Output: "False"

print(~a) # Bitwise NOT. Equivalent to 15 - a. Output: "Nibble(0)"
```
Here is a simple adder circuit.
```python
def add(a, b):
    return ~(~a - b)
```
This circuit will take in two nibbles and output the sum. If the result is too large to fit into one
nibble, then the max nibble of 15 is returned.

Because the NOT operator is equivalent to 15 - nibble, this circuit can be simplified mathematically to
`15 - (15 - a - b)`. This can be expanded to `15 - 15 + a + b`, which can be simplified to `a + b`.
This is how simple addition can be accomplished with just comparator logic.

## Development
`compy` was developed in Python 3.9.7 and may not work on earlier versions of Python.
There is NO Python 2 support.

## Release History
- 1.1
  - ADD: `difference`, `increment`, `increment_wrap` functions added to `functions.py`
  - MOD: `>` and `<` operators now perform as expected, instead of comparing like `>=` and `<=`
- 1.0
  - First version

## License
`compy` is distributed under the GNU Lesser General Public License.

This means that you can use the code however you want, but if you publish a modified version of this
code, the code must be open source.

    compy - A library for working with combinational logic for Minecraft's redstone comparators.
    Copyright (C) 2021  https://github.com/Binary-Ninja

    This library is free software; you can redistribute it and/or
    modify it under the terms of the GNU Lesser General Public
    License as published by the Free Software Foundation; either
    version 2.1 of the License, or (at your option) any later version.

    This library is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
    Lesser General Public License for more details.

    You should have received a copy of the GNU Lesser General Public
    License along with this library; if not, write to the Free Software
    Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301
    USA
