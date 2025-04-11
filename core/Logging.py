import logging
import LoggingFormatter
from pathlib import Path
from datetime import date
from config import loggingConstants
from config import settings

class Logging:
    """Класс для логирования"""

    def __init__(self):
        self.__logger = logging.getLogger()
        self.__addFile()
        self.__addFormat()
    """Конструктор логов"""

    def __addFile(self):
        Path(loggingConstants.LOG_FILE_PATH).mkdir(exist_ok=True)
        fileHandler = logging.FileHandler(loggingConstants.LOG_FILE_PATH + "/log_" + str(date.today()) + ".log")
        formatter = logging.Formatter(loggingConstants.LOG_FORMAT)
        fileHandler.setFormatter(formatter)
        self.__logger.addHandler(fileHandler)
    """Добавление информации в файл логов"""

    def __addFormat(self):
        self.__logger.setLevel(logging.DEBUG)
        streamHandler = logging.StreamHandler()
        streamHandler.setLevel(logging.DEBUG)
        streamHandler.setFormatter(LoggingFormatter.CustomFormatter())
        self.__logger.addHandler(streamHandler)
    """Формат текста для вывода в консоль"""

    def info(self, message):
        self.__logger.setLevel(logging.INFO)
        self.__logger.info(message)
    """Информационный текст"""

    def debug(self, message):
        if settings.DEBUG:
            self.__logger.setLevel(logging.DEBUG)
            self.__logger.debug(message)
    """Debug текст"""

    def warning(self, message):
        self.__logger.setLevel(logging.WARNING)
        self.__logger.warning(message)
    """Предупреждение"""

    def error(self, message):
        self.__logger.setLevel(logging.ERROR)
        self.__logger.error(message)
    """Ошибка"""