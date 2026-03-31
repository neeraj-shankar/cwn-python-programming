"""
You have a list of transaction logs: 
data = [{"user": "A", "cost": 10}, {"user": "B", "cost": 20}, {"user": "A", "cost": 5}]

Task
-----------------------------------------------------------
1. Sum the total cost per user. 
2. Then, invert that result to show which users spent the same amount.

"""

class SpendingLog():

    @staticmethod
    def solution_bruteforce(log_data: list)-> dict:
        """
        1. Create a new dictionary of results, visit each item in the list
        2. for each user key check if the key exists in results
        3. If yes, sum the value, else insert new records.
        """

        result = {}

        for item in log_data:

            if item['user'] not in result:
                result[item['user']] = item['cost']
            else:
                result[item['user']] += item['cost']

        return result
    
    def solution_cleaner(log_data: list) -> dict:

        result = {}
        for data in log_data:

            result[data['user']] = result.get(data['user'], 0) + data['cost']
        print("Intermediate: ", result)
        # Case 1: When values are guranteed to be different
        # inverted_result = {cost:name for name, cost in result.items()}

        # Case 2: When Values can overlap with after sum
        inverted = {}

        for user, cost in result.items():
            inverted.setdefault(cost, []).append(user)

        return inverted
    
if __name__ == "__main__":

    data = [{"user": "A", "cost": 10}, {"user": "B", "cost": 20}, {"user": "A", "cost": 5}]
    
    ans = SpendingLog.solution_bruteforce(data)
    print("Output: ", ans)

    ans = SpendingLog.solution_cleaner(data)
    print("Output Cleaner: ", ans)

