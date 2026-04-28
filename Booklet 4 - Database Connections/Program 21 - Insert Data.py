import os
from datetime import date
from pathlib import Path

import mysql.connector
from dotenv import load_dotenv
from mysql.connector import Error

base_path = Path(__file__).resolve().parent.parent
env_path = base_path / '.env'
load_dotenv(dotenv_path=env_path)

def insert_employee():
    try:
        conn = mysql.connector.connect(
            host=os.getenv('DB_HOST'),
            user=os.getenv('DB_USER'),
            password=os.getenv('DB_PASS'),
            database=os.getenv('DB_NAME')
        )
    except Error as e:
        print(f"Connection Error: {e}")
        return

    cursor = None

    try:
        cursor = conn.cursor()

        print("--- Add New Employee Record ---")
        name = input("Enter Employee Name: ")
        # Changed 'role' to 'position' to match your SQL file
        position = input("Enter Job Position: ") 
        salary = float(input("Enter Salary: "))
        department = input("Enter Department: ")
        # Auto-generating today's date for hireDate
        hire_date = str(date.today())

        # Updated query to match your exact SQL column names
        query = """
            INSERT INTO Employees (name, position, salary, department, hireDate) 
            VALUES (%s, %s, %s, %s, %s)
        """
        values = (name, position, salary, department, hire_date)
        
        cursor.execute(query, values)
        conn.commit()
        
        print(f"Successfully added {name} to the Employees table.")

    except Error as e:
        print(f"Database Error: {e}")
        conn.rollback() 
    except ValueError:
        print("Error: Please enter a valid number for the salary.")
    finally:
        if conn.is_connected():
            if cursor is not None:
                cursor.close()
            conn.close()

if __name__ == "__main__":
    insert_employee()