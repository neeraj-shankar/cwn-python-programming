"""
csv_to_mysql.py
---------------
Reads a flat employee CSV and loads it into 4 normalized MySQL tables
with proper foreign-key relationships.

Schema
------
  employees        (emp_code PK, name, age, gender)
  departments      (dept_id PK AUTO, department_name UNIQUE)
  jobs             (job_id  PK AUTO, job_title, job_location)
  employee_details (detail_id PK AUTO,
                    emp_code  FK → employees,
                    dept_id   FK → departments,
                    job_id    FK → jobs,
                    salary, experience, joining_date, performance)

Prerequisites
-------------
  pip install mysql-connector-python pandas

Usage
-----
  1. Edit CONFIG below (host, user, password, database).
  2. python csv_to_mysql.py                    # uses employees.csv by default
  2. python csv_to_mysql.py my_file.csv        # or pass a custom path
"""

import sys
import logging
from pathlib import Path

import pandas as pd
import mysql.connector
from mysql.connector import Error, MySQLConnection

# ─────────────────────────────────────────────
# ❶  CONFIGURATION  – edit before running
# ─────────────────────────────────────────────
CONFIG = {
    "host":     "localhost",
    "port":     3306,
    "user":     "root",          # ← your MySQL username
    "password": "John@7982", # ← your MySQL password
    "database": "employee_db",   # will be created if absent
}

CSV_PATH = Path(sys.argv[1]) if len(sys.argv) > 1 else Path("employees.csv")

# ─────────────────────────────────────────────
# Logging
# ─────────────────────────────────────────────
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s  %(levelname)-8s  %(message)s",
    datefmt="%H:%M:%S",
)
log = logging.getLogger(__name__)


# ─────────────────────────────────────────────
# ❷  DDL STATEMENTS
# ─────────────────────────────────────────────

DDL_EMPLOYEES = """
CREATE TABLE IF NOT EXISTS employees (
    emp_code  VARCHAR(20)  NOT NULL,
    name      VARCHAR(100) NOT NULL,
    age       TINYINT UNSIGNED NOT NULL,
    gender    VARCHAR(20)  NOT NULL,
    PRIMARY KEY (emp_code)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
"""

DDL_DEPARTMENTS = """
CREATE TABLE IF NOT EXISTS departments (
    dept_id         INT UNSIGNED NOT NULL AUTO_INCREMENT,
    department_name VARCHAR(100) NOT NULL,
    PRIMARY KEY (dept_id),
    UNIQUE KEY uq_dept_name (department_name)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
"""

DDL_JOBS = """
CREATE TABLE IF NOT EXISTS jobs (
    job_id       INT UNSIGNED NOT NULL AUTO_INCREMENT,
    job_title    VARCHAR(100) NOT NULL,
    job_location VARCHAR(100) NOT NULL,
    PRIMARY KEY (job_id),
    UNIQUE KEY uq_job (job_title, job_location)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
"""

DDL_EMPLOYEE_DETAILS = """
CREATE TABLE IF NOT EXISTS employee_details (
    detail_id    INT UNSIGNED  NOT NULL AUTO_INCREMENT,
    emp_code     VARCHAR(20)   NOT NULL,
    dept_id      INT UNSIGNED  NOT NULL,
    job_id       INT UNSIGNED  NOT NULL,
    salary       DECIMAL(12,2) NOT NULL,
    experience   TINYINT UNSIGNED NOT NULL,
    joining_date DATE          NOT NULL,
    performance  VARCHAR(30)   NOT NULL,
    PRIMARY KEY (detail_id),
    UNIQUE KEY uq_emp (emp_code),                                 -- 1-to-1 with employees
    CONSTRAINT fk_ed_emp  FOREIGN KEY (emp_code) REFERENCES employees(emp_code)
        ON DELETE CASCADE ON UPDATE CASCADE,
    CONSTRAINT fk_ed_dept FOREIGN KEY (dept_id)  REFERENCES departments(dept_id)
        ON DELETE RESTRICT ON UPDATE CASCADE,
    CONSTRAINT fk_ed_job  FOREIGN KEY (job_id)   REFERENCES jobs(job_id)
        ON DELETE RESTRICT ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
"""


