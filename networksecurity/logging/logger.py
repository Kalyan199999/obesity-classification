import logging
from datetime import datetime
import os

# Directory for logs
LOG_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "logs")

os.makedirs(LOG_DIR, exist_ok=True)  # create directory if it doesn't exist

# File name with safe datetime format (replace colon ':' with dash '-')
LOG_FILE_FORMAT = datetime.now().strftime('%Y-%m-%d_%H-%M-%S') + ".log"

# Full log file path
LOG_FILE_PATH = os.path.join(LOG_DIR, LOG_FILE_FORMAT)

# Configure logger
logging.basicConfig(
    filename=LOG_FILE_PATH,
    format='[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s',
    filemode='w',
    level=logging.INFO
)
