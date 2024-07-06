@pytest.fixture
-----------------------------------------------------------------------------------------------------------------------
Structure:
-----------------------------------------------------------------------------------------
@fixture(fixture_function=None, *, scope='function', params=None, autouse=False, ids=None, name=None)
-----------------------------------------------------------------------------------------

1. This decorator can be used, with or without parameters, to define a fixture function.
2. Test functions can directly use fixture names as input arguments in which case the fixture instance returned 
   from the fixture function will be injected.

1.  monkeypatch
-----------------------------------------------------------------------------------------
A built-in fixture that provides a way to dynamically modify attributes or behaviors of objects during test execution.
It allows you to "patch" or "mock" objects, functions, or methods temporarily within the scope of a test function,
without modifying the actual implementation.

Use case
------------------
1. Patching Environment Variables
2. Mocking External API Calls



