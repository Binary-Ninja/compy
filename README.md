# compy
A python library for working with combinational logic for Minecraft's redstone comparators.

The standard for computing in Minecraft is with binary logic. However, by utilizing redstone signal
strength, analog hexadecimal computers are possible. These are a very different flavor from their binary
cousins, and hexadecimal circuits can be extremely compact and fast in comparison. However, it can be more
difficult to create complex logic circuits and keep track of all the signals. `compy` was designed to make
hexadecimal computing easier by smoothing the design process of hexadecimal circuits.

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

Inside the package itself there are two main modules, `nibble.py` and `functions.py`. `nibble.py` contains
the class that represents a single hexadecimal digit. This class has some basic functionality. Read the
included documentation strings to figure out what it can do. `functions.py` is for more advanced circuits
wrapped into functions, so they can be reused. Everything in the modules is carefully designed to be
possible with redstone. The more complex circuits can be broken down into smaller steps, allowing great
modularity in design.

### Examples
Let's create a simple circuit that adds two Nibbles.
```python
def add(a, b):
    return ~(~a - b)
```
This simple adder function will return a Nibble with a value of `a + b` if `a + b` is less than 15.
If the result is over 15, the function will just return 15 regardless.

The `-` operator will perform a comparator subtraction, with the Nibble on the left assumed to be the
rear input, and the Nibble on the right assumed to be the side input. For three input subtraction, use the
`subtract` function in the `functions` module.

The `~` operator is a bitwise NOT, which is the same as `15 - Nibble`.

This means the circuit above can
also be represented as `15 - (15 - a - b)`. Simplifying this mathematically gets us `15 - 15 + a + b`, or
`a + b`. This is how addition is possible by only using subtraction.

The use of operator overloading provides a clean, understandable syntax in just a few characters.
This is not an exhaustive reference; both modules have more functionality than shown or discussed here.
Download the library for yourself to add new functions and create complex circuits!

## Development
`compy` was developed in Python 3.9.7 and may not work on earlier versions of Python.
There is NO Python 2 support.

## Release History
- 1.0
  - First version

## License
`compy` is distributed under the GNU Lesser General Public License.

This means that you can use the code however you want, but if you publish a modified version of this code,
the code must be open source.

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
