from typing import Union
import logging
from logging.handlers import RotatingFileHandler
from datetime import datetime


# Функция для создания логеров
def setup_logger(name: str, log_file: str, level: int = logging.DEBUG) -> logging.Logger:
    # Создание логгера
    logger = logging.getLogger(name)
    logger.setLevel(level)

    # Форматирование сообщений
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    # Создание FileHandler для записи в файл
    file_handler = RotatingFileHandler(log_file, mode='w', maxBytes=1024 * 1000, backupCount=10)
    file_handler.setFormatter(formatter)

    # Добавляем Handler к логеру
    logger.addHandler(file_handler)

    return logger


# Создание логгеров для модулей
logger_utils: logging.Logger = setup_logger('utils', 'logs/utils.log')
logger_masks: logging.Logger = setup_logger('masks', 'logs/masks.log')

# Примеры использования логгеров
logger_utils.debug("This is a debug message from the utils module.")
logger_masks.info("This is an info message from the masks module.")
logger_utils.error("An error occurred in the utils module.")
logger_masks.critical("A critical error occurred in the masks module.")
