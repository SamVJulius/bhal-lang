# 🐻 bhal-lang

A custom interpreted programming language built in Python, with a quirky `BH`-prefixed keyword system. bhal-lang is an expression-oriented, dynamically-typed scripting language that supports variables, arithmetic, comparisons, control flow, functions, and lists — all with its own unique syntax flavor.

---

## Table of Contents

1. [Getting Started](#getting-started)
2. [Running bhal-lang](#running-bhal-lang)
3. [Language Overview](#language-overview)
4. [Data Types](#data-types)
5. [Variables](#variables)
6. [Operators](#operators)
7. [Comments](#comments)
8. [Control Flow](#control-flow)
   - [If / Elif / Else](#if--elif--else)
   - [For Loop](#for-loop)
   - [While Loop](#while-loop)
9. [Functions](#functions)
10. [Lists](#lists)
11. [Built-in Functions & Constants](#built-in-functions--constants)
12. [Error Types](#error-types)
13. [Keyword Reference](#keyword-reference)
14. [Full Examples](#full-examples)

---

## Getting Started

### Requirements

- Python 3.x

### Project Files

| File | Description |
|------|-------------|
| `basic.py` | The core interpreter — lexer, parser, and evaluator |
| `shell.py` | Interactive REPL shell |
| `strings_with_arrows.py` | Utility for pretty error messages |
| `grammar.txt` | Formal grammar definition |
| `test.txt` | Sample program demonstrating functions, loops, and lists |
| `test2.txt` | Sample program demonstrating functions and for loops |

---

## Running bhal-lang

### Interactive REPL

Start the interactive shell by running:

```bash
python shell.py
```

You will see the prompt:

```
bhal-lang >
```

Type any bhal-lang expression and press Enter to evaluate it.

```
bhal-lang > BHRINT("Hello, world!")
Hello, world!

bhal-lang > BHAR x = 10 + 5
bhal-lang > BHRINT(x)
15
```

### Running a Script File

From within the REPL, use the `BHUN` built-in to execute a `.txt` script file:

```
bhal-lang > BHUN("test.txt")
```

---

## Language Overview

bhal-lang is an **expression-oriented** language. Almost every construct — including `if`, `for`, `while`, and function definitions — is an expression and returns a value.

Keywords follow a consistent `BH` prefix pattern (short for **bhal**), giving the language its distinctive style.

---

## Data Types

bhal-lang has three primitive types and one compound type:

| Type | Description | Example |
|------|-------------|---------|
| `INT` | Whole numbers | `42`, `-7`, `0` |
| `FLOAT` | Decimal numbers | `3.14`, `-0.5` |
| `STRING` | Text, double-quoted | `"hello"`, `"bhal-lang"` |
| `LIST` | Ordered collection of values | `[1, 2, "three"]` |

### Booleans

There is no dedicated boolean type. Truthiness follows these rules:

- **Number**: `0` is falsy, any other number is truthy
- **String**: empty string `""` is falsy, non-empty is truthy
- Two built-in constants act as boolean aliases:

```
BHRUE    # equivalent to 1 (true)
BHALSE   # equivalent to 0 (false)
BHULL    # null / no value (0)
```

### String Escape Sequences

Inside strings, you can use:

| Escape | Meaning |
|--------|---------|
| `\n` | Newline |
| `\t` | Tab |
| `\\` | Literal backslash |

```
BHRINT("Line one\nLine two")
```

---

## Variables

Variables are declared and assigned using the `BHAR` keyword.

**Syntax:**
```
BHAR <name> = <expression>
```

Variables are **dynamically typed** — the type is determined by the value assigned, and can change on reassignment.

```
BHAR name = "bhal"
BHAR count = 10
BHAR ratio = 3.14
BHAR items = [1, 2, 3]
```

To reassign an already-declared variable, use `BHAR` again:

```
BHAR x = 5
BHAR x = x + 1    # x is now 6
```

> **Note:** Variables are scoped. Functions create a new scope that inherits from the parent scope, but assignments inside a function don't affect the outer scope.

---

## Operators

### Arithmetic Operators

| Operator | Description | Example |
|----------|-------------|---------|
| `+` | Addition (numbers) / Concatenation (strings) | `3 + 4` → `7`, `"a" + "b"` → `"ab"` |
| `-` | Subtraction | `10 - 3` → `7` |
| `*` | Multiplication | `4 * 5` → `20` |
| `/` | Division | `10 / 4` → `2.5` |
| `^` | Exponentiation | `2 ^ 8` → `256` |

Division by zero raises a runtime error.

```
BHAR result = (2 + 3) * 4 ^ 2   # 80
```

### Comparison Operators

| Operator | Description |
|----------|-------------|
| `==` | Equal to |
| `!=` | Not equal to |
| `<` | Less than |
| `>` | Greater than |
| `<=` | Less than or equal |
| `>=` | Greater than or equal |

```
BHRINT(5 == 5)    # 1
BHRINT(3 != 4)    # 1
BHRINT(10 > 20)   # 0
```

### Logical Operators

| Keyword | Description |
|---------|-------------|
| `BHAND` | Logical AND |
| `BHOR` | Logical OR |
| `BHOT` | Logical NOT |

```
BHRINT(BHRUE BHAND BHALSE)   # 0
BHRINT(BHRUE BHOR BHALSE)    # 1
BHRINT(BHOT BHRUE)            # 0
```

### List Operators

The arithmetic operators have special meanings when applied to lists:

| Operator | On List | Description |
|----------|---------|-------------|
| `+` | `list + value` | Appends `value` to list, returns new list |
| `-` | `list - index` | Removes element at `index`, returns new list |
| `*` | `list * list` | Concatenates two lists, returns new list |
| `/` | `list / index` | Retrieves the element at `index` |

```
BHAR nums = [10, 20, 30]
BHRINT(nums / 0)    # 10
BHRINT(nums / 2)    # 30
```

---

## Comments

Single-line comments start with `#`. Everything after `#` on the same line is ignored.

```
# This is a comment
BHAR x = 42    # inline comment
```

---

## Control Flow

### If / Elif / Else

#### One-liner form

```
BHIF <condition> BHEN <statement>
```

```
BHIF x > 0 BHEN BHRINT("positive")
```

#### One-liner with else

```
BHIF <condition> BHEN <statement> BHELSE <statement>
```

```
BHIF x > 0 BHEN BHRINT("positive") BHELSE BHRINT("not positive")
```

#### Multi-line block form

```
BHIF <condition> BHEN
    <statements>
BHEND
```

```
BHIF score >= 90 BHEN
    BHRINT("A grade")
BHELIF score >= 75 BHEN
    BHRINT("B grade")
BHELIF score >= 60 BHEN
    BHRINT("C grade")
BHELSE
    BHRINT("Failing")
BHEND
```

The `if` expression returns the value of the branch that was executed.

```
BHAR label = BHIF x > 0 BHEN "positive" BHELSE "non-positive"
```

---

### For Loop

Iterates a counter variable from a start value **up to** (but not including) an end value.

#### One-liner form

```
BHFOR <var> = <start> BHO <end> BHEN <statement>
```

```
BHFOR i = 0 BHO 5 BHEN BHRINT(i)
```

#### With optional step

```
BHFOR <var> = <start> BHO <end> BHEP <step> BHEN <statement>
```

```
BHFOR i = 0 BHO 10 BHEP 2 BHEN BHRINT(i)   # prints 0, 2, 4, 6, 8
BHFOR i = 5 BHO 0 BHEP -1 BHEN BHRINT(i)   # counts down: 5, 4, 3, 2, 1
```

#### Multi-line block form

```
BHFOR <var> = <start> BHO <end> BHEN
    <statements>
BHEND
```

```
BHFOR i = 1 BHO 6 BHEN
    BHAR squared = i * i
    BHRINT(squared)
BHEND
```

> A for loop used as an expression (one-liner form) returns a list of all values produced by its body.

---

### While Loop

Repeats a block as long as the condition is truthy.

#### One-liner form

```
BHILE <condition> BHEN <statement>
```

```
BHILE running BHEN BHRINT("still going")
```

#### Multi-line block form

```
BHILE <condition> BHEN
    <statements>
BHEND
```

```
BHAR n = 1
BHILE n <= 5 BHEN
    BHRINT(n)
    BHAR n = n + 1
BHEND
```

### Loop Control

| Keyword | Description |
|---------|-------------|
| `BHONTINUE` | Skip to the next iteration |
| `BHREAK` | Exit the loop immediately |

```
BHFOR i = 0 BHO 10 BHEN
    BHIF i == 3 BHEN BHONTINUE
    BHIF i == 7 BHEN BHREAK
    BHRINT(i)
BHEND
# Prints: 0, 1, 2, 4, 5, 6
```

---

## Functions

Functions are defined using the `BHUNC` keyword.

### Named function (block form)

```
BHUNC <name>(<param1>, <param2>, ...)
    <statements>
    BHETURN <value>
BHEND
```

```
BHUNC greet(name)
    BHETURN "Hello, " + name + "!"
BHEND

BHRINT(greet("world"))    # Hello, world!
```

### One-liner arrow function

Uses `->` to define a single-expression function body. The expression's value is automatically returned.

```
BHUNC <name>(<params>) -> <expression>
```

```
BHUNC square(x) -> x * x
BHRINT(square(5))    # 25

BHUNC add(a, b) -> a + b
BHRINT(add(3, 4))    # 7
```

### Anonymous (lambda) functions

Omit the name to create an anonymous function. Useful for passing as arguments.

```
BHAR double = BHUNC(x) -> x * 2
BHRINT(double(6))    # 12
```

### Returning values

Use `BHETURN` to return a value from a multi-line function. A bare `BHETURN` (no expression) returns `BHULL` (null).

```
BHUNC abs_val(n)
    BHIF n < 0 BHEN
        BHETURN -n
    BHEND
    BHETURN n
BHEND
```

### Functions as first-class values

Functions can be stored in variables and passed as arguments:

```
BHUNC apply(func, value) -> func(value)

BHUNC triple(x) -> x * 3
BHRINT(apply(triple, 7))    # 21
```

---

## Lists

Lists are ordered, zero-indexed collections created with square brackets `[...]`.

```
BHAR fruits = ["apple", "banana", "cherry"]
BHAR mixed = [1, "two", 3.0, [4, 5]]
BHAR empty = []
```

### Indexing

Use the `/` operator to access elements by index:

```
BHAR nums = [10, 20, 30]
BHRINT(nums / 0)    # 10
BHRINT(nums / 2)    # 30
```

### Modifying lists with built-ins

```
BHAR items = [1, 2, 3]

BHAPPEND(items, 4)           # items is now [1, 2, 3, 4]
BHOP(items, 0)               # removes and returns item at index 0
BHEXTEND(items, [10, 11])    # merges another list into items
BHRINT(BHLEN(items))         # prints the number of elements
```

---

## Built-in Functions & Constants

### Constants

| Name | Value | Description |
|------|-------|-------------|
| `BHULL` | `0` | Null / no value |
| `BHRUE` | `1` | Boolean true |
| `BHALSE` | `0` | Boolean false |
| `BHATH_BHI` | `3.14159…` | Mathematical constant π |

### I/O Functions

| Function | Signature | Description |
|----------|-----------|-------------|
| `BHRINT` | `BHRINT(value)` | Prints `value` to stdout |
| `BHRINT_RET` | `BHRINT_RET(value)` | Returns the string representation of `value` without printing |
| `BHINPUT` | `BHINPUT()` | Reads a line of text from stdin, returns a string |
| `BHINPUT_INT` | `BHINPUT_INT()` | Reads from stdin, re-prompts until a valid integer is entered |

```
BHAR name = BHINPUT()
BHRINT("Hello, " + name)

BHAR age = BHINPUT_INT()
BHRINT("You are " + BHRINT_RET(age) + " years old")
```

### Type-checking Functions

| Function | Signature | Returns |
|----------|-----------|---------|
| `BHIS_BHUM` | `BHIS_BHUM(value)` | `1` if value is a number, else `0` |
| `BHIS_STR` | `BHIS_STR(value)` | `1` if value is a string, else `0` |
| `BHIS_BHIST` | `BHIS_BHIST(value)` | `1` if value is a list, else `0` |
| `BHIS_BHUN` | `BHIS_BHUN(value)` | `1` if value is a function, else `0` |

```
BHRINT(BHIS_BHUM(42))           # 1
BHRINT(BHIS_STR("hello"))       # 1
BHRINT(BHIS_BHIST([1, 2, 3]))   # 1
```

### List Functions

| Function | Signature | Description |
|----------|-----------|-------------|
| `BHAPPEND` | `BHAPPEND(list, value)` | Appends `value` to the end of `list` (mutates in place) |
| `BHOP` | `BHOP(list, index)` | Removes and returns the element at `index` |
| `BHEXTEND` | `BHEXTEND(listA, listB)` | Appends all elements of `listB` into `listA` (mutates in place) |
| `BHLEN` | `BHLEN(list)` | Returns the number of elements in `list` |

```
BHAR data = [3, 1, 4]
BHAPPEND(data, 1)
BHAPPEND(data, 5)
BHPRINT(BHLEN(data))    # 5

BHAR removed = BHOP(data, 0)
BHRINT(removed)          # 3
```

### Utility Functions

| Function | Signature | Description |
|----------|-----------|-------------|
| `BHLEAR` / `CLS` | `BHLEAR()` | Clears the terminal screen |
| `BHUN` | `BHUN(filename)` | Loads and executes a bhal-lang script file |

```
BHUN("test.txt")          # runs the script at test.txt
BHLEAR()                  # clears the screen
```

---

## Error Types

bhal-lang reports errors with the file name, line number, and a visual arrow pointing to the problematic token.

| Error | When it occurs |
|-------|---------------|
| `Illegal Character` | A character the lexer doesn't recognise (e.g., `@`, `$`) |
| `Expected Character` | A character that must follow another wasn't found (e.g., `!` not followed by `=`) |
| `Invalid Syntax` | The token sequence doesn't match any valid grammar rule |
| `Runtime Error` | An error that occurs during execution (e.g., division by zero, undefined variable, wrong argument count) |

Runtime errors include a **traceback** showing the call stack:

```
Traceback (most recent call last):
  File test.txt, line 3, in <program>
  File test.txt, line 1, in myFunc
Runtime Error: Division by zero
```

---

## Keyword Reference

All reserved keywords in bhal-lang:

| Keyword | Role |
|---------|------|
| `BHAR` | Variable declaration / assignment |
| `BHIF` | If condition |
| `BHELIF` | Else-if condition |
| `BHELSE` | Else branch |
| `BHEN` | Then (used after conditions in `if`/`for`/`while`) |
| `BHEND` | Closes a multi-line block |
| `BHFOR` | For loop |
| `BHO` | To (range end in for loop) |
| `BHEP` | Step (increment in for loop) |
| `BHILE` | While loop |
| `BHUNC` | Function definition |
| `BHETURN` | Return from function |
| `BHONTINUE` | Continue to next loop iteration |
| `BHREAK` | Break out of loop |
| `BHAND` | Logical AND |
| `BHOR` | Logical OR |
| `BHOT` | Logical NOT |

---

## Full Examples

### Hello World

```
BHRINT("Hello, world!")
```

### FizzBuzz

```
BHFOR i = 1 BHO 101 BHEN
    BHIF i * (i % 15 == 0) BHEN
        BHRINT("FizzBuzz")
    BHELIF i % 3 == 0 BHEN
        BHRINT("Fizz")
    BHELIF i % 5 == 0 BHEN
        BHRINT("Buzz")
    BHELSE
        BHRINT(i)
    BHEND
BHEND
```

### Fibonacci Sequence

```
BHUNC fib(n)
    BHIF n <= 1 BHEN BHETURN n
    BHETURN fib(n - 1) + fib(n - 2)
BHEND

BHFOR i = 0 BHO 10 BHEN
    BHRINT(fib(i))
BHEND
```

### Joining a List (from `test.txt`)

```
# Joins list elements into a string with a separator
BHUNC join(elements, separator)
    BHAR result = ""
    BHAR len = BHLEN(elements)

    BHFOR i = 0 BHO len BHEN
        BHAR result = result + elements/i
        BHIF i != len - 1 BHEN BHAR result = result + separator
    BHEND

    BHETURN result
BHEND

BHRINT(join(["a", "b", "c"], ", "))    # a, b, c
```

### Higher-Order Functions (from `test.txt`)

```
# One-liner function
BHUNC bhalify(suffix) -> "bhal" + suffix

# Map: applies a function to each element of a list
BHUNC map(elements, func)
    BHAR new_elements = []

    BHFOR i = 0 BHO BHLEN(elements) BHEN
        BHAPPEND(new_elements, func(elements/i))
    BHEND

    BHETURN new_elements
BHEND

BHAR words = ["lang", "world", "code"]
BHAR bhalified = map(words, bhalify)
BHRINT(join(bhalified, " | "))    # bhal-lang | bhal-world | bhal-code
```

### User Input

```
BHRINT("What is your name?")
BHAR name = BHINPUT()
BHRINT("Hello, " + name + "!")

BHRINT("Enter a number:")
BHAR n = BHINPUT_INT()
BHRINT("Double that is: " + BHRINT_RET(n * 2))
```

### Running a Script from Another Script

```
# From the REPL or another script:
BHUN("test.txt")
```

---

## Architecture (For Developers)

bhal-lang is implemented as a classic **Lexer → Parser → Interpreter** pipeline, all contained in `basic.py`:

```
Source Text
    │
    ▼
 Lexer          (tokenises the source into a flat list of tokens)
    │
    ▼
 Parser         (builds an Abstract Syntax Tree from the token list)
    │
    ▼
 Interpreter    (tree-walks the AST and evaluates each node)
    │
    ▼
 Result / Error
```

| Component | Class | Responsibility |
|-----------|-------|----------------|
| Lexer | `Lexer` | Converts raw text into `Token` objects |
| Parser | `Parser` | Produces an AST using recursive-descent parsing |
| Values | `Number`, `String`, `List`, `Function`, `BuiltInFunction` | Runtime value types |
| Interpreter | `Interpreter` | Walks the AST via `visit_*` methods |
| Scope | `SymbolTable`, `Context` | Manages variable lookup and function scoping |