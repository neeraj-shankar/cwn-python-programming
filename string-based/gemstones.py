"""
There is a collection of rocks where each rock has various minerals embeded in it. 
Each type of mineral is designated by a lowercase letter in the range ascii[a-z]. 

There may be multiple occurrences of a mineral in a rock. A mineral is called a gemstone if it occurs 
at least once in each of the rocks in the collection.

Given a list of minerals embedded in each of the rocks, display the number of types of gemstones in the collection.
"""

class Gemstones:

    def __init__(self, collection):
        self.collection = collection
    
    def gems_count_using_set(self):
        
        # Convert each string to a set of unique characters
        sets_collection = [set(mineral) for mineral in self.collection]
        print(sets_collection)

        # Find the intersection of all sets
        gemstones_set = set.intersection(*sets_collection)
        print(gemstones_set)

        return len(gemstones_set)


        
    def gems_count_using_naive_approach(arr):
        # Write your code here
        total_gems = 0
        for _chr in arr[0]:
            result = all(_chr in item for item in arr)
            if result:
                total_gems += 1
        return total_gems


if __name__ == '__main__':
    rocks_collection = ["abc", "abc", "bc"]

    Gemstones(rocks_collection).gems_count_using_set()