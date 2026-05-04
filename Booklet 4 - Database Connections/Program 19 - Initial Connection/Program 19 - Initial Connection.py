import os
from pathlib import Path

import mysql.connector
from dotenv import load_dotenv
from mysql.connector import Error

# Load the .env file from the workspace root (three levels up from this script)
base_path = Path(__file__).resolve().parent.parent.parent
env_path = base_path / '.env'
load_dotenv(dotenv_path=env_path)

def test_connection():
    # FR11: provide clear status feedback at program start.
    print("Checking connection to external database...")

    # FR8: validate required environment configuration values.
    db_host = os.getenv('DB_HOST')
    db_user = os.getenv('DB_USER')
    db_pass = os.getenv('DB_PASS')
    db_name = os.getenv('DB_NAME')

    missing = [name for name, val in [('DB_HOST', db_host), ('DB_USER', db_user),
                                       ('DB_PASS', db_pass), ('DB_NAME', db_name)] if not val]
    if missing:
        # FR11: return clear failure feedback if config is invalid.
        print(f"Configuration Error: Missing environment variable(s): {', '.join(missing)}")
        return

    cursor = None

    try:
        # FR6: connect to the database and execute a query.
        conn = mysql.connector.connect(
            host=db_host,
            user=db_user,
            password=db_pass,
            database=db_name
        )
    except Error as e:
        # FR11: report connection errors clearly.
        print(f"Connection Error: {e}")
        conn = None

    if conn and conn.is_connected():
        try:
            # FR6: use SQL query to validate connectivity.
            cursor = conn.cursor()
            cursor.execute("SELECT VERSION();")
            version = cursor.fetchone()
            
            # FR11: success feedback with query output.
            print("--- Connection Successful! ---")
            print(f"Database Server Version: {version[0]}")
            
        except Error as e:
            # FR14: include meaningful error context from failed query.
            print(f"Connected, but query failed: {e}")
        finally:
            # FR11: always clean up open database resources.
            if cursor is not None:
                cursor.close()
            conn.close()
            print("Connection closed safely.")
    else:
        # FR11: failure feedback and troubleshooting guidance.
        print("--- Connection Failed ---")
        print("Check your GitHub Secrets (Host, User, Pass) and Firewall settings.")

if __name__ == "__main__":
    test_connection()