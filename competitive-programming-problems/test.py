def weighted_characters(inputString):

    # set to holds the weights of the substring
    weights = set()

    # variable to store the current char
    current_character = inputString[0]

    # variable to store current weights
    current_weight = ord(current_character) - ord('a') + 1
    print(f"Weight of the first character: {current_weight}")


    for i in range(1, len(inputString)):
        if current_character == inputString[i]:
            current_weight += ord(inputString[i]) - ord('a') + 1
            print(f"Current character family: {current_character}")
            print(f"Current Weight set: {current_weight}")
        else:
            current_weight = ord(inputString[i]) - ord('a') + 1
            current_character = inputString[i]
        
        # adds the current weight to the sets.
        weights.add(current_weight)
    print(f"Set of character weights: {weights}")


data = "aaabbbccc"
weighted_characters(data)