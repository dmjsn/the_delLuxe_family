class LoggingConstants:
    """Константы для логов"""

    LOG_FILE_PATH: str = "logs"
    """Путь к файлам логов"""

    LOG_FORMAT = "%(asctime)s | %(levelname)s | %(message)s"
    """Формат логов"""

    ERROR_COLOR = "\x1b[31m"
    """Цвет ошибки"""

    WARNING_COLOR = "\x1b[33m"
    """Цвет предупреждения"""

    DEBUG_COLOR = "\x1b[36m"
    """Цвет debug информации"""

    DEFAULT_COLOR = "\x1b[37m"
    """Цвет по умолчанию"""
