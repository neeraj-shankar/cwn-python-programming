"""
You operate a shuttle bus running strictly eastward through numbered stops (e.g., Stop 0, Stop 1, Stop 2, etc.). 
Your bus has a maximum number of seats, given by B.

A list of ride requests is provided in A, where each request is of the form:

[numPassengers, pickupStop, dropoffStop]

It indicates:

numPassengers waiting at pickupStop
All these passengers exit at dropoffStop (a higher-numbered stop)
Your goal:
decide if the shuttle can accommodate every request in A without exceeding its seat capacity B at any point.
Return 1 if it's possible, or 0 otherwise.
Problem Constraints

1 <= A.length <= 1000
1 <= B <= 100000
1 <= numPassengers <= 100
0 <= pickupStop < dropoffStop <= 1000
"""

class CityShuttleService:

    def solution_prefix_sum(self, A: list[list[int]], B: int)-> int:
        
        psum = [0] * 10
        for passengers, pickup, dropoff in A:
            psum[pickup] += passengers

            psum[dropoff] -= passengers
        
        print(psum)
        current = 0
        for stop in psum:
            current += stop 
            if current > B:
                return 0

        for i in range(1, len(psum)):
            psum[i] = psum[i-1] + psum[i]
        print(psum)

        return 1

if __name__ == "__main__":

    css = CityShuttleService()
    A = [[2, 1, 5], [3, 3, 7]]
    B = 4

    print(f"Possible ?: {css.solution_prefix_sum(A, B)}")