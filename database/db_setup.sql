CREATE DATABASE IF NOT EXISTS weather_db;

USE weather_db;

CREATE TABLE if not EXISTS weather_data (
    id INT AUTO_INCREMENT PRIMARY KEY,
    location VARCHAR(255),
    temperature FLOAT,
    humidity INT,
    conditions VARCHAR(255),
    date_times DATETIME DEFAULT CURRENT_TIMESTAMP
);

