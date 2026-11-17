import mysql.connector
from mysql.connector import Error

class DatabaseConnection:
    @staticmethod
    def get_connection():
        try:
            return mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                database="db_kos"
            )
        except Error as e:
            print(f"Gagal terhubung ke MySQL: {e}")
            return None