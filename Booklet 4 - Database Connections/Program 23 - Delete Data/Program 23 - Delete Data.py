import os
from pathlib import Path

import mysql.connector
from dotenv import load_dotenv
from mysql.connector import Error

base_path = Path(__file__).resolve().parent.parent.parent
env_path = base_path / '.env'
load_dotenv(dotenv_path=env_path)


def get_positive_int(prompt):
    # FR9: validate numeric keyboard input for positive integer IDs.
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


def get_delete_confirmation(prompt):
    # FR10: validate confirmation text input before delete action.
    while True:
        value = input(prompt).strip().lower()
        if value in ("y", "yes"):
            return True
        if value in ("n", "no"):
            return False
        print("Error: Please enter Yes or No.")


def delete_employee():
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
        # FR6: connect to the database to execute lookup and delete queries.
        conn = mysql.connector.connect(
            host=db_host,
            user=db_user,
            password=db_pass,
            database=db_name
        )
    except Error as e:
        # FR11: report connection errors clearly.
        print(f"Connection Error: {e}")
        return

    cursor = None

    try:
        cursor = conn.cursor()

        # FR7: interface prompt to receive query input value.
        print("--- Delete Employee Record ---")
        employee_id = get_positive_int("Enter Employee ID to delete: ")

        # FR6/FR12: select existing record and validate it exists.
        select_query = """
            SELECT id, name, position, salary, department
            FROM Employees
            WHERE id = %s
        """
        cursor.execute(select_query, (employee_id,))
        employee = cursor.fetchone()

        if employee is None:
            # FR11: clear not-found feedback for invalid target ID.
            print(f"No employee found with ID {employee_id}.")
            return

        # FR7: show current record and ask for confirmation.
        print("Record found:")
        print(
            f"ID={employee[0]}, Name={employee[1]}, Position={employee[2]}, "
            f"Salary={employee[3]}, Department={employee[4]}"
        )

        confirm = get_delete_confirmation("Are you sure you want to delete this record? (Yes/No): ")
        if not confirm:
            print("Delete cancelled. No changes made.")
            return

        # FR6: execute parameterised DELETE query.
        delete_query = "DELETE FROM Employees WHERE id = %s"
        cursor.execute(delete_query, (employee_id,))

        # FR15: commit successful transaction to maintain consistency.
        conn.commit()

        if cursor.rowcount == 0:
            print("No record was deleted.")
        else:
            print(f"Successfully deleted employee ID {employee_id}.")

    except Error as e:
        # FR14/FR15: show error context and roll back failed transaction.
        print(f"Database Error: {e}")
        conn.rollback()
    finally:
        if conn.is_connected():
            if cursor is not None:
                cursor.close()
            conn.close()
            # FR11: always close resources safely.


if __name__ == "__main__":
    delete_employee()
