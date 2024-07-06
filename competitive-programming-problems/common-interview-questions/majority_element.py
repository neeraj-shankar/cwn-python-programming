"""
Find the majority element in an array (element that appears more than n/2 times).
"""


class MajorityElement:

    def __init__(self, input_data) -> None:

        self.input_data = input_data

    def find_majority_element_dict(self):

        # python to dictionary to store elements and occurence count
        counter = {}
        n = len(self.input_data) / 2

        # traverse through each element of the list
        # Store count of each element in counter dictionary
        # Check whether count of any element crossed n/2
        for ele in self.input_data:
            counter[ele] = counter.get(ele, 0) + 1
            if counter[ele] > n:
                return ele
        return None

    def majority_element_boyer_moore_voting(self):

        candidate = None
        counter = 0

        for num in self.input_data:
            if counter == 0:
                candidate = num
            counter +=1 if candidate == num else -1
        return candidate
            

if __name__ == "__main__":

    raw_data = [1, 2, 3, 2, 1, 2]

    result = MajorityElement(raw_data).find_majority_element_dict()
    print(f"The Element appearing more than n/2: {result}")

    result = MajorityElement(raw_data).majority_element_boyer_moore_voting()
    print(f"The Element appearing more than n/2: {result}")
