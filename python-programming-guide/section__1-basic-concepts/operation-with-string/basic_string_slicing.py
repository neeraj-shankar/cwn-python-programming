"""
Python slicing is about obtaining a sub-string from the given string by slicing it respectively from start to end. 
"""

# General Format --> arr[start:stop:step]
my_string = "python programming"

#slice from the begining of the string
s1 = my_string[:4]
print(f"First 4 letters from start--> {s1}")

# slice string from begining to end using step size
s2 = my_string[0:6:1]
print(f"First 5 letters from start of the string--> {s2}")

# Using negative index to slice a string
s3 = my_string[-1:-7:-1]
print(f"Using the negative index to slice string--> {s3}")

# reverse a string using string slicing
s4 = my_string[::-1]
print(f"The reversed version of the string--> {s4}")

# experimental --> Using negative index with positive step size
s5 = my_string[-7:-1:1]
print(f"Slicing from negative index and positive step size--> {s5}")

# experimental --> slice string from start and back with step size as one
s6 = my_string[1:-1]
print(f"Experimental --> {s6}")

#experiment
one_letter = "a"
s7 = one_letter[1:-1]
print(f"Slicing single letter--> {s7}")