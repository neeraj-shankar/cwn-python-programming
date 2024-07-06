What are Python Generators?
-----------------------------------------------------------------------------------------------------------------------
Python's generator functions are used to create iterators(which can be traversed like list, tuple)  and return a traversal object. 

Generator functions are defined as the normal function, but to identify the difference between the normal function
and generator function is that in the normal function, we use the return keyword to return the values, and in the 
generator function, instead of using the return, we use yield to execute our iterator.


Yield vs return
-----------------------------------------------------------------------------------------------------------------------

Yield
-----------------------------------------------------------------------------------------
1. It is responsible for controlling the flow of the generator function.
2. After returning the value from yield, it pauses the execution by saving the states.

Return 
-----------------------------------------------------------------------------------------
1. It is used in normal functions.
2. Return statement returns the value and terminates the function.


Difference Between Generator Function & Normal Function
-----------------------------------------------------------------------------------------------------------------------
1. In generator functions, there are one or more yield functions, whereas, in Normal functions, there is only one function

2. When the generator function is called, the normal function pauses its execution, and the call is transferred 
     to the generator function.

3. Local variables and their states are remembered between successive calls.

4. When the generator function is terminated, StopIteration is called automatically on further calls.

Use of Generators in Python
-----------------------------------------------------------------------------------------------------------------------

1. Easy to Implement:
-----------------------------------------------------------------------------------------
Generator functions are easy to implement as compared with iterators. In iterators, we have to implement iter(), __next__() 
function to make our iterator work.

2. Memory Efficient:
-----------------------------------------------------------------------------------------
Generator Functions are memory efficient, as they save a lot of memory while using generators. A normal function
will return a sequence of items, but before giving the result, it creates a sequence in memory and then gives us the result, 
whereas the generator function produces one output at a time.

3. Infinite Sequence:
-----------------------------------------------------------------------------------------
We all are familiar that we can't store infinite sequences in a given memory. This is where generators come into the picture. 
As generators can only produce one item at a time, so they can present an infinite stream of data/sequence


Summary 
-----------------------------------------------------------------------------------------------------------------------
1. Generator functions in Python are used to create iterators and return an iterator object.
2. In the generator function, we use a yield statement instead of a return statement.
3. We can use multiple yield statements in the generator function.
4. When iterating over the generator function using next, in the end, it will show up StopIteration error, whereas when we use the for loop, it doesn't show any error.