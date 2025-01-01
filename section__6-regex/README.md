# Python Regular Expressions (RegEx) Guide

This README provides a detailed explanation of Python's Regular Expressions (RegEx) functions and meta characters. Regular expressions are a powerful tool for matching patterns within strings.

## RegEx Functions

### 1. `findall(pattern, string)`
Matches all occurrences of the pattern present in the string and returns them as a list.

### 2. `search(pattern, string)`
Searches the string for a match to the pattern, returning a match object for the first occurrence.

### 3. `split(pattern, string)`
Splits the string at each occurrence of the pattern and returns a list of substrings.

### 4. `sub(pattern, rep_substring, string)`
Replaces one or more matches of the pattern in the string with the given replacement substring.

## Meta Characters

Meta characters are special characters in a RegEx that have a unique meaning and are used to define the search pattern.

### `[ ]` (Square brackets)
Matches any single character contained within the brackets.

### `.` (Period)
Matches any character except a newline character.

### `^` (Caret)
Matches the start of the string with the given pattern.

### `$` (Dollar)
Matches the end of the string with the given pattern.

### `*` (Asterisk)
Matches zero or more occurrences of the pattern to its left.

### `+` (Plus)
Matches one or more occurrences of the pattern to its right.

### `?` (Question Mark)
Matches zero or one occurrence of the pattern to its left.

### `{ }` (Braces)
Matches a specified number of occurrences of the pattern inside the braces.

### `|` (Pipe)
Acts as a logical OR. Matches the pattern either on the left or the right side of the pipe.

### `( )` (Group)
Groups multiple patterns into a single unit for matching.

### `\` (Backslash)
Used to escape special characters or to signal a special sequence.

---

Regular expressions are a key concept in Python for string manipulation and pattern matching. Use this guide as a reference when working with Python RegEx in your projects. Remember to import the `re` module before using these functions in your code.