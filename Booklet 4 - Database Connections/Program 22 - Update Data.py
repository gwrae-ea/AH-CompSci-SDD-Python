import os
from pathlib import Path

import mysql.connector
from dotenv import load_dotenv
from mysql.connector import Error

base_path = Path(__file__).resolve().parent.parent
env_path = base_path / '.env'
load_dotenv(dotenv_path=env_path)


def get_non_empty_text(prompt, max_length=20):
    while True:
        value = input(prompt).strip()
        if not value:
            print("Error: This field cannot be empty.")
            continue
        if len(value) > max_length:
            print(f"Error: Maximum length is {max_length} characters.")
            continue
        return value


def get_optional_text(prompt, current_value, max_length=20):
    while True:
        value = input(prompt).strip()
        if value == "":
            return current_value
        if len(value) > max_length:
            print(f"Error: Maximum length is {max_length} characters.")
            continue
        return value


def get_positive_int(prompt):
    while True:
        value = input(prompt).strip()
        try:
            number = int(value)
            if number <= 0:
                print("Error: Please enter a whole number greater than 0.")
                continue
            return number
        except ValueError:
            print("Error: Please enter a valid whole number.")


def get_optional_positive_float(prompt, current_value):
    while True:
        value = input(prompt).strip()
        if value == "":
            return current_value
        try:
            number = float(value)
            if number <= 0:
                print("Error: Salary must be greater than 0.")
                continue
            return number
        except ValueError:
            print("Error: Please enter a valid number for salary.")


def update_employee():
    db_host = os.getenv('DB_HOST')
    db_user = os.getenv('DB_USER')
    db_pass = os.getenv('DB_PASS')
    db_name = os.getenv('DB_NAME')

    missing = [name for name, val in [('DB_HOST', db_host), ('DB_USER', db_user),
                                       ('DB_PASS', db_pass), ('DB_NAME', db_name)] if not val]
    if missing:
        print(f"Configuration Error: Missing environment variable(s): {', '.join(missing)}")
        return

    try:
        conn = mysql.connector.connect(
            host=db_host,
            user=db_user,
            password=db_pass,
            database=db_name
        )
    except Error as e:
        print(f"Connection Error: {e}")
        return

    cursor = None

    try:
        cursor = conn.cursor()

        print("--- Update Employee Record ---")
        employee_id = get_positive_int("Enter Employee ID to update: ")

        select_query = """
            SELECT id, name, position, salary, department
            FROM Employees
            WHERE id = %s
        """
        cursor.execute(select_query, (employee_id,))
        employee = cursor.fetchone()

        if employee is None:
            print(f"No employee found with ID {employee_id}.")
            return

        print("Leave a field blank to keep its current value.")
        print(
            f"Current values: Name={employee[1]}, Position={employee[2]}, "
            f"Salary={employee[3]}, Department={employee[4]}"
        )

        new_name = get_optional_text("Enter New Name: ", employee[1])
        new_position = get_optional_text("Enter New Position: ", employee[2])
        new_salary = get_optional_positive_float("Enter New Salary: ", employee[3])
        new_department = get_optional_text("Enter New Department: ", employee[4])

        update_query = """
            UPDATE Employees
            SET name = %s, position = %s, salary = %s, department = %s
            WHERE id = %s
        """
        values = (new_name, new_position, new_salary, new_department, employee_id)

        cursor.execute(update_query, values)
        conn.commit()

        if cursor.rowcount == 0:
            print("No changes were made.")
        else:
            print(f"Successfully updated employee ID {employee_id}.")

    except Error as e:
        print(f"Database Error: {e}")
        conn.rollback()
    finally:
        if conn.is_connected():
            if cursor is not None:
                cursor.close()
            conn.close()


if __name__ == "__main__":
    update_employee()
