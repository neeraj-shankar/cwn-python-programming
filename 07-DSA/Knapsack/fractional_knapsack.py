"""
Given two integer arrays A and B of size N each which represent values and weights associated 
with N items respectively.

Also given an integer C which represents knapsack capacity.

Find out the maximum total value that we can fit in the knapsack. 
If the maximum total value is ans, then return ⌊ans × 100⌋ , i.e., floor of (ans × 100).

NOTE:
You can break an item for maximizing the total value of the knapsack
"""

class FractionalKnapsack:

    def solution_sorting(self, values: list[int], weights: list[int], capacity: int):

        # Create a 2d array of values, weights 
        items = []
        for i in range(len(values)):
            items.append((values[i], weights[i]))
        
        print(items)

        # Sort items using value/weight
        items.sort(key= lambda x:x[0]/x[1], reverse=True)
        print(items)

        ans = 0
        for i in range(0, len(items), 1):

            val = items[i][0]
            wt = items[i][1]

            if capacity <= 0:
                break

            if wt <= capacity:
                ans += val
                capacity -= wt 
            else:
                r = capacity/wt 
                ans += r *val
                break
            
        # rounded_ans = int(round(ans * 100))
        rounded_ans = int(ans * 100 + 1e-9)
        print(f"Oringinal Ans: {ans}")
        return rounded_ans
    

if __name__ == "__main__":

    fk = FractionalKnapsack()

    # Test Case 1:
    A = [60, 100, 120]
    B = [10, 20, 30]
    C = 50
    print(f"Maximum Value Picked: {fk.solution_sorting(A, B, C)}")

    A = [10, 20, 30, 40]
    B = [12, 13, 15, 19]
    C = 10
    print(f"Maximum Value Picked: {fk.solution_sorting(A, B, C)}")

    A = [3]
    B = [20]
    C = 17
    print(f"Maximum Value Picked: {fk.solution_sorting(A, B, C)}")

    A = [2, 7]
    B = [11, 3]
    C = 7
    print(f"Maximum Value Picked: {fk.solution_sorting(A, B, C)}")




