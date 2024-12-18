# PyAss

[![Testing if all example files work](https://github.com/CrestFallenTurtle/PyAss/actions/workflows/example_files.yml/badge.svg)](https://github.com/CrestFallenTurtle/PyAss/actions/workflows/example_files.yml) [![Testing backend](https://github.com/CrestFallenTurtle/PyAss/actions/workflows/test_backend.yml/badge.svg)](https://github.com/CrestFallenTurtle/PyAss/actions/workflows/test_backend.yml)

![Boris The Snake](images/output.jpg)



## Syntax and program layout

### Variable Declaration
Within each program there is a dedicated section where the programmer can declare all variables that will be utilized
during the programs execution and lifetime. This area begins with a `WAKE UP` followed by a simple variable declaration as can be seen in multiple languages.

#### Example
```
WAKE UP
 A = 10
 B = 20
 C = 30

...
```
The declaration area will continue until the function declaration area is declared.

No function calls are allowed to take place within this section, and are reserved to the function declaration and the main declaration.

### Function Declaration
Method/functions can only be declared within the `EVERYDAY I WAKE UP` section, variables are not allowed to be declared here.

#### Example
```
EVERYDAY I WAKE UP

    foo:
        print $str
        add $a, $b, $c

    boo:
        print $c
```

### Main loop Declaration
All of the meat of the program should primarly be reserved to the main loop, `PIECE OF SHIT`. Nothing can be definied in this section, and that should be reserved for the variable and method declaration sections.

#### Example
```
PIECE OF SHIT
    gtfo foo, boo
```

### Exiting loop Declaration
The exiting loop, `FUCK THIS SHIT`, is left to be utilized by the user in order to do some last minute things before the software exits. Nothing can be definied in this section, and that should be reserved for the variable and method declaration sections.


```
FUCK THIS SHIT
    print "I'm out of here"
```

### Program Layout

### Available syntaxes
General operators
| Function         | Description     | Example |
|--------------|-----------|-----------|
| `print` | Prints the provides value/s | `print $a, $c, "Hello"` |
| `obtain`| Takes a user input, and saves it in a variable  | `obtain $a` |
| `ass`| Assigns the provided value into one or more variables during runtime | `ass 69, $a, $b` |
| `judge`| Compares two values, and jumps to one of the corresponding methods as a result | `judge $a, $b, foo, boo` |
| `length`| Provides the length of a variable, and places it in the last provided variable | `length $a, $b` |
| `index`| Indexes the provided variable at the provided index, and places the result in the last provided variable | `index $a, 2, $b` |

Bitwise operators
| Function         | Description     | Example |
|--------------|-----------|-----------|
| `band` | Bitwise And, results are placed in the last provided variable  | `band $a, $b, $c` |
| `bor`| Bitwise Or, results are placed in the last provided variable  | `bor $a, $b, $c` |
| `bxor`| Bitwise Xor, results are placed in the last provided variable  | `bxor $a, $b, $c` |
| `lshift`| Bitwise left shift, results are placed in the last provided variable | `lshift $a, $b, $c` |
| `rshift`| Bitwise right shift, results are placed in the last provided variable | `rshift $a, $b, $c` |
| `bnot`| Bitwise not, results are placed in the last provided variable | `bnot $a, $c` |

Math operators
| Function         | Description     | Example |
|--------------|-----------|-----------|
| `add` | Adds two values, results are placed in the last provided variable | `add $a, $b, $c` |
| `sub`| Subs two values, results are placed in the last provided variable | `sub $a, $b, $c` |
| `mult`| Multiplies two values, results are placed in the last provided variable | `mult $a, $b, $c` |
| `div`| Divides two values, results are placed in the last provided variable | `div $a, $b, $c` |
| `mod`| Performs a modular operation on two values, results are placed in the last provided variable | `mod $a, $b, $c` |
| `inc`| Increments the value of one or more variables by one | `inc $a, $b, $c` |
| `dec`| Decrement the value of one or more variables by one | `dec $a, $b, $c` |

String operators
| Function         | Description     | Example |
|--------------|-----------|-----------|
| `marriage` | Combines two the values of two strings, and saves it in the first variable | `marriage $a, $b` |
| `divorce` | Splits a string into n-pieces based on a provided delimiter, the results are saved in the second parameter sent in | `divorce $a, $b, " "` |
| `strip` | Removes the second argument from the first argument | `strip $a, "World"` |
| `remarriage` | Replaces a value within a given string | `remarriage $str1, "no", $str2` |

### Example program
```
WAKE UP
    str="Hello World"
    a=10
    b=20
    c=0

EVERYDAY I WAKE UP

    foo:
        print $str
        add $a, $b, $c

    boo:
        print $c

PIECE OF SHIT
    gtfo foo, boo

FUCK THIS SHIT

```
