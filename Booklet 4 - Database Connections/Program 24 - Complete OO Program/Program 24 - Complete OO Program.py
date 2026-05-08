import os
from pathlib import Path

import mysql.connector
from dotenv import load_dotenv
from mysql.connector import Error

# Load the .env file from the workspace root (three levels up from this script)
base_path = Path(__file__).resolve().parent.parent.parent
env_path = base_path / '.env'
load_dotenv(dotenv_path=env_path)


class Employee:
    # FR1: developer-defined class with encapsulated properties.
    def __init__(self, employee_id, name, salary, department, position, hire_date):
        self.__id = None
        self.__name = ""
        self.__salary = 0.0
        self.__department = ""
        self.__position = ""
        self.__hire_date = ""

        # FR1: use setter methods to validate and assign values.
        self.set_id(employee_id)
        self.set_name(name)
        self.set_salary(salary)
        self.set_department(department)
        self.set_position(position)
        self.set_hire_date(hire_date)

    def get_id(self):
        return self.__id

    def get_name(self):
        return self.__name

    def get_salary(self):
        return self.__salary

    def get_department(self):
        return self.__department

    def get_position(self):
        return self.__position

    def get_hire_date(self):
        return self.__hire_date

    def set_id(self, employee_id):
        if isinstance(employee_id, int) and employee_id > 0:
            self.__id = employee_id
        else:
            raise ValueError("Employee ID must be a whole number greater than 0.")

    def set_name(self, name):
        cleaned = str(name).strip()
        if 1 <= len(cleaned) <= 20:
            self.__name = cleaned
        else:
            raise ValueError("Employee name must be 1 to 20 characters long.")

    def set_salary(self, salary):
        try:
            salary_value = float(salary)
        except (TypeError, ValueError) as exc:
            raise ValueError("Salary must be numeric.") from exc

        if salary_value > 0:
            self.__salary = round(salary_value, 2)
        else:
            raise ValueError("Salary must be greater than 0.")

    def set_department(self, department):
        cleaned = str(department).strip()
        if 1 <= len(cleaned) <= 20:
            self.__department = cleaned
        else:
            raise ValueError("Department must be 1 to 20 characters long.")

    def set_position(self, position):
        cleaned = str(position).strip()
        if 1 <= len(cleaned) <= 20:
            self.__position = cleaned
        else:
            raise ValueError("Position must be 1 to 20 characters long.")

    def set_hire_date(self, hire_date):
        cleaned = str(hire_date).strip()
        if cleaned:
            self.__hire_date = cleaned
        else:
            raise ValueError("Hire date cannot be empty.")


def get_non_empty_text(prompt, max_length=20):
    # FR10: validate mandatory text input.
    while True:
        value = input(prompt).strip()
        if not value:
            print("Error: This field cannot be empty.")
            continue
        if len(value) > max_length:
            print(f"Error: Maximum length is {max_length} characters.")
            continue
        return value


def get_positive_float(prompt):
    # FR9: validate numeric keyboard input for salary filter.
    while True:
        value = input(prompt).strip()
        try:
            number = float(value)
            if number <= 0:
                print("Error: Please enter a number greater than 0.")
                continue
            return number
        except ValueError:
            print("Error: Please enter a valid number.")


def get_percentage(prompt):
    # FR9: validate numeric keyboard input for percentage values.
    while True:
        value = input(prompt).strip()
        try:
            number = float(value)
            if number < 0 or number > 100:
                print("Error: Please enter a percentage from 0 to 100.")
                continue
            return number
        except ValueError:
            print("Error: Please enter a valid number.")


def validate_environment_config():
    # FR8: validate required environment configuration values.
    db_host = os.getenv('DB_HOST')
    db_user = os.getenv('DB_USER')
    db_pass = os.getenv('DB_PASS')
    db_name = os.getenv('DB_NAME')

    required_values = [
        ('DB_HOST', db_host),
        ('DB_USER', db_user),
        ('DB_PASS', db_pass),
        ('DB_NAME', db_name)
    ]

    missing = [name for name, val in required_values if not val]
    if missing:
        print(f"Configuration Error: Missing environment variable(s): {', '.join(missing)}")
        return None

    return db_host, db_user, db_pass, db_name


