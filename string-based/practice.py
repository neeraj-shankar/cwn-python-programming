def minimize_cost(input_str, cost):
    # Amanda can choose any strategy here based on her goal
    # For simplicity, let's just append a character.
    new_str = input_str + 'c'
    return new_str

input_str = "abab"
cost = 1
result = minimize_cost(input_str, cost)
print("New string:", result)


input_string = "abab"
cost = 1
print(minimize_cost(input_string, cost))