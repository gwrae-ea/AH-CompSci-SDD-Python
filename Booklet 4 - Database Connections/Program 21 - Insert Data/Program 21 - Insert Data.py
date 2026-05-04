import os
from datetime import date
from pathlib import Path

import mysql.connector
from dotenv import load_dotenv
from mysql.connector import Error

base_path = Path(__file__).resolve().parent.parent.parent
env_path = base_path / '.env'
load_dotenv(dotenv_path=env_path)

def insert_employee():
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
        # FR6: connect to the database to execute required queries.
        conn = mysql.connector.connect(
            host=db_host,
            user=db_user,
            password=db_pass,
            database=db_name
        )
    except Error as e:
        # FR11: provide clear failure feedback to the user.
        print(f"Connection Error: {e}")
        return

    cursor = None

    try:
        cursor = conn.cursor()

        # FR7: interface prompt to receive query input values.
        print("--- Add New Employee Record ---")

        # FR10: validate mandatory text input (name cannot be blank).
        name = input("Enter Employee Name: ").strip()
        while not name:
            print("Error: Employee name cannot be empty.")
            name = input("Enter Employee Name: ").strip()

        # FR10: validate mandatory text input (position cannot be blank).
        position = input("Enter Job Position: ").strip()
        while not position:
            print("Error: Job position cannot be empty.")
            position = input("Enter Job Position: ").strip()

        # FR9: validate keyboard numeric input (salary format and range).
        salary = None
        while salary is None:
            try:
                salary = float(input("Enter Salary: ").strip())
                if salary < 0:
                    print("Error: Salary cannot be negative.")
                    salary = None
            except ValueError:
                print("Error: Please enter a valid number for the salary.")

        # FR10: validate mandatory text input (department cannot be blank).
        department = input("Enter Department: ").strip()
        while not department:
            print("Error: Department cannot be empty.")
            department = input("Enter Department: ").strip()

        # FR7: include system-generated value for formatted output/data capture.
        hire_date = str(date.today())

        # FR5/FR6: execute an INSERT against the employee table using parameters.
        query = """
            INSERT INTO Employees (name, position, salary, department, hireDate) 
            VALUES (%s, %s, %s, %s, %s)
        """
        values = (name, position, salary, department, hire_date)
        
        cursor.execute(query, values)
        # FR15: commit transaction to keep the database in a consistent state.
        conn.commit()
        
        # FR11: provide clear success feedback to the user.
        print(f"Successfully added {name} to the Employees table.")

    except Error as e:
        # FR14/FR15: show meaningful error context and roll back failed transaction.
        print(f"Database Error: {e}")
        conn.rollback()
    finally:
        if conn.is_connected():
            if cursor is not None:
                cursor.close()
            conn.close()
            # FR11: always close resources safely after processing.

if __name__ == "__main__":
    insert_employee()