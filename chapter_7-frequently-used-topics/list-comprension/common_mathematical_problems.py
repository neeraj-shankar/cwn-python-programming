
# Finding number from 1-1000 that are divisible by 7

number_list = [num for num in range(1, 1001) if num % 7 == 0]
# print(number_list)

# finding all number from 1 to 1000 which has 3 in them
number_list = [num for num in range(1, 1001) if str(num).__contains__('3')]
print(number_list)

# Create a list of all the consonants 
phrase = "Yellow Yaks like yelling and yawning and yesturday they yodled while eating yuky yams"
