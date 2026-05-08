import os
from pathlib import Path

import mysql.connector
from dotenv import load_dotenv
from mysql.connector import Error

base_path = Path(__file__).resolve().parent.parent.parent
env_path = base_path / '.env'
load_dotenv(dotenv_path=env_path)


# FR1: developer-defined class for object-oriented solution.
class Employee:
    def __init__(self, id, name, salary, department, position, hireDate):
        self.id = int(id)
        self.name = str(name)
        self.salary = float(salary)
        self.department = str(department)
        self.position = str(position)
        self.hireDate = str(hireDate)


def select_employees():
    # FR8: validate required environment configuration values.
    db_host = os.getenv('DB_HOST')
    db_user = os.getenv('DB_USER')
    db_pass = os.getenv('DB_PASS')
    db_name = os.getenv('DB_NAME')

    missing = [name for name, val in [('DB_HOST', db_host), ('DB_USER', db_user),
                                       ('DB_PASS', db_pass), ('DB_NAME', db_name)] if not val]
    if missing:
        # FR11: provide clear failure feedback to the user.
        print(f"Configuration Error: Missing environment variable(s): {', '.join(missing)}")
        return

    try:
        # FR6: connect to the database to execute retrieval query.
        conn = mysql.connector.connect(
            host=db_host,
            user=db_user,
            password=db_pass,
            database=db_name
        )
    except Error as err:
        # FR11: report connection errors clearly.
        print(f"Connection Error: {err}")
        return

    cursor = None

    try:
        # FR6: execute SELECT query against employee table.
        query = "SELECT * FROM Employees"
        cursor = conn.cursor()

        cursor.execute(query)
        db_rows = cursor.fetchall()

        # FR2: create and populate an array of Employee objects.
        num_rows = len(db_rows)
        results = [None] * num_rows
        for i in range(num_rows):
            row = db_rows[i]
            results[i] = Employee(row[0], row[1], row[2], row[3], row[4], row[5])

        # FR7: display formatted query output.
        print(f"{'id':<10}{'name':<20}{'salary':<12}{'dept':<30}{'position':<30}{'date':<12}")

        for worker in results:
            print(f"{str(worker.id):<10}{str(worker.name):<20}{str(worker.salary):<12}"
                  f"{str(worker.department):<30}{str(worker.position):<30}{str(worker.hireDate):<12}")

    except Error as err:
        # FR14: include meaningful error context when query fails.
        print(f"Connection failed: {err}")
    finally:
        if conn.is_connected():
            if cursor is not None:
                cursor.close()
            conn.close()
            # FR11: always close resources safely.


if __name__ == "__main__":
    select_employees()
