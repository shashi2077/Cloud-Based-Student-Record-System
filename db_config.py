import os
import mysql.connector
from dotenv import load_dotenv

load_dotenv()

def get_connection():
    """Create and return a MySQL connection using environment variables."""
    return mysql.connector.connect(
        host=os.getenv("DB_HOST", "localhost"),
        user=os.getenv("DB_USER", "root"),
        password=os.getenv("DB_PASSWORD", ""),
        database=os.getenv("DB_NAME", "student_db"),
        port=int(os.getenv("DB_PORT", "3306")),
    )
