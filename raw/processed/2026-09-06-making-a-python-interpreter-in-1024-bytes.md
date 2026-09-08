---
source_url: https://austinhenley.com/blog/python1024.html
author: Austin Z. Henley
date: 2026-09-06
---

# Making a Python Interpreter in 1024 Bytes

Henley describes a weekend coding challenge: build a Python interpreter in C, limited to 1024 bytes, with no macros or external library tricks.

The target program was a FizzBuzz implementation using recognizable Python syntax — `def`, colons, indentation, and `if` without parentheses. He notes he "probably can't fit *all* of the Python language" into 1024 bytes, so the goal was a convincing subset.

## Architecture

Rather than tokenizing into an AST and emitting bytecode like CPython, this interpreter uses a handful of globals and parses source directly. State includes a raw source array, a symbol table (`vars[256]`), and position trackers. Expressions use standard recursive descent, executed immediately during parsing. There is **no error handling**.

Variable names are restricted to single lowercase letters, enabling direct symbol table lookups via ASCII value comparisons.

## Control Flow

Blocks execute until indentation decreases. Loops work by jumping backward and **reparsing source** each iteration. Functions store their source position in the symbol table; calls save and restore the caller's position.

## Code Golf Techniques

Henley used several C89 tricks to compress the readable ~4800-byte version down to exactly 1024 bytes:

- Single-letter names, implicit `int` types, global zero-initialization
- ASCII values instead of character literals
- Ternary and comma operators
- Bitwise ops replacing logical ops

For example, a skip-to-end-of-line function was reduced to: `Y(){c&&c-10&&Y(G());}` — using `&&` short-circuit evaluation instead of nested `if` blocks.

## Supported Features

The final interpreter handles integer variables/literals, arithmetic (`+ - * %`) with precedence, comparisons, `if`/`else`, `while`/`for` loops, no-argument function definitions, recursive calls, indent-based blocks, `print`, and comments.

Henley concluded that the process was "quite tedious" and both versions are available on GitHub.
