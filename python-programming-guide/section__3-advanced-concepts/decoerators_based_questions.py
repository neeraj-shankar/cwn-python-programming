"""
1. **What is a decorator in Python? Can you explain how it works?**
   - Expect to explain the concept of decorators as functions that modify the behavior of other functions or methods. You should be able to describe the process of wrapping a function and the use of `@` syntax.

2. **Can you write a decorator that times the execution of a function?**
   - This question tests your ability to write practical decorators. You might need to use the `time` module to calculate the duration of function execution.

3. **How can you preserve a function's metadata when using decorators?**
   - Discuss the use of `functools.wraps` and why it's important to preserve a function's `__name__`, `__doc__`, and other attributes.

4. **What is the difference between `@staticmethod`, `@classmethod`, and instance methods?**
   - You should be able to explain the differences and when to use each one.

5. **Can you create a decorator that caches the result of a function call?**
   - This question assesses your understanding of more complex decorator patterns, such as memoization or caching.

6. **How would you implement a decorator that can be used both with and without arguments?**
   - This tests your knowledge of writing decorators that can handle optional arguments, which requires an extra layer of function nesting.

7. **Explain the decorator pattern and its advantages and disadvantages.**
   - Discuss the design pattern, not just the Python feature, and when it might be useful or problematic in software design.

8. **Can you stack multiple decorators on a single function? What is the order of execution?**
   - You should know how to apply multiple decorators to a function and understand how the order affects the result.

9. **How do decorators interact with function arguments?**
   - Explain how to write decorators that can handle functions with any combination of arguments using `*args` and `**kwargs`.

10. **Are there any performance considerations when using decorators?**
    - Discuss any potential performance impacts of decorators, such as added overhead or issues with recursive decorators.

11. **Can you explain how a class-based decorator works compared to a function-based decorator?**
    - You might need to describe how to implement a decorator using a class with `__call__` method and when it might be preferable over a function-based decorator.

12. **How can you debug a function wrapped with a decorator?**
    - Discuss strategies for debugging, such as temporarily disabling the decorator or using tools that understand decorators.

13. **Can you use decorators to enforce function argument types or return types?**
    - This question assesses your knowledge of using decorators for type checking, which can be particularly relevant with the introduction of type hints in Python.

14. **How would you implement a decorator that logs every call to the decorated function?**
    - This tests your ability to write decorators for cross-cutting concerns like logging.

15. **Can you describe a real-world scenario where you successfully used a decorator in your code?**
    - Be prepared to discuss actual use cases from your experience, which might include decorators for authentication, authorization, transaction handling, or other aspects.


"""
from utils import calculate_execution_time, cache_decorator, my_decorator    
import re    
import time

# calling palindrome checker



class PracticeQuestionWithDecorators:

    def __init__(self) -> None:
        pass

    @my_decorator
    def check_palindrome(self, string_list):
        """
        A palindrome is a word, phrase, number, or other sequences of characters that reads the same forward and backward (ignoring spaces,
        punctuation, and capitalization). In other words, if you reverse the sequence, it remains unchanged.

        Takes list of strings and returns a list of Boolean (True for Palindrome and False for Non-Palindrome)

        """
        
        is_palindrome_list = []
        for word in string_list:
            # Remove non-alphanumeric characters and convert to lower case
            cleaned_word_phrase= re.sub(r'[^A-Za-z0-9]', '', word).lower()         
            if cleaned_word_phrase == cleaned_word_phrase[::-1]:
                is_palindrome_list.append("YES")
            else:
                is_palindrome_list.append("NO")
        time.sleep(1)
        return is_palindrome_list
    
    

if __name__ == "__main__":

    # Raw data for testing
    original_string_list = [
        "radar",
        "level",
        "civic",
        "name",
        "madam",
        "last",
        "rotor",
        "A man, a plan, a canal, Panama",
        "Was it a car or a cat I saw?",
    ]


    instance1 = PracticeQuestionWithDecorators()

    result = instance1.check_palindrome(original_string_list)
    print(f"Palindrome Check: {result}")
    print(instance1.check_palindrome.__name__)
    # print(instance1.check_palindrome.__doc__)

    # @calculate_execution_time
    # @cache_decorator
    # @calculate_execution_time
    # def compute_fibonacci(n):
    #     """Compute the nth Fibonacci number."""
    #     if n in (0, 1):
    #         return n
    #     return compute_fibonacci(n - 1) + compute_fibonacci(n - 2)
    
    # print(compute_fibonacci(10))
    # print(compute_fibonacci(10))




