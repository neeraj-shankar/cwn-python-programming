This is your "In Case of Emergency" guide. Keep this nearby during development or right before an interview to keep the syntax fresh.

---

## 🚀 Pytest Mastery Cheatsheet

### 1. The Basics (CLI)

| Command | Action |
| --- | --- |
| `pytest` | Run all tests in current directory. |
| `pytest -v` | **Verbose**: Shows name of each test and status. |
| `pytest -k "expression"` | Run tests matching a keyword (e.g., `-k "login"`). |
| `pytest -x` | **Exit** immediately on first failure. |
| `pytest --lf` | Run only the tests that **Last Failed**. |
| `pytest --tb=short` | Shorter, cleaner error tracebacks. |

---

### 2. Assertions & Exceptions

```python
assert a == b             # Equality
assert a is True          # Identity
assert "part" in string   # Membership
assert 0.1 + 0.2 == approx(0.3) # Floating point

# Testing for expected errors
with pytest.raises(TypeError) as excinfo:
    func_that_fails()
assert "specific message" in str(excinfo.value)

```

---

### 3. Fixtures (The Lifecycle)

```python
@pytest.fixture(scope="module")
def db_conn():
    # Setup code
    db = connect()
    yield db 
    # Teardown code (runs after tests)
    db.close()

def test_query(db_conn):
    assert db_conn.is_active

```

* **Scopes:** `function` (default), `class`, `module`, `package`, `session`.

---

### 4. Parametrization (Data-Driven)

```python
@pytest.mark.parametrize("input, expected", [
    (1, 2),
    (5, 6),
    (10, 11),
], ids=["small", "medium", "large"])
def test_increment(input, expected):
    assert input + 1 == expected

```

---

### 5. Mocking & Monkeypatching

```python
# Mocker (requires pytest-mock)
def test_api(mocker):
    # Patching the return value
    mock_call = mocker.patch("app.api.get_data", return_value={"id": 1})
    # Verification
    mock_call.assert_called_once()

# Monkeypatch (built-in)
def test_env(monkeypatch):
    monkeypatch.setenv("DB_URL", "localhost:5432")
    monkeypatch.setattr(obj, "attr", value)

```

---

### 6. Markers (Organizing Tests)

```python
@pytest.mark.skip(reason="not implemented yet")
@pytest.mark.skipif(sys.platform == "win32", reason="Linux only")
@pytest.mark.slow    # Custom marker (requires config in pyproject.toml)
@pytest.mark.xfail   # We expect this to fail

```

---

### 7. Configuration (`pyproject.toml`)

This is the modern way to configure your test suite.

```toml
[tool.pytest.ini_options]
testpaths = ["tests"]
python_files = "test_*.py"
markers = [
    "slow: marks tests as slow (deselect with '-m \"not slow\"')",
]
addopts = "-v --tb=short"

```

---

## 🏆 Phase 5: Code Coverage

Now that you have the cheatsheet, we need to know: **"What did we miss?"**

Code coverage tells you exactly which lines of your source code were executed during the tests. We use a plugin called `pytest-cov`.

**Would you like me to show you how to generate a "Visual Coverage Report" (HTML) so you can literally see the gaps in your testing?**