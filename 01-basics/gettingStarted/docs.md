# Python -- Getting Started

## **Namespace**
Think of a **Namespace** as a giant dictionary where every name (variable, function, class) you create is a **Key**, and the object it points to is the **Value**.

Its main job is to make sure that names stay unique so there are no conflicts. 

For example, you might have a friend named "Alice" in your family and a different "Alice" at your workplace. You don't get them confused because they belong to different **spaces**.

---

### 🏛️ The 4 Levels of Namespace (The LEGB Rule)

Python looks for names in a specific order, moving from the "smallest" room to the "biggest" building.

1. **Local (L):** Names defined inside a function. These only exist while the function is running.
2. **Enclosing (E):** Names in the local scope of "outer" functions (relevant when you have a function inside a function).
3. **Global (G):** Names defined at the top level of your script or module.
4. **Built-in (B):** Reserved names that come pre-loaded in Python (like `print()`, `len()`, or `range()`).

---

### 💡 A Simple Analogy: The "Box" System

Imagine you are at a large hotel:

* **The Global Namespace** is the hotel lobby. Everyone in the hotel can see the "Lobby Clock."
* **The Local Namespace** is your specific hotel room. If you bring your own "Travel Clock," that's the one you'll look at.
* **The Conflict:** If you ask someone in your room, "What time is it?", they look at the **Travel Clock** (Local). They don't even check the **Lobby Clock** (Global) unless your room doesn't have one.

---

### 💻 See it in Code

Here is how Python handles these different "layers":

```python
# Global Namespace
name = "Global Alice"

def outer_function():
    # Enclosing Namespace
    name = "Enclosing Alice"
    
    def inner_function():
        # Local Namespace
        name = "Local Alice"
        print(name) # This will print 'Local Alice'
        
    inner_function()

outer_function()

```

If you comment out `name = "Local Alice"`, Python will look one level up and print `"Enclosing Alice"`. If you delete that too, it goes to the **Global** level.

### 🛠️ Why do we need this?

Without namespaces, programming would be a nightmare. Imagine if every time you imported a library, you had to check if the library creator used the same variable names as you! Namespaces create "safety bubbles" so your code doesn't accidentally overwrite someone else's.

Would you like to see how the `global` and `nonlocal` keywords can be used to "break" these boundaries?

### FAQs --> Namespaces
#### 1.Which namespace is created when the Python interpreter starts and is never deleted until the interpreter quits?
- **Built in Namespace:** The built-in namespace contains names like 'print' and 'int' and exists for the entire duration of the script execution.

#### 2. What keyword allows you to modify a variable in the global namespace from within a local function scope?
- The **'global'** keyword explicitly tells Python that a specific name belongs to the global namespace.

#### 3. If Python cannot find a name in the Local, Enclosing, or Global namespaces, where does it look last?
- The Built-in namespace is the final level of the LEGB rule before a NameError is raised.

#### 4. What happens if you try to use a name that does not exist in any of the four namespaces?
- When a name cannot be found after checking all four scopes, Python raises a NameError exception.

#### 5. Which of the following creates a new Local namespace?
- A new local namespace is created every time a function is executed.

#### 6. When is the Global namespace for a module created?
- The global namespace exists for the duration of the module's life in the program.

#### 7. Which keyword is used in a nested function to indicate that a variable belongs to the outer (but not global) function scope?
- The 'nonlocal' keyword is used to work with variables inside nested functions that aren't global.

#### 8. What happens when you try to assign a value to a variable inside a function that has the same name as a global variable, without using the 'global' keyword?
- This is known as shadowing; the local variable exists only within the function scope while the global one remains unchanged.

#### 9. If you use *'from math import sqrt'*, where is 'sqrt' added in your script's namespace structure?
- Direct imports place the imported name into the global namespace of the script doing the importing.

#### 10. What occurs if you attempt to use the 'nonlocal' keyword on a variable that exists in the Global scope but not in any Enclosing function scope?

#### 11. Which of these functions can be used to see all the names currently defined in the Global namespace?
- The **globals()** function returns a dictionary representing the current module's global symbol table.

#### 12. What is 'Variable Shadowing' in Python?
- When a variable in a narrower scope has the same name as one in a broader scope. When names collide, the innermost scope takes priority, 'shadowing' or hiding the outer variable.