# ─────────────────────────────────────────────
# ❸  HELPERS
# ─────────────────────────────────────────────

def get_connection(cfg: dict, with_db: bool = True) -> MySQLConnection:
    """Return a mysql-connector connection, optionally without selecting a DB."""
    params = {k: v for k, v in cfg.items() if k != "database"} if not with_db else cfg
    conn = mysql.connector.connect(**params)
    conn.autocommit = False
    return conn


def ensure_database(cfg: dict) -> None:
    """Create the target database if it doesn't exist yet."""
    conn = get_connection(cfg, with_db=False)
    try:
        cur = conn.cursor()
        cur.execute(
            f"CREATE DATABASE IF NOT EXISTS `{cfg['database']}` "
            "CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci;"
        )
        log.info("Database '%s' ready.", cfg["database"])
    finally:
        conn.close()


def create_tables(conn: MySQLConnection) -> None:
    """Run all DDL statements in the correct FK-safe order."""
    cur = conn.cursor()
    for ddl in (DDL_EMPLOYEES, DDL_DEPARTMENTS, DDL_JOBS, DDL_EMPLOYEE_DETAILS):
        cur.execute(ddl)
    conn.commit()
    log.info("All 4 tables created (or already exist).")


# ─────────────────────────────────────────────
# ❹  LOAD  – each dimension table first, then the fact table
# ─────────────────────────────────────────────

def load_employees(cur, df: pd.DataFrame) -> None:
    """Insert / update the employees dimension."""
    sql = """
        INSERT INTO employees (emp_code, name, age, gender)
        VALUES (%s, %s, %s, %s)
        ON DUPLICATE KEY UPDATE
            name   = VALUES(name),
            age    = VALUES(age),
            gender = VALUES(gender);
    """
    records = df[["emp_code", "name", "age", "gender"]].itertuples(index=False, name=None)
    cur.executemany(sql, list(records))
    log.info("  employees   : %d rows upserted.", cur.rowcount)


def load_departments(cur, df: pd.DataFrame) -> None:
    """Insert unique department names; ignore duplicates."""
    unique_depts = df["department_name"].dropna().unique().tolist()
    sql = """
        INSERT IGNORE INTO departments (department_name)
        VALUES (%s);
    """
    cur.executemany(sql, [(d,) for d in unique_depts])
    log.info("  departments : %d unique names processed.", len(unique_depts))


def load_jobs(cur, df: pd.DataFrame) -> None:
    """Insert unique (job_title, job_location) combinations; ignore duplicates."""
    unique_jobs = (
        df[["job_title", "job_location"]]
        .drop_duplicates()
        .itertuples(index=False, name=None)
    )
    sql = """
        INSERT IGNORE INTO jobs (job_title, job_location)
        VALUES (%s, %s);
    """
    cur.executemany(sql, list(unique_jobs))
    log.info("  jobs        : unique job combos processed.")


