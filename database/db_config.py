import mysql.connector

def connect_db():
    """Establish a database connection."""
    return mysql.connector.connect(
        host="localhost",
        user="root1",
        password="1234",
        database="weather_db"
    )
