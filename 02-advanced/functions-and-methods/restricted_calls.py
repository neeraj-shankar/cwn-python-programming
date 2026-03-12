# Understanding 'nonlocal' keyword

# Example 1: WITHOUT nonlocal - This will cause an error
def example_without_nonlocal():
    count = 0
    
    def inner():
        # This will raise UnboundLocalError!
        # count += 1  # Uncommenting this line causes error
        print(f"Count is: {count}")  # Reading works fine
    
    inner()
    return count

# Example 2: WITH nonlocal - This works correctly
def example_with_nonlocal():
    count = 0
    
    def inner():
        nonlocal count  # This tells Python: "count refers to the outer function's variable"
        count += 1      # Now we can modify it
        print(f"Count is: {count}")
    
    inner()
    inner()
    return count

# Example 3: Let's see what happens in our decorator context
def restricted_calls_demo(max_call):
    def decorator(func):
        count = 0  # This is in the 'enclosing scope' of wrapper()
        
        def wrapper(*args, **kwargs):
            nonlocal count  # Without this, count += 1 would fail!
            count += 1
            
            if count > max_call:
                print(f"Blocked: {count}/{max_call}")
                return
            
            print(f"Allowed: {count}/{max_call}")
            return func(*args, **kwargs)
        
        return wrapper
    return decorator

# Example 4: What happens WITHOUT nonlocal in decorator
def broken_decorator(max_call):
    def decorator(func):
        count = 0
        
        def wrapper(*args, **kwargs):
            # count += 1  # This would cause UnboundLocalError
            print("This would break if we tried to modify count")
            return func(*args, **kwargs)
        
        return wrapper
    return decorator

# Example 5: Demonstrating different scopes
x = "global"

def outer():
    x = "enclosing"
    
    def inner():
        nonlocal x
        x = "modified by inner"
        print(f"Inner sees: {x}")
    
    print(f"Before inner(): {x}")
    inner()
    print(f"After inner(): {x}")

# Testing the examples
if __name__ == "__main__":
    print("=== Example 1: Reading without nonlocal (works) ===")
    result1 = example_without_nonlocal()
    print(f"Returned: {result1}\n")
    
    print("=== Example 2: Modifying with nonlocal (works) ===")
    result2 = example_with_nonlocal()
    print(f"Returned: {result2}\n")
    
    print("=== Example 3: Decorator with nonlocal ===")
    @restricted_calls_demo(max_call=2)
    def test_func():
        print("Function executed!")
    
    test_func()  # Call 1
    test_func()  # Call 2  
    test_func()  # Call 3 - blocked
    print()
    
    print("=== Example 5: Scope demonstration ===")
    outer()