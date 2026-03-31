# Sorting on integers list
numbers = [34, 12, 78, 23, 90, 45, 67]

sorted_top_3 = sorted(numbers, reverse=True)[0:3]
print(sorted_top_3) # [90, 78, 67]


# String Sorting
words = ['banana', 'apple', 'cherry', 'date', 'elderberry']

# sorts alphabetically
sorted_words = sorted(words, reverse=False)
print(sorted_words) # ['apple', 'banana', 'cherry', 'date', 'elderberry']

# Sort by word len 
sorted_by_len = sorted(words, key=len)
print(sorted_by_len)

# Mixed case of strings
