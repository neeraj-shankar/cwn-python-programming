word = "abcdef"

def test():
    for char in word:
        if char == "d":
            return True
        else:
            print(f"Current Char: {char}")

# function call
test()
