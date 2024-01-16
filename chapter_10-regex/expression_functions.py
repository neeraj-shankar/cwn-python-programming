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
