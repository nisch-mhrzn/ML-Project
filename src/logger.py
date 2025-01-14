import logging
import os
from datetime import datetime

# Define log directory and log file name
LOG_DIR = os.path.join(os.getcwd(), "logs")
LOG_FILE = f"{datetime.now().strftime('%m-%d-%Y_%H-%M-%S')}.log"  # Replace ':' with '_'

# Create the logs directory if it doesn't exist
os.makedirs(LOG_DIR, exist_ok=True)

# Full path to the log file
LOG_FILE_PATH = os.path.join(LOG_DIR, LOG_FILE)

# Configure logging
logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)

if __name__ == "__main__":
    logging.info("Logging Started")
