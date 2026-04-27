from database import get_db_connection
from mysql.connector import Error

def test_connection():
    print("Checking connection to external database...")
    
    # Attempt to get the connection object from your database.py
    conn = get_db_connection()

    if conn and conn.is_connected():
        try:
            # Create a cursor to execute a simple server command
            cursor = conn.cursor()
            cursor.execute("SELECT VERSION();")
            version = cursor.fetchone()
            
            print("--- Connection Successful! ---")
            print(f"Database Server Version: {version[0]}")
            
        except Error as e:
            print(f"Connected, but query failed: {e}")
        finally:
            # Clean up
            cursor.close()
            conn.close()
            print("Connection closed safely.")
    else:
        print("--- Connection Failed ---")
        print("Check your GitHub Secrets (Host, User, Pass) and Firewall settings.")

if __name__ == "__main__":
    test_connection()