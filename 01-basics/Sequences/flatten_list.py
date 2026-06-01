

class FlatternList:

    def __init__(self):
        pass

    @staticmethod
    def solution_recursion(nested_list):
        """
        1. Iterate through each item
        2. If item is a list, recursively flatten it
        3. If item is not a list, add it to result

        Time Complexity: O(n) where n = total elements
        Space Complexity: O(d) where d = maximum depth (call stack)
        """

        ans = []

        for item in nested_list:

            if isinstance(item, list):
                # Recursively flatten the nested list
                ans.extend(FlatternList.solution_recursion(item))
            else:
                ans.append(item)

        return ans
    @staticmethod
    
    def solution_iterative(nested_list):

        ans = []

        while nested_list:
            item = nested_list.pop()

            if isinstance(item, list):
                nested_list.extend(item)
            else:
                ans.append(item)
        return ans

if __name__ == "__main__":
    nested_list = [1, [2, 3], [4, [5, 6]], 7]
    print(FlatternList.solution_recursion(nested_list))
    print(FlatternList.solution_iterative(nested_list))
