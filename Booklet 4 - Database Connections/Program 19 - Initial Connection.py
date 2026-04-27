import mysql.connector
import sys

# Define the Class structure to mirror SQA-RL
class Employee:
    def __init__(self, id, name, salary, department, position, hireDate):
        self.id = int(id)
        self.name = str(name)
        self.salary = float(salary)
        self.department = str(department)
        self.position = str(position)
        self.hireDate = str(hireDate)

# 1. Connection Details with Port
config = {
    'host': 'b07invi6fy0sdm4vfxaw-mysql.services.clever-cloud.com',
    'user': 'ugckxuxbrxdott5j',
    'password': 'rPKPsrlvZweFCu2ftdv0',
    'database': 'b07invi6fy0sdm4vfxaw'
}

# 2, 3 & 4. Establish Connection and Error Check
try:
    connection = mysql.connector.connect(**config)
except mysql.connector.Error as err:
    print(f"Connection Failed: {err}")
    sys.exit()

try:
    # 5. Query
    query = "SELECT * FROM Employees "
    cursor = connection.cursor()
    
    # 6 & 7. Execute and Map to Array of Class Objects
    cursor.execute(query)
    db_rows = cursor.fetchall()
    
    results = []
    for row in db_rows:
        # Create instance of Employee class
        results.append(Employee(row[0], row[1], row[2], row[3], row[4], row[5]))

    # 8. Display Headings
    print(f"{'id':<5}{'name':<20}{'salary':<12}{'dept':<30}{'position':<30}{'date':<12}")

    # 9. Loop through the results array
    for worker in results:
          print(f"{str(worker.id):<5}{str(worker.name):<20}{str(worker.salary):<12}"
              f"{str(worker.department):<30}{str(worker.position):<30}{str(worker.hireDate):<12}")

finally:
    # 10. Close Connection
    if connection.is_connected():
        cursor.close()
        connection.close()