# Uteis Package

## Overview
Uteis is a Python package that provides utility functions for numerical operations, string manipulations, and color palette management. It is designed to simplify common tasks in these areas.

## Installation
You can install Uteis using pip. Run the following command in your terminal:

```
pip install Uteis
```

## Sub-packages

### Números
The `números` sub-package contains functions for basic arithmetic operations. It includes the following functions:
- `add(a, b)`: Returns the sum of `a` and `b`.
- `subtract(a, b)`: Returns the difference of `a` and `b`.
- `multiply(a, b)`: Returns the product of `a` and `b`.
- `divide(a, b)`: Returns the quotient of `a` and `b`.

### Strings
The `strings` sub-package provides functions for manipulating strings. It includes the following functions:
- `to_upper(s)`: Converts the string `s` to uppercase.
- `to_lower(s)`: Converts the string `s` to lowercase.
- `capitalize(s)`: Capitalizes the first letter of the string `s`.
- `reverse(s)`: Reverses the string `s`.

### Cores
The `cores` sub-package offers functions related to color palettes. It includes the following functions:
- `get_palette(name)`: Returns a color palette based on the given name.
- `mix_colors(color1, color2)`: Mixes two colors and returns the resulting color.
- `color_to_hex(color)`: Converts a color to its hexadecimal representation.

## Usage Example
Here is a simple example of how to use the Uteis package:

```python
from uteis.numeros.operations import add
from uteis.strings.manipulations import to_upper
from uteis.cores.palette import get_palette

result = add(5, 3)
print(result)  # Output: 8

upper_string = to_upper("hello")
print(upper_string)  # Output: HELLO

palette = get_palette("default")
print(palette)  # Output: [list of colors]
```

## Contributing
Contributions are welcome! Please feel free to submit a pull request or open an issue for any suggestions or improvements.

## License
This project is licensed under the MIT License. See the LICENSE file for more details.