
# Create a list of only even numbers from a given numbers range
even_numbers = [ num for num in range(20) if num % 2 == 0]
print(even_numbers) # [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]

# Numbers divisible by both 3 AND 5
special_numbers = [ num for num in range(100) if num % 3 == 0 if num % 5 == 0]
print(special_numbers) # [0, 15, 30, 45, 60, 75, 90]

# List of words of a length more than or equal to B and it contains a in it
words = ['python', 'java', 'ruby', 'javascript']
large_words = [word for word in words if len(word) >=4 and 'a' in word]
print(large_words) # ['java', 'javascript']

# Cartesian product - nested loops flatten left-to-right
colors = ['red', 'blue']
sizes = ['S', 'M', 'L']
combinations = [(color, size) for color in colors for size in sizes]
print(combinations) # [('red', 'S'), ('red', 'M'), ('red', 'L'), ('blue', 'S'), ('blue', 'M'), ('blue', 'L')]
# Think of it as:
# for color in colors:
#     for size in sizes:
#         combinations.append((color, size))

# Flatten the matrix
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
flattened = [num for row in matrix for num in row]
flattened = [matrix[row][col] for row in range(len(matrix)) for col in range(len(matrix))]
print(flattened)

temp_ans = []
for i in range(len(matrix)):
    for j in range(len(matrix)):
        temp_ans.append(matrix[i][j])
print(temp_ans)

# Different from filtering! This KEEPS all items but transforms conditionally
numbers = [1, 2, 3, 4, 5]
# Mark even or odd
labeled = ['even' if num % 2 == 0 else 'odd' for num in numbers]
print(labeled)

# Critical distinction:

# if at the end = filter (fewer items)
# if-else in the expression = transform (same number of items)


