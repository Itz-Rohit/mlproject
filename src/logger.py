import logging
import os
from datetime import datetime

# Configure the logger

LOG_FILE = f"{datetime.now().strftime('%m_%d_%y_%H_%M_%S')}.log"  # Removed extra space
LOG_DIR = os.path.join(os.getcwd(), "logs")
os.makedirs(LOG_DIR, exist_ok=True)  # Create logs directory if not exists

LOG_FILE_PATH = os.path.join(LOG_DIR, LOG_FILE)  # Correct file path

logging.basicConfig(
    filename=LOG_FILE_PATH,
    format='[%(asctime)s] %(lineno)d %(levelname)s - %(message)s',
    level=logging.INFO,
    datefmt='%Y-%m-%d %H:%M:%S'
)

if __name__ == "__main__":
    logging.info("Logging has started.")
