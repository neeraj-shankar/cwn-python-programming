import sqlite3
from contextlib import contextmanager

@contextmanager
def database_transaction(db_path):
    """Context manager to handle database transactions."""
    conn = sqlite3.connect(db_path)  # Setup: Connect to the database
    cursor = conn.cursor()
    try:
        yield cursor  # Provide the cursor for database operations
        conn.commit()  # Commit the transaction if successful
    except Exception as e:
        conn.rollback()  # Rollback the transaction in case of an error
        print(f"Transaction rolled back due to: {e}")
        raise  # Re-raise the exception for further handling
    finally:
        conn.close()  # Ensure the connection is always closed

# Using the context manager
db_path = "example.db"

with database_transaction(db_path) as cursor:
    # Create a table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            age INTEGER NOT NULL
        )
    """)
    # Insert a record
    cursor.execute("INSERT INTO users (name, age) VALUES (?, ?)", ("Alice", 30))

    # Uncomment the line below to simulate an error
    # cursor.execute("INSERT INTO non_existent_table VALUES (1)")

    # Query the database
    cursor.execute("SELECT * FROM users")
    print(cursor.fetchall())