def connect_to_database(db_config):
    # FR6: connect to the database with validated configuration.
    try:
        conn = mysql.connector.connect(
            host=db_config[0],
            user=db_config[1],
            password=db_config[2],
            database=db_config[3]
        )
        return conn
    except Error as err:
        print(f"Connection Error: {err}")
        return None


def fetch_employees(conn):
    # FR6: retrieve employee rows without ORDER BY so sorting is done in Python.
    query = "SELECT id, name, salary, department, position, hireDate FROM Employees"
    cursor = conn.cursor()
    cursor.execute(query)
    rows = cursor.fetchall()
    cursor.close()

    # FR2: store data in an array (list) of Employee objects.
    employees = []
    for row in rows:
        try:
            employee = Employee(row[0], row[1], row[2], row[3], row[4], row[5])
            employees.append(employee)
        except ValueError as err:
            # FR13: include data context if a row fails object validation.
            print(f"Skipping invalid row ID {row[0]}: {err}")
    return employees


def insertion_sort_by_salary_desc(employee_array):
    # FR3/FR4: insertion sort on array of objects using get_salary().
    for index in range(1, len(employee_array)):
        key_employee = employee_array[index]
        compare_index = index - 1

        while compare_index >= 0 and employee_array[compare_index].get_salary() < key_employee.get_salary():
            employee_array[compare_index + 1] = employee_array[compare_index]
            compare_index -= 1

        employee_array[compare_index + 1] = key_employee


def filter_by_department_and_min_salary(employee_array, department, min_salary):
    # FR12: create a processed subset based on user-entered criteria.
    filtered = []
    for employee in employee_array:
        if (
            employee.get_department().lower() == department.lower()
            and employee.get_salary() >= min_salary
        ):
            filtered.append(employee)
    return filtered


def apply_pay_rise(employee_array, percentage):
    # FR1: demonstrate setter usage by updating each selected object safely.
    multiplier = 1 + (percentage / 100)
    for employee in employee_array:
        new_salary = employee.get_salary() * multiplier
        employee.set_salary(new_salary)


def display_employees(employee_array, heading):
    # FR7: display formatted output for the user.
    print("\n" + heading)
    print(f"{'ID':<6}{'Name':<22}{'Salary':<12}{'Department':<22}{'Position':<22}{'Hire Date':<12}")
    print("-" * 96)

    for employee in employee_array:
        print(
            f"{employee.get_id():<6}"
            f"{employee.get_name():<22}"
            f"{employee.get_salary():<12.2f}"
            f"{employee.get_department():<22}"
            f"{employee.get_position():<22}"
            f"{employee.get_hire_date():<12}"
        )


def run_program_24():
    # FR11: clear status message at start.
    print("--- Program 24: Complete OO Employee Processing ---")

    db_config = validate_environment_config()
    if db_config is None:
        return

    conn = connect_to_database(db_config)
    if conn is None:
        return

    try:
        # FR6/FR2: load employee data from database into object array.
        employees = fetch_employees(conn)

        if not employees:
            print("No employee records were loaded.")
            return

        # FR3/FR4: sort the object array using insertion sort.
        insertion_sort_by_salary_desc(employees)

        # FR7: collect user criteria for processing.
        print("\nFilter employees by department and minimum salary.")
        target_department = get_non_empty_text("Enter Department: ")
        minimum_salary = get_positive_float("Enter Minimum Salary: ")
        rise_percentage = get_percentage("Enter Pay Rise Percentage (0-100): ")

        matches = filter_by_department_and_min_salary(employees, target_department, minimum_salary)

        if not matches:
            print("No employees matched the selected criteria.")
            return

        display_employees(matches, "Matching employees before salary update:")

        # FR1: update objects using setter methods.
        apply_pay_rise(matches, rise_percentage)

        display_employees(matches, "Matching employees after salary update:")

        # FR11: clear completion feedback.
        print(f"\nProcessed {len(matches)} employee object(s) successfully.")

    except Error as err:
        # FR13/FR14: provide context and keep data operations safe.
        print(f"Database Error: {err}")
    except ValueError as err:
        print(f"Validation Error: {err}")
    finally:
        # FR15: always close database connection safely.
        if conn.is_connected():
            conn.close()
            print("Database connection closed safely.")


if __name__ == "__main__":
    run_program_24()