def load_employee_details(cur, df: pd.DataFrame) -> None:
    """
    Resolve FK ids from the dimension tables and insert the fact rows.
    Uses a single JOIN-heavy INSERT … SELECT to avoid per-row round-trips.
    """
    # Build a temporary staging table in memory (MEMORY engine is fast for this)
    cur.execute("DROP TEMPORARY TABLE IF EXISTS _staging;")
    cur.execute("""
        CREATE TEMPORARY TABLE _staging (
            emp_code     VARCHAR(20),
            dept_name    VARCHAR(100),
            job_title    VARCHAR(100),
            job_location VARCHAR(100),
            salary       DECIMAL(12,2),
            experience   TINYINT UNSIGNED,
            joining_date DATE,
            performance  VARCHAR(30)
        ) ENGINE=MEMORY DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
    """)

    stage_sql = """
        INSERT INTO _staging
               (emp_code, dept_name, job_title, job_location,
                salary, experience, joining_date, performance)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s);
    """
    stage_rows = df[[
        "emp_code", "department_name", "job_title", "job_location",
        "salary", "experience", "joining_date", "performance"
    ]].itertuples(index=False, name=None)
    cur.executemany(stage_sql, list(stage_rows))

    # Resolve FKs and insert into the real table in one shot
    cur.execute("""
        INSERT INTO employee_details
               (emp_code, dept_id, job_id, salary, experience, joining_date, performance)
        SELECT  s.emp_code,
                d.dept_id,
                j.job_id,
                s.salary,
                s.experience,
                s.joining_date,
                s.performance
        FROM    _staging s
        JOIN    departments d ON d.department_name = s.dept_name
        JOIN    jobs         j ON j.job_title       = s.job_title
                              AND j.job_location    = s.job_location
        ON DUPLICATE KEY UPDATE
            dept_id      = VALUES(dept_id),
            job_id       = VALUES(job_id),
            salary       = VALUES(salary),
            experience   = VALUES(experience),
            joining_date = VALUES(joining_date),
            performance  = VALUES(performance);
    """)
    log.info("  employee_details: %d rows upserted.", cur.rowcount)

    cur.execute("DROP TEMPORARY TABLE IF EXISTS _staging;")


# ─────────────────────────────────────────────
# ❺  VALIDATION
# ─────────────────────────────────────────────

def validate(cur) -> None:
    """Quick sanity checks – prints row counts and a joined sample."""
    log.info("── Validation ─────────────────────────────────────────")
    for table in ("employees", "departments", "jobs", "employee_details"):
        cur.execute(f"SELECT COUNT(*) FROM {table};")
        count = cur.fetchone()[0]
        log.info("  %-20s: %d rows", table, count)

    log.info("Sample joined output (first 3 rows):")
    cur.execute("""
        SELECT  e.emp_code,
                e.name,
                e.age,
                e.gender,
                d.department_name,
                j.job_title,
                j.job_location,
                ed.salary,
                ed.experience,
                ed.joining_date,
                ed.performance
        FROM    employees        e
        JOIN    employee_details ed USING (emp_code)
        JOIN    departments      d  USING (dept_id)
        JOIN    jobs             j  USING (job_id)
        LIMIT   3;
    """)
    cols = [desc[0] for desc in cur.description]
    for row in cur.fetchall():
        log.info("  %s", dict(zip(cols, row)))


# ─────────────────────────────────────────────
# ❻  MAIN PIPELINE
# ─────────────────────────────────────────────

def main() -> None:
    # ── 1. Read & validate CSV ──────────────────
    if not CSV_PATH.exists():
        log.error("CSV file not found: %s", CSV_PATH)
        sys.exit(1)

    log.info("Reading %s …", CSV_PATH)
    df = pd.read_csv(CSV_PATH)

    required = {
        "emp_code", "name", "age", "gender",
        "department_name",
        "job_title", "job_location",
        "salary", "experience", "joining_date", "performance",
    }
    missing = required - set(df.columns)
    if missing:
        log.error("CSV is missing columns: %s", missing)
        sys.exit(1)

    # Light cleanup
    df["joining_date"] = pd.to_datetime(df["joining_date"]).dt.date
    df = df.dropna(subset=list(required))
    log.info("%d valid rows after cleanup.", len(df))

    # ── 2. Set up database & tables ────────────
    ensure_database(CONFIG)
    conn = get_connection(CONFIG)

    try:
        create_tables(conn)
        cur = conn.cursor()

        log.info("Loading data …")
        # Dimension tables first (no FK dependencies)
        load_employees(cur, df)
        load_departments(cur, df)
        load_jobs(cur, df)
        # Fact table last (depends on all three dimensions)
        load_employee_details(cur, df)

        conn.commit()
        log.info("All data committed successfully.")

        validate(cur)

    except Error as exc:
        conn.rollback()
        log.error("MySQL error – transaction rolled back: %s", exc)
        raise
    finally:
        conn.close()
        log.info("Connection closed.")


if __name__ == "__main__":
    main()