"""
Generator Basics:
--------------------------------------------------------------------------
1. Can you explain what a generator is in Python and how it differs from a regular function?
2. How do you create a generator, and what is the yield keyword used for?
3. What are the benefits of using a generator instead of a list when dealing with large datasets?

Generator Control Flow:
--------------------------------------------------------------------------
4. How does the execution of a generator function differ from a normal function after a yield statement is encountered?
5. What happens when a generator's next() method is called for the first time, and what happens when it's called after the generator has yielded a value?

Generator Methods and State:
--------------------------------------------------------------------------
6. Besides next(), what other methods can be called on a generator, and what are their purposes?
7. Can you describe how a generator maintains its state between calls?
8. How would you handle resetting a generator, and what are the implications of doing so?

Advanced Generator Usage:
--------------------------------------------------------------------------
9. How can you chain multiple generators together, and why might you want to do this?
10. Can you provide an example of using a generator expression? How does it differ from a list comprehension?
11. What is a coroutine, and how does it relate to generators in Python?

Generators and Performance:
--------------------------------------------------------------------------
11. In what scenarios might a generator provide performance benefits over a list or other iterable?
12. Can you discuss any potential downsides or limitations of using generators?

Generators and Memory Management:
--------------------------------------------------------------------------
13. How do generators help with memory management in Python?
14. What is lazy evaluation, and how do generators enable this in Python?

Generator Internals:
--------------------------------------------------------------------------
15. What is the StopIteration exception, and how is it related to generators?
16. How does Python's iterator protocol work under the hood, and how do generators comply with it?

Practical Applications:
--------------------------------------------------------------------------
17. Can you give an example of a practical problem that can be efficiently solved using generators?
18. How would you use a generator to implement a function that reads a large file line by line without loading the entire file into memory?

Generators and Asynchronous Programming:
--------------------------------------------------------------------------
19. How do generators play a role in asynchronous programming in Python?
20. Can you explain the difference between a generator and an asynchronous generator (async def with yield)?


"""

class GeneratorFunctionPractice:

    def __init__(self) -> None:
        pass

    @staticmethod
    def simple_generator():
        yield "first"
        yield "seconds"
        yield "Third"



if __name__ == "__main__":

    # Create Practive set class object instance

    obj = GeneratorFunctionPractice()

    # Create an generator function object
    gen = obj.simple_generator()

    # calling the next() for the first time
    print(gen.__next__()) # first
    print(gen.__next__()) # seconds

    # Calling next() for third time
    print(gen.__next__())


    # Calling generator for the fourth time
    try:
        print(gen.__next__())

    except StopIteration as ex:
        print("The generator is exhausted (no more values to yield).")

