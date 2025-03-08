import logging

logging.basicConfig(
    filename="weather_app.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def log_info(message):
    """Log an info message."""
    logging.info(message)

def log_error(message):
    """Log an error message."""
    logging.error(message)