#### 13. In a script containing only one function, how many total namespaces are typically active while that function is executing?
- For a non-nested function, the active layers are the function's own local scope, the script's global scope, and the interpreter's built-ins.

#### 14. Consider this problematic code:
```python
x = 10

def test():
    print(x)
    x = 20
    
test()
```
- **UnboundLocalError:** Because 'x' is assigned later in the function, Python treats it as local for the whole function, making the print attempt to use it before it is defined.

#### 15. How does Python handle namespaces for modules that are imported using 'import math'?
- A new namespace is created for the 'math' module, accessible via the name 'math'. Importing a module creates a separate namespace to prevent name clashes with your script's variables.

#### 16. What is the lifetime of a Local namespace?
- It is created when a function is called and deleted when it returns or raises an exception. Local namespaces are temporary and exist only during the execution of the specific block they belong to.

#### 17. Why is using 'from module import *' often considered bad practice in terms of namespaces?
- It can lead to 'namespace pollution' where imported names overwrite existing ones unexpectedly. This makes it hard to tell where a name came from and can cause bugs if different modules use the same names.

#### 18. When using a nested function (a closure), where does Python store the variables of the outer function that the inner function needs to remember?
- In a special attribute called closure. Closures use this attribute to store 'cell' objects that point to the variables in the enclosing scope.
- Closures & __closure__: Note that for closures, Python doesn't simply copy variables into the local namespace; it stores them in a special __closure__ attribute to maintain the link to the enclosing scope.

#### 19. If you define 'def print(x): return x' in your script, what happens when you call 'print(5)'?
- It returns 5 and displays nothing on the console. Your local/global definition 'shadows' the built-in one because Python finds your version first in the LEGB search order.

#### 20. In the context of namespaces, what is a 'Module' in Python?
- A file containing Python code that defines its own Global namespace. Every Python file acts as a module, and the variables defined at its top level constitute its global namespace.

#### 21. Which of these best describes 'Enclosing' scope?
- The scope of a function that contains a nested function. Enclosing scope is the intermediate layer that nested functions search before reaching the global level.

#### 22. What is the relationship between a Class and a Namespace?
- A Class definition creates its own namespace for its attributes and methods.Just like modules and functions, classes serve as containers for names, accessible via dot notation.

#### 23. What happens to the global namespace when you terminate a Python program?
- It is cleared from memory as the interpreter shuts down. Namespaces exist only while the process is active; they are destroyed when the program ends.


## Additional Deep Dive (Optional)

The output of `globals()` is a standard Python dictionary representing the **Global Namespace** of your current module (in this case, your script `test.py`).

Even if you haven't defined any variables yet, Python automatically populates this namespace with several "dunder" (double underscore) variables that provide metadata about the execution environment. Here is a breakdown of what those specific keys mean:

### 1. The Execution Context

* **`'__name__': '__main__'`**: This is the most important one. It tells you the name of the module. When you run a script directly (rather than importing it), Python assigns it the special name `'__main__'`.
* **`'__file__': '.../test.py'`**: This contains the full path to the script currently being executed. It's very useful for locating data files relative to your code.

### 2. The Link to the Built-ins

* **`'__builtins__': <module 'builtins'>`**: This is a reference to the **Built-in Namespace**. This is how your script "finds" the `B` in the **LEGB** rule. It contains functions like `print()`, `len()`, and `int`.

### 3. Import & Infrastructure Metadata

* **`'__loader__'` and `'__spec__'**`: these are used by Python's import machinery. They track how the module was loaded and its configuration (specification). Since this is the main script, the `SourceFileLoader` is used to read the `.py` file.
* **`'__cached__': None`**: Usually, this points to the `.pyc` (compiled bytecode) file. For the script you are running directly, it's often `None`.
* **`'__package__': None`**: This indicates whether the script is part of a larger Python package. Since it’s a standalone script, it's `None`.

### 4. Documentation and Hints

* **`'__doc__': None`**: If you had a "docstring" (a string at the very top of your file), it would be stored here.
* **`'__annotations__': {}`**: This stores variable type hints if you define any at the global level (e.g., `x: int = 5`).

### How this changes

If you were to go back to your `test.py` and add `my_var = 100` at the top level, and then call `globals()` again, you would see `'my_var': 100` added to this dictionary. This dictionary *is* your Global Namespace.