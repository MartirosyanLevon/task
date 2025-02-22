import logging

# ✅ Define log file name
LOG_FILENAME = "locust.log"

# ✅ Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler(LOG_FILENAME),  # ✅ Logs to file
        logging.StreamHandler()  # ✅ Logs to console
    ]
)

# ✅ Get the logger instance
logger = logging.getLogger(__name__)
