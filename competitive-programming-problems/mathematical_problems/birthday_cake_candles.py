"""
You are in charge of the cake for a child's birthday. You have decided the cake will have one candle for each year of
their total age. They will only be able to blow out the tallest of the candles. Count how many candles are tallest.

candles = [4, 4, 1, 3]

The maximum height candles are 4 units high. There are 2 of them, so return 2.

Returns
-----------------------------------------------------------
int: the number of candles that are tallest

Input Format
-----------------------------------------------------------
The first line contains a single integer, n, the size of candles[].
The second line contains n space-separated integers, where each integer i describes the height of candles[i].

"""


class BirthdayCakeCandles(object):
    @staticmethod
    def naive_approach(candles):
        print(f"Candles: {candles}")
        sorted_candle_list = sorted(candles, reverse=True)
        print(f"The sorted candle list --> {sorted_candle_list}")
        longest_height = sorted_candle_list[0]
        longest_candle_count = 0
        for candle in sorted_candle_list:
            if candle == longest_height:
                longest_candle_count += 1

        print(f"The count of longest candles --> {longest_candle_count}")
        return longest_candle_count


"""
"""
fptr = open("output_file.txt", "w")

candles_count = int(input().strip())

candle_list = list(map(int, input().rstrip().split()))

result = BirthdayCakeCandles.naive_approach(candle_list)

fptr.write(str(result) + "\n")

fptr.close()
