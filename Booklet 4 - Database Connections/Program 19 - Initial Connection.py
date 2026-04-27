import mysql.connector
import sys

# Define the Class structure to mirror SQA-RL
class Employee:
    def __init__(self, id, name, salary, department, position, hireDate):
        self.id = id
        self.name = name
        self.salary = salary
        self.department = department
        self.position = position
        self.hireDate = hireDate

# 1. Connection Details with Port
config = {
    'host': '213.171.200.29',
    'user': 'EAAHCSTeacher',
    'password': 'EAAHCSt00!',
    'database': 'EAAHCS'
}

# 2, 3 & 4. Establish Connection and Error Check
try:
    connection = mysql.connector.connect(**config)
except mysql.connector.Error as err:
    print(f"Connection Failed: {err}")
    sys.exit()

try:
    # 5. Query
    query = "SELECT id, name, salary, department, position, hireDate FROM Temployees"
    cursor = connection.cursor()
    
    # 6 & 7. Execute and Map to Array of Class Objects
    cursor.execute(query)
    db_rows = cursor.fetchall()
    
    results = []
    for row in db_rows:
        # Create instance of Employee class
        results.append(Employee(row[0], row[1], row[2], row[3], row[4], row[5]))

    # 8. Display Headings
    print("id\tname\tsalary\tdept\tpos\tdate")

    # 9. Loop through the results array
    for worker in results:
        print(f"{worker.id}\t{worker.name}\t{worker.salary}\t"
              f"{worker.department}\t{worker.position}\t{worker.hireDate}")

finally:
    # 10. Close Connection
    if connection.is_connected():
        cursor.close()
        connection.close()