import os
from pathlib import Path

import mysql.connector
from dotenv import load_dotenv
from mysql.connector import Error

# Load the same .env file used by database.py
base_path = Path(__file__).resolve().parent.parent
env_path = base_path / '.env'
load_dotenv(dotenv_path=env_path)

def test_connection():
    print("Checking connection to external database...")

    cursor = None

    try:
        conn = mysql.connector.connect(
            host=os.getenv('DB_HOST'),
            user=os.getenv('DB_USER'),
            password=os.getenv('DB_PASS'),
            database=os.getenv('DB_NAME')
        )
    except Error as e:
        print(f"Connection Error: {e}")
        conn = None

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
            if cursor is not None:
                cursor.close()
            conn.close()
            print("Connection closed safely.")
    else:
        print("--- Connection Failed ---")
        print("Check your GitHub Secrets (Host, User, Pass) and Firewall settings.")

if __name__ == "__main__":
    test_connection()