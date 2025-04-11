import logging
from config import loggingConstants

class CustomFormatter(logging.Formatter):
    """Кастомизация форматов для вывода в консоль"""

    FORMATS = {
        logging.DEBUG: loggingConstants.DEBUG_COLOR + loggingConstants.LOG_FORMAT + loggingConstants.DEFAULT_COLOR,
        logging.INFO: loggingConstants.DEFAULT_COLOR + loggingConstants.LOG_FORMAT + loggingConstants.DEFAULT_COLOR,
        logging.WARNING: loggingConstants.WARNING_COLOR + loggingConstants.LOG_FORMAT + loggingConstants.DEFAULT_COLOR,
        logging.ERROR: loggingConstants.ERROR_COLOR + loggingConstants.LOG_FORMAT + loggingConstants.DEFAULT_COLOR,
    }

    def format(self, record):
        log_fmt = self.FORMATS.get(record.levelno)
        formatter = logging.Formatter(log_fmt)
        return formatter.format(record)