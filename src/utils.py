import json
import logging

# Получение логгера
logger = logging.getLogger(__name__)


def read_json_file(file_path: str) -> list:
    """
    Читает JSON-файл и возвращает список словарей с данными о финансовых транзакциях.

    :param file_path: Путь к JSON-файлу.
    :return: Список словарей с данными о транзакциях. Если файл пустой, содержит не список или не найден, возвращается пустой список.
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)

        if isinstance(data, list):
            logger.info(f"Успешно прочитан JSON-файл: {file_path}.")
            return data
        else:
            logger.warning("JSON файл не является списком.")
            return []
    except FileNotFoundError:
        logger.error(f"Файл не найден: {file_path}.")
        return []
    except json.JSONDecodeError:
        logger.exception(f"Ошибка декодирования JSON в файле: {file_path}.")
        return []

