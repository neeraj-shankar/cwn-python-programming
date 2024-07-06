Introduction
-----------------------------------------------------------------------------------------------------------------------
pytest is a powerful testing framework for Python, and it provides various command-line options (flags) that 
allow you to customize the test execution.

Some commonly used flags with the pytest command:

-v or --verbose:
-----------------------------------------------------------------------------------------
This flag increases the verbosity level, providing more detailed information about the tests being executed. 
It shows the name of each test function and its status (passed, failed, skipped, etc.).

-q or --quiet:
-----------------------------------------------------------------------------------------
This flag decreases the verbosity level, suppressing most of the detailed information and only displaying the overall
test results.

-k EXPRESSION:
-----------------------------------------------------------------------------------------
This flag allows you to select and run tests based on a substring match against their names.

-m MARKEXPR:
-----------------------------------------------------------------------------------------
This flag allows you to select and run tests based on their markers. 

-x or --exitfirst
-----------------------------------------------------------------------------------------
This flag stops the test run after the first failure. If a test fails, pytest will stop executing further tests 
and exit immediately.

--maxfail=num:
-----------------------------------------------------------------------------------------
This flag specifies the maximum number of failures before stopping the test run. If the number of failures exceeds 
the specified limit, pytest will stop executing further tests and exit.

--tb=style:
-----------------------------------------------------------------------------------------
This flag sets the traceback style for reporting test failures. You can specify various styles like short, 
line, no, native, etc., to customize the traceback format.

-s or --capture=no:
-----------------------------------------------------------------------------------------
By default, pytest captures the output (stdout and stderr) during test execution. This flag disables output 
capturing, allowing you to see the output directly in the console.

--durations=N:
-----------------------------------------------------------------------------------------
This flag displays the N slowest tests and their durations at the end of the test run. It helps you identify 
and optimize slow-running tests.

--ignore=path:
-----------------------------------------------------------------------------------------
This flag tells pytest to ignore the specified path or directory when discovering and running tests. You can 
use this flag to exclude certain parts of your codebase from being tested.

--cov=APP_NAME:
-----------------------------------------------------------------------------------------
This flag enables coverage reporting using the pytest-cov plugin. Replace APP_NAME with the name of your 
application to generate a coverage report for your codebase.

--cov-report=TYPE
-----------------------------------------------------------------------------------------
This flag specifies the type of coverage report to generate. You can specify different report types 
like term, html, xml, json, etc


