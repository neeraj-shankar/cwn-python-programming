# A fun game -The program should print number from 1 to 100 when a number divisible by 3, answer is fizz
# when the number is divisible by 5 then its called buzz 
# if the number is divisible by both 3 and 5 its called fizzbuzz

def fizz_buzz_game():
    for number in range(1, 101, 1):
        if number % 3 == 0 and number % 5 == 0:
            print(f"FizzBuzz")

        elif number % 5 == 0:
            print(f"Fuzz")

        elif number % 3 == 0:
            print(f"Fizz")
        
        else: print(number)

# Calling the function 
fizz_buzz_game()