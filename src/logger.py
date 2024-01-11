import logging
import os
from datetime import datetime

# Log file name
log_file_name = f"{datetime.now().strftime('%m-%d-%Y_%H-%M-%S')}.log"

# Path to logs directory
logs_dir = os.path.join(os.getcwd(), "logs")

# Create logs directory if it doesn't exist
os.makedirs(logs_dir, exist_ok=True)

# Full log file path
log_file_path = os.path.join(logs_dir, log_file_name)

# Basic logging configuration
logging.basicConfig(
    filename=log_file_path,
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)