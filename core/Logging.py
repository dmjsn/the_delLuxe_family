import logging
from pathlib import Path
from datetime import date
from config import loggingConstants
from config import settings
from core.LoggingFormatter import CustomFormatter

class Logging:
    """Класс для логирования"""

    def __init__(self):
        """Конструктор логов"""
        self.__logger = logging.getLogger()
        self.__addFile()
        self.__addFormat()

    def __addFile(self):
        """Добавление информации в файл логов"""
        Path(loggingConstants.LOG_FILE_PATH).mkdir(exist_ok=True)
        fileHandler = logging.FileHandler(loggingConstants.LOG_FILE_PATH + "/log_" + str(date.today()) + ".log")
        formatter = logging.Formatter(loggingConstants.LOG_FORMAT)
        fileHandler.setFormatter(formatter)
        self.__logger.addHandler(fileHandler)


    def __addFormat(self):
        """Формат текста для вывода в консоль"""
        streamHandler = logging.StreamHandler()
        streamHandler.setFormatter(CustomFormatter())
        self.__logger.addHandler(streamHandler)

    def info(self, message):
        """Информационный текст"""
        self.__logger.setLevel(logging.INFO)
        self.__logger.info(message)

    def debug(self, message):
        """Debug текст"""
        if settings.DEBUG:
            self.__logger.setLevel(logging.DEBUG)
            self.__logger.debug(message)

    def warning(self, message):
        """Предупреждение"""
        self.__logger.setLevel(logging.WARNING)
        self.__logger.warning(message)

    def error(self, message):
        """Ошибка"""
        self.__logger.setLevel(logging.ERROR)
        self.__logger.error(message)