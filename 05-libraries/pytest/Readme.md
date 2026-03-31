# Phase 1: The Foundations

## Discovery Rules:
- Test files and functions are named `test_*.py` and `test_*` mainly for automatic test discovery.
- Test runners like pytest scan the filesystem using naming conventions to identify which files and functions contain tests, without requiring any manual registration or configuration.
- This makes the test framework simple, fast, and zero-config, while keeping tests clearly separated from production code.”

```python
for file in all_files:
    if file matches "test_*.py":
        import file
        for function in file:
            if function name starts with "test_":
                run it
```

## The power of **`assert`**
In most Python testing frameworks, you have to memorize a whole library of methods like `self.assertEqual()`, `self.assertAlmostEqual()`, or `self.assertIsInstance()`.

In pytest, you only need the standard Python assert
- The "magic" happens behind the scenes. When you run pytest, it intercepts these assertions and rewrites them so that if they fail, you get a detailed "autopsy" of what went wrong.

## Fixture
Think of a fixture as a resource provider. If your test needs a *database connection*, a temporary file, or a logged-in API client, you define a fixture to "provide" that object.

- *A fixture is a dependency injection tool that decouples the environment setup from the test logic, allowing for modular, reusable, and scoped resource management.*

### Scope of Fixtures

| **Scope**            | **Lifetime**                            | **Best For**                            |
| -------------------- | --------------------------------------- | --------------------------------------- |
| function *(Default)* | Setup/Teardown for every test           | Clean state, simple objects             |
| class                | Setup/Teardown once per test class      | Sharing state across related methods    |
| module               | Setup/Teardown once per Python file     | Database connections used by many tests |
| session              | Setup/Teardown once per entire test run | Global config, heavy API clients        |

## The Mocking
Mocking is the art of replacing a real, complex part of your system (like a Stripe API, a slow Database, or a weather service) with a "fake" object that behaves exactly how you want it to.

### Why Mock?
Imagine you have a function that sends an email when a user signs up.

- You don't want to send a real email every time you run a test.
- You don't want your test to fail just because the email server is down.
- You want to verify that the send_email function was called with the right address.