import os
from pathlib import Path
from mysql.connector import Error
import mysql.connector
from dotenv import load_dotenv

# This finds the root folder regardless of where you run the script from
base_path = Path(__file__).resolve().parent.parent
env_path = base_path / '.env'
load_dotenv(dotenv_path=env_path)

def get_db_connection():
    try:
        connection = mysql.connector.connect(
            host=os.getenv('DB_HOST'),
            user=os.getenv('DB_USER'),
            password=os.getenv('DB_PASS'),
            database=os.getenv('DB_NAME')
        )
        return connection
    except Error as e:
        print(f"Connection Error: {e}")
        return None