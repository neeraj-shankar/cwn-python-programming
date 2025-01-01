import re

##############################################################################
## search(pattern, string): this function can search patterns irrespective of
## the position at which the pattern is present.  This function matches the
## first occurrence of the pattern.
##############################################################################

text = """
Organizing is a practice of leadership whereby we define leadership as enabling others to achieve shared purpose under conditions of uncertainty.
"""
pattern = "leader"
res = re.search(pattern, text)
print(f"Result of Search: {res}")

pattern = "define"
res = re.search(pattern, text)
print(f"Result of Search: {res}")

##############################################################################
## split(pattern, string): This function splits a string on the given pattern.
## This returns the result as a list after splittin
##############################################################################
pattern = r"\s+"  # Matches one or more white spaces
res = re.split(pattern, text)
print(f"Result of Split: {res}")
# Result of Split: ['', 'Organizing', 'is', 'a', 'practice', 'of', 'leadership', 'whereby', 'we', 'define', 'leadership', 'as', 'enabling', 'others', 'to', 'achieve', 'shared', 'purpose', 'under', 'conditions', 'of', 'uncertainty.', '']


##############################################################################
## sub(pattern, repl, string): This function replaces a pattern with the given
## substring in a given string.
##############################################################################
pattern = "under"
replace_word = "out of"
res = re.sub(pattern, replace_word, text)
print(f"Result of sub: {res}")
# Organizing is a practice of leadership whereby we define leadership as enabling others to achieve shared purpose out of conditions of uncertainty.


##############################################################################
## Match Object:
## Whenever we call any regex method/function it searches the pattern in the 
## string. If it finds a match then it returns a match object else return None.

## match.group(): This returns the part of the string where the match was there

## match.start(): This returns the start position of the matching pattern in 
## the string.

## match.end(): This returns the end position of the matching pattern in the string.

## match.span(): This returns a tuple which has start and end positions of 
## matching pattern.

## match.re: This returns the pattern object used for matching.

## match.string: This returns the string given for matching.

## Using r prefix before regex: This is used to convert the pattern to raw string.This
## means any special character will be treated as normal character. 
##############################################################################

import re
text = '''Using r prefix before regex: This is used to convert the pattern to raw string. This means any special character will be treated as normal character'''
# Searches the pattern in the string.
res = re.search('convert',text)
print("Raw Match Object Output: {}".format(res))
print("--"*50)
print("Match group() method output: ",res.group())
print("--"*50)
print("Start position of the matching pattern: ",res.start()) 
print("--"*50)
print("End position of the matching pattern: ",res.end())
print("--"*50)
print("Tuple of start and end position of the matching pattern: ",res.span()) 
print("--"*50)
print("Pattern Used for matching: ",res.re)
print("--"*50)
print("The original text in string: ",res.string)
print("--"*50)


