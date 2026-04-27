from database import get_db_connection
from mysql.connector import Error
from datetime import date

def insert_employee():
    conn = get_db_connection()
    if conn is None:
        return

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
            cursor.close()
            conn.close()

if __name__ == "__main__":
    insert_employee()