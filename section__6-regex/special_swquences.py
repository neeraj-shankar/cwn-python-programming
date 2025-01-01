import re

text = '''Alan Turing was born on 23 June 1912 in London.'''

# Example of \A: This gives a match if the characters to the right of this are
# at the beginning of the string.
res = re.findall('\AAlan', text)
print(f"Result for \A: {res}")

# Example of \b:
res = re.findall(r'\bAlan', text)
print(f"Result for \b: {res}")