"""
You are trying to send signals to aliens using a linear array of A laser lights. 
You don't know much about how the aliens are going to percieve the signals, but what 
you know is that if two consecutive lights are on then the aliens might take it as a sign of 
danger and destroy the earth.

Find and return the total number of ways in which you can send a signal without compromising the safty of the earth. 
Return the ans % 109 + 7.

"""

class WaystoSendSignal:

    def solution_tda(self, A: int)-> int:
        
        memo = [[-1] * (A+1) for _ in range(2)]
        return self.ways(A, 0, 0, memo)

    def ways(self, A: int, prev, i, memo):

        # One valid signal is created
        if i == A:
            return 1
        
        if memo[prev][i] != -1:
            return memo[prev][i]
        
        print(f"Call being made...")
        # Send the OFF signal
        off = self.ways(A, 0, i+1, memo)

        on = 0
        if prev == 0:
            on = self.ways(A, 1, i+1, memo)
        
        memo[prev][i] = on + off
        return memo[prev][i]
        
if __name__ == "__main__":

    wss = WaystoSendSignal()

    # Test Case:
    A = 4
    print(F"Total Number of ways: {wss.solution_tda(A)}")