##############################################################################
## About Function: In Python, a function is treated as a first-class object.
## This means that a function has all the rights as any other variable in the
## language.
## Example1: Assigning a function to a variable
##############################################################################


def greet():
    print(f"Hello Good Morning! Welcome to Python World")


# Assigning greet function to a variable
greet_variable = greet

# We will call the greet() and then greet_variable
# both returns the same output
# As everything is an object in Python, the names we define are simply
# identifiers referencing these objects.
greet()  # Hello Good Morning! Welcome to Python World
greet_variable()  # Hello Good Morning! Welcome to Python World

##############################################################################
## Example2: Passing a function to another function
##############################################################################


def say_it_twice(func):
    func()
    func()


def say_hello():
    print(f"I am being passed into another function.")


# The say_it_twice function accepts a function and calls it twice in its body.
say_it_twice(say_hello)  # I am being passed into another function.
# I am being passed into another function.

##############################################################################
## Example3: Returning a function from a function
## Higher-order function is a function that takes a function as an argument or
## returns a function.
##############################################################################


def change_to_upper_case():
    return str.upper


to_upper = change_to_upper_case()
print(to_upper)

print(to_upper("scaler topics"))


##############################################################################
## Inner Functions: We can define a function inside other functions. Such
## functions are called inner functions or nested functions. Decorators in
## Python also use inner functions.
## The inner functions are locally scoped to the parent. They are not available
## outside of the parent function. If you try calling the first_child outside
## of the parent body, you will get a NameError.
##############################################################################


def parent():
    print(f"I am the parent (outer) function.")

    def first_child():
        print(f"I am the first child function.")

    def second_child():
        print(f"I am second child function.")

    # calling the first_child and second_child from parent block
    first_child()
    second_child()


# Finally calling parent function. This would then call it child function
parent()  # I am the parent (outer) function.
# I am the first child function.
# I am second child function.

##############################################################################
## Understanding Closure Pattern: Inner functions can access variables in the
## outer scope of the enclosing function. This pattern is known as a Closure.
##############################################################################


def outer(message):
    def inner():
        print(f"Message: {message}")

    return inner


# The message is remembered by the inner function even after the outer
# function has finished executing. This technique by which some data gets
# attached to the code is called closure in Python.
say_hello = outer("Hi.. There!! Good Morning.")
print(f"Outer Refence:{say_hello}")
# Outer Refence:<function outer.<locals>.inner at 0x000002587F9C9260>
say_hello()  # Message: Hi.. There!! Good Morning.

say_bye = outer("Hi.. There!! Good Bye.")
print(f"Outer Refence:{say_bye}")
say_bye()  # Message: Hi.. There!! Good Bye.
