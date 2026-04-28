import os
from pathlib import Path

import mysql.connector
from dotenv import load_dotenv
from mysql.connector import Error

base_path = Path(__file__).resolve().parent.parent
env_path = base_path / '.env'
load_dotenv(dotenv_path=env_path)


# Define the Class structure
class Employee:
    def __init__(self, id, name, salary, department, position, hireDate):
        self.id = id
        self.name = name
        self.salary = salary
        self.department = department
        self.position = position
        self.hireDate = hireDate


def select_employees():
    try:
        conn = mysql.connector.connect(
            host=os.getenv('DB_HOST'),
            user=os.getenv('DB_USER'),
            password=os.getenv('DB_PASS'),
            database=os.getenv('DB_NAME')
        )
    except Error as err:
        print(f"Connection Error: {err}")
        return

    cursor = None

    try:
        query = "SELECT * FROM Employees"
        cursor = conn.cursor()

        cursor.execute(query)
        db_rows = cursor.fetchall()

        results = []
        for row in db_rows:
            results.append(Employee(row[0], row[1], row[2], row[3], row[4], row[5]))

        print(f"{'id':<10}{'name':<20}{'salary':<12}{'dept':<30}{'position':<30}{'date':<12}")

        for worker in results:
            print(f"{str(worker.id):<10}{str(worker.name):<20}{str(worker.salary):<12}"
                  f"{str(worker.department):<30}{str(worker.position):<30}{str(worker.hireDate):<12}")

    except Error as err:
        print(f"Connection failed: {err}")
    finally:
        if conn.is_connected():
            if cursor is not None:
                cursor.close()
            conn.close()


if __name__ == "__main__":
    select_employees()
