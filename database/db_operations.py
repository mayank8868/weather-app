from database.db_config import connect_db

def insert_weather_data(location, temperature, humidity, conditions):
    """Insert weather data into the database."""
    db = connect_db()
    cursor = db.cursor()
    sql = "INSERT INTO weather_data (location, temperature, humidity, conditions) VALUES (%s, %s, %s, %s)"
    cursor.execute(sql, (location, temperature, humidity, conditions))
    db.commit()
    db.close()

def get_weather_data():
    """Retrieve all weather data."""
    db = connect_db()
    cursor = db.cursor(dictionary=True)
    cursor.execute("SELECT * FROM weather_data")
    data = cursor.fetchall()
    db.close()
    return data

