Weather App

Overview

This Weather App is developed as part of the AI Engineer Intern technical assessment. It fetches real-time weather data from APIs, supports multiple location input types, and provides a 5-day forecast. The app also stores user queries in a database with CRUD functionality and additional features like API integrations and data export options.

Features

Real-Time Weather Data: Fetches weather details using APIs.

Multiple Location Inputs: Supports city names, coordinates, and ZIP codes.

5-Day Forecast: Displays extended weather predictions.

Database Storage: Stores user queries with CRUD functionality.

API Integrations: Google Maps, YouTube (if implemented).

Data Export: Supports JSON, XML, CSV, PDF, and Markdown formats.

Technologies Used

Backend: Flask

Frontend: HTML, CSS, JavaScript

Database: MySQL (or another chosen database)

APIs: OpenWeather API (or any other chosen provider)

Additional Tools: Pandas, Matplotlib (if used for analytics/visualization)

Installation


Create a virtual environment and activate it:

python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`

Install dependencies:

pip install -r requirements.txt

Set up API keys (OpenWeather API, Google Maps, etc.) in a .env file:

Run the application:

python app.py

Access the app in your browser at http://127.0.0.1:5000/.

Usage

Enter a location to fetch real-time weather data.

View current conditions and a 5-day forecast.

Export weather data in different formats.

Future Enhancements

Implement AI-based weather predictions.

Add user authentication for personalized experiences.

Enhance UI with interactive charts.

Contributing

Feel free to submit issues or pull requests to improve the project.


Author
MAYANK YADAV