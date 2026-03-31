class ReverseTheWord:
    """
    A class to reverse the words in a given string, handling multiple spaces and punctuation.

    Attributes:
    ----------
    input_str : str
        The input string that needs to be processed and reversed by word order.

    Methods:
    --------
    solutionTwoPointer():
        Reverses the order of words in the input string using a two-pointer technique.
        Handles multiple spaces and punctuation.
    """

    def __init__(self, input_str):
        """
        Initializes the ReverseTheWord object with the input string.
        
        Parameters:
        -----------
        input_str : str
            The input string to be processed and reversed by word order.
        """
        self.str = input_str

    def solutionTwoPointer(self):
        """
        Reverses the order of words in the input string using the two-pointer technique.
        Handles multiple spaces and punctuation.

        Steps:
        ------
        1. Clean the string to remove punctuation using regular expressions.
        2. Split the string into words while handling multiple spaces.
        3. Reverse the words using the two-pointer technique.
        4. Join the reversed words back into a string and return the result.
        
        Returns:
        --------
        str
            The input string with the order of words reversed, while maintaining punctuation and handling multiple spaces.
        """
        

        # convert the string into a list due to immutability of string
        temp = self.str.split()

        # initialize i and j 
        i =  0
        j = len(temp) - 1
        print(f"Word List: {temp}")
        while (i<j):
            temp[i], temp[j] = temp[j], temp[i]

            # increase i and decrease j
            i += 1
            j -= 1

        
        return " ".join(temp)
    
if __name__ == "__main__":
    
    input_str = "hello, world! how are you?"

    # Create instance of the class ReverseString
    rts = ReverseTheWord(input_str)
    print(f"Reversed String: {rts.solutionTwoPointer()}")
        