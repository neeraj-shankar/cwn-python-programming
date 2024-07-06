"""
You are choreographing a circus show with various animals. For one act, you are given two kangaroos on a number line ready
to jump in the positive direction (i.e, toward positive infinity).

The first kangaroo starts at location x1 and moves at a rate of v1 meters per jump.
The second kangaroo starts at location x2 and moves at a rate of v2 meters per jump.

You have to figure out a way to get both kangaroos at the same location at the same time as part of the show. If it is possible, 
return YES, otherwise return NO.

Example
-----------------------------------------------------------
x1 = 2, v1 = 1
x2 = 1, v2 = 2

The formula to check if the kangaroos will meet is:
-----------------------------------------------------------
position1 + (rate1 * x) == position2 + (rate2 * x)

Where:

position1 and position2 are the initial positions of the first and second kangaroos.
rate1 and rate2 are the rates of movement of the first and second kangaroos.
x is the number of jumps.

"""
def kangaroo_meet(position1, rate1, position2, rate2):
    # If the rates are the same, the kangaroos will never meet.
    if rate1 == rate2:
        return "NO"

    x = (position2 - position1) / (rate1 - rate2)
    
    if x.is_integer() and x >= 0:
        return "YES"
    else:
        return "NO"

# Example usage:
position1 = 0
rate1 = 3
position2 = 4
rate2 = 2

result = kangaroo_meet(position1, rate1, position2, rate2)
print(result)  # Output: YES