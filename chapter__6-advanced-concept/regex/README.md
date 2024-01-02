Absolutely, here's a comprehensive documentation covering various concepts used in regular expressions (regex) along with explanations and examples for each concept.

## Regular Expressions (Regex) Documentation

Regular expressions (regex) are powerful tools for pattern matching and manipulation of text data. They provide a concise and flexible way to describe and search for patterns within strings. This documentation will cover the fundamental concepts of regex, along with examples to illustrate each concept.

### Table of Contents

1. **Introduction to Regex**
   - What is a Regular Expression?
   - Regex Syntax
   - Literal Characters

2. **Basic Patterns**
   - Character Classes
   - Anchors
   - Quantifiers
   - Alternation

3. **Special Characters and Escaping**
   - Escaping Metacharacters
   - Dot (.)
   - Word Boundaries (\b)
   - Character Escapes

4. **Grouping and Capturing**
   - Capturing Groups
   - Non-Capturing Groups
   - Backreferences

5. **Modifiers and Flags**
   - Case Insensitivity (re.I)
   - Multiline Matching (re.M)
   - Dot Matches All (re.DOTALL)
   - Verbose Mode (re.VERBOSE)

6. **Lookahead and Lookbehind**
   - Positive Lookahead
   - Negative Lookahead
   - Positive Lookbehind
   - Negative Lookbehind

7. **Commonly Used Regex Patterns**
   - Matching Numbers
   - Matching Email Addresses
   - Matching URLs
   - Extracting Dates

---

### 1. Introduction to Regex

#### What is a Regular Expression?
A regular expression is a sequence of characters that defines a search pattern. It's used for matching strings or portions of strings based on specified patterns.

#### Regex Syntax
Regex patterns consist of ordinary characters (such as letters and digits) and special metacharacters that define the pattern's behavior.

#### Literal Characters
Literal characters match themselves. For example, the regex `a` matches the character 'a'.

### 2. Basic Patterns

#### Character Classes
- `[abc]` matches any of the characters 'a', 'b', or 'c'.
- `[0-9]` matches any digit.
- `[^a-z]` matches any character except lowercase letters.

#### Anchors
- `^` matches the start of a string.
- `$` matches the end of a string.

#### Quantifiers
- `*` matches zero or more occurrences.
- `+` matches one or more occurrences.
- `?` matches zero or one occurrence.
- `{n}` matches exactly n occurrences.
- `{n, m}` matches between n and m occurrences.

#### Alternation
- `|` matches either the expression on its left or the expression on its right.

### 3. Special Characters and Escaping

#### Escaping Metacharacters
Use `\` to escape metacharacters like `^`, `$`, `.`, `*`, `+`, `?`, `(`, `)`, `[`, `]`, `{`, `}`, `|`.

#### Dot (.)
The dot `.` matches any character except a newline.

#### Word Boundaries (\b)
`\b` matches a position between a word character and a non-word character.

#### Character Escapes
- `\d` matches any digit.
- `\w` matches any word character (alphanumeric or underscore).
- `\s` matches any whitespace character.

### 4. Grouping and Capturing

#### Capturing Groups
- `(abc)` captures and remembers the matched text.
- `()` can be nested and referenced using backreferences.

#### Non-Capturing Groups
- `(?:abc)` groups without capturing.

#### Backreferences
- `\1`, `\2`, etc. refer to the text captured by corresponding groups.

### 5. Modifiers and Flags

#### Case Insensitivity (re.I)
Makes the pattern case-insensitive.

#### Multiline Matching (re.M)
Allows `^` and `$` to match the start/end of each line.

#### Dot Matches All (re.DOTALL)
Allows `.` to match newline characters.

#### Verbose Mode (re.VERBOSE)
Ignore whitespace and comments within the pattern for better readability.

### 6. Lookahead and Lookbehind

#### Positive Lookahead
- `x(?=y)` matches 'x' only if followed by 'y'.

#### Negative Lookahead
- `x(?!y)` matches 'x' only if not followed by 'y'.

#### Positive Lookbehind
- `(?<=y)x` matches 'x' only if preceded by 'y'.

#### Negative Lookbehind
- `(?<!y)x` matches 'x' only if not preceded by 'y'.

### 7. Commonly Used Regex Patterns

#### Matching Numbers
- `\d+` matches one or more digits.
- `-?\d+(\.\d+)?` matches integers and floating-point numbers.

#### Matching Email Addresses
- `[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}` matches email addresses.

#### Matching URLs
- `(https?|ftp)://[^\s/$.?#].[^\s]*` matches URLs starting with 'http', 'https', or 'ftp'.

#### Extracting Dates
- `(\d{4})-(\d{2})-(\d{2})` captures year, month, and day in 'YYYY-MM-DD' format.

---

This documentation provides an overview of essential concepts in regular expressions along with examples to illustrate 
each concept. Regular expressions can be a versatile and powerful tool for text processing and pattern matching. 

Practice and experimentation are key to becoming proficient in crafting and using regex patterns effectively.