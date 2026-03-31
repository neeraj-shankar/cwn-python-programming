# In built methods and functions in Python

## The **lambda** function
In Python, a Lambda function is a small, *anonymous* function that is defined *without a name*. While normal functions are defined using the def keyword, lambda functions *use the lambda keyword*.

### Syntax: lambda {arguments}:{expression}
- **lambda**: The keyword that starts the function.
- **arguments**: The inputs (comma-separated, just like normal functions).
- **expression**: A single piece of code that is executed and automatically returned.

- *Note*: Lambda functions can have any number of arguments but only one expression.

```Python
square_lambda = lambda x: x * x

print(square_lambda(5)) # Output: 25
```
### FAQs on Lambda

#### 1. Which built-in function is often used with lambda to extract elements from an iterable based on a condition?
- **filter()**: Filter takes a function (often a lambda) that returns True or False to keep specific items.

#### 3. What happens if you try to include a 'return' statement inside a lambda expression?
- The 'return' statement is not allowed in lambda syntax because the expression is returned automatically.

#### 4. Consider the following code: nums = [1, 2, 3]. Which code snippet doubles each number using a lambda?
- **map(lambda x: x * 2, nums)**: 

#### 5. True or False: Lambda functions can access variables from their containing scope.
- Lambda functions are closures and can access variables defined in the scope where they were created.

#### 6. What will be the output of the following code snippet? `print((lambda x: (lambda y: x + y))(5)(10))`
- **15**: The first call binds 5 to x, returning a function that takes y, and the second call binds 10 to y, resulting in 5 + 10.

#### 7. In the following list of lambdas, what is the output of `funcs[0]()`? `funcs = [lambda: i for i in range(3)]`
- **2**: All functions in the list reference the same variable 'i', which ends at its final value in the loop after the list is created.

#### 8. How can you fix the 'late binding' issue in a list of lambdas to ensure each lambda remembers its specific loop value?
- **By using a default argument: `lambda i=i: i`**: Default arguments are evaluated at definition time, effectively 'freezing' the current value of the variable for that specific function instance.

#### 9. What is an 'IIFE' in the context of Python lambdas?
- **An Immediately Invoked Function Expression**: This refers to defining a lambda and calling it immediately in the same line, e.g., `(lambda x: x+1)(5)`.

#### 10. What is the primary limitation of using a lambda compared to a function defined with def?
- **Lambdas cannot have docstrings**: Because they are expressions without a header, there is no place to put a triple-quoted docstring string.