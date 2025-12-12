class ReverseString:

    def __init__(self, input_str):
        self.str = input_str

    def solutionTwoPointer(self):

        i = 0
        j = len(self.str) - 1
        # convert the string into a list due to immutability of string
        temp = list(self.str)
        while (i<j):
            temp[i], temp[j] = temp[j], temp[i]

            # increase i and decrease j
            i += 1
            j -= 1

        
        return "".join(temp)
    
if __name__ == "__main__":
    
    input_str = "madam"

    # Create instance of the class ReverseString
    rs = ReverseString(input_str)
    print(f"Reversed String: {rs.solutionTwoPointer()}")
        