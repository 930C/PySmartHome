import logging
from logging.handlers import RotatingFileHandler
import sys

from smart_home.logging.custom_log_record import CustomLogRecord


# Factory Pattern: The LoggerFactory creates a logger with a console and a file handler.
class LoggerFactory:
    @staticmethod
    def setup_logger(name):
        logger = logging.getLogger(name)
        logger.setLevel(logging.DEBUG)

        # Create a formatter using the custom log record
        logging.setLogRecordFactory(CustomLogRecord)
        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(module)s - %(name)s - %(message)s')

        # Create a console handler and set the level to DEBUG
        console_handler = logging.StreamHandler(sys.stdout)
        console_handler.setLevel(logging.DEBUG)
        console_handler.setFormatter(formatter)

        # Create a file handler and set the level to DEBUG
        file_handler = RotatingFileHandler('logs.log', maxBytes=10 * 1024 * 1024, backupCount=5)
        file_handler.setLevel(logging.DEBUG)
        file_handler.setFormatter(formatter)

        # Add the handlers to the logger
        logger.addHandler(console_handler)
        logger.addHandler(file_handler)

        return logger

