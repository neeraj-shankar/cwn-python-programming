##############################################################################
## for-else controll statement: The else clause in a loop is executed when the
## loop condition becomes false
## This can help use handle cases when we want check if all elements matches
## a certain condition before we take action on them
##############################################################################

# check if all numbers in a list are positive
numbers = [2, 5, -3, 10]

for num in numbers:
    if num <= 0:
        print(f"All numbers in the are not positive")
        break
else:
    print(f"All numbers are positive")
