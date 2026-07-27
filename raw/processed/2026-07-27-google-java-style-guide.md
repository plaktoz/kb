# Google Java Style Guide

source_url: https://google.github.io/styleguide/javaguide.html

---

This document serves as the complete definition of Google's coding standards for source code in the Java™ Programming Language.

## 1. Introduction

### Terminology Notes
- `@interface` refers to an annotation type declaration.
- "class" means an ordinary class, enum, annotation type, or interface.

## 2. Source File Basics

- **File name**: The file name consists of the case-sensitive name of the top-level class plus the `.java` extension.
- **Encoding**: UTF-8.
- **Special characters**: Only ASCII horizontal space (0x20) is permitted; use special escape sequences (`\b`, `\t`, `\n`, `\f`, `\r`, `\"`, `\'`, `\\`) over octal or Unicode escapes.

## 3. Source File Structure

Order: License/copyright → Package declaration → Import statements (static then non-static) → Exactly one top-level class.

### 3.3 Imports
- No wildcard imports.
- No module imports.
- Imports are ordered: static imports, blank line, non-static imports; within each group in ASCII sort order.

### 3.4 Class Declaration
- Exactly one top-level class per file.
- Class contents should follow a logical order; overloaded methods appear in a single contiguous group.

## 4. Formatting

- **Braces**: Always used for `if`, `else`, `for`, `do`, `while`, even for single-statement bodies. K&R (Kernighan and Ritchie) style for nonempty blocks.
- **Indentation**: +2 spaces per block level.
- **One statement per line**.
- **Column limit**: 100 characters.
- **Line-wrapping**: Break at higher syntactic levels; continuation lines indented at least +4.
- **Horizontal whitespace**: Single space after reserved keywords; spaces around operators.
- **Horizontal alignment**: Never required.
- **Grouping parentheses**: Recommended when omitting them would cause ambiguity.

### 4.8 Specific Constructs
- **Variables**: One variable per declaration; declare close to point of first use.
- **Arrays**: Square brackets part of type (`String[] args`, not `String args[]`).
- **Switch**: All switches must be exhaustive; include `default` label even when not logically required. New-style (arrow) switches must be used for expressions.
- **Numeric literals**: `long` literals use uppercase `L` suffix (e.g., `3000000000L`).
- **Text blocks**: Opening `"""` always on a new line.

## 5. Naming

- **Identifiers**: ASCII letters and digits only; no special prefixes/suffixes like `name_`, `mName`, `s_name`, `kName`.
- **Package/module names**: Lowercase letters and digits only; concatenated words (e.g., `com.example.deepspace`).
- **Class names**: UpperCamelCase; typically nouns. Test classes end in `Test`.
- **Method names**: lowerCamelCase; typically verbs.
- **Constant names**: `UPPER_SNAKE_CASE`; static final fields with deeply immutable contents.
- **Non-constant fields**: lowerCamelCase.
- **Parameters/locals**: lowerCamelCase; avoid single-char parameter names in public methods.
- **Type variables**: Single capital letter (`E`, `T`, `X`) or class name + `T` (e.g., `RequestT`).
- **Unnamed variables**: `_` syntax allowed.

### 5.3 Camel Case Rules
Convert acronyms/special words by treating them as single words: `XmlHttpRequest` (not `XMLHTTPRequest`), `newCustomerId` (not `newCustomerID`), `supportsIpv6OnIos` (not `supportsIPv6OnIOS`).

## 6. Programming Practices

- **`@Override`**: Always used when legal; omit only when parent method is `@Deprecated`.
- **Caught exceptions**: Do nothing only with a comment explaining why.
- **Static members**: Referenced through the class name, not an instance.
- **Finalizers**: Do not override `Object.finalize`.

## 7. Javadoc

- **Format**: `/** ... */`; summary fragment as first sentence (noun or verb phrase, not a complete imperative sentence).
- **Block tags**: `@param`, `@return`, `@throws`, `@deprecated`; in that order; never with empty descriptions.
- **Where required**: Every public class, member, or record component; optional for "obvious" members.
- **Overrides**: Not always required on overriding methods.
