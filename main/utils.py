import json
import logging


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


def filter_transactions_by_status(transactions, status):
    # Приводим статус к нижнему регистру для унифицированного сравнения
    normalized_status = status.strip().lower()

    # Выводим данные перед фильтрацией
    #print("Исходные данные перед фильтрацией:", transactions)

    # Фильтруем операции, приводя статус к нижнему регистру и удаляя пробелы
    filtered_transactions = [transaction for transaction in transactions
                             if transaction.get('state', '').strip().lower() == normalized_status]

    # Выводим данные после фильтрации


    return filtered_transactions


from datetime import datetime

def sort_transactions_by_date(transactions, order="ascending"):
    """
    Сортирует операции по дате.

    :param transactions: Список словарей с данными о банковских операциях.
    :param order: Порядок сортировки ("ascending" или "descending").
    :return: Отсортированный список операций.
    """
    # Преобразовываем даты в формате строки в объекты datetime
    for transaction in transactions:
        date_str = transaction.get('date')
        try:
            transaction['date_obj'] = datetime.strptime(date_str, "%d.%m.%Y").date()
        except ValueError:
            continue  # Пропускаем запись, если дата имеет неправильный формат

    # Сортируем операции по дате
    if order == "ascending":
        return sorted(transactions, key=lambda x: x.get('date_obj'))
    elif order == "descending":
        return sorted(transactions, key=lambda x: x.get('date_obj'), reverse=True)
    else:
        raise ValueError("Неправильный порядок сортировки. Допустимые значения: 'ascending', 'descending'.")


def filter_rub_transactions(transactions):
    """
    Фильтрует операции, оставляя только рублевые транзакции.

    :param transactions: Список словарей с данными о банковских операциях.
    :return: Список операций, суммы которых указаны в рублях.
    """
    return [transaction for transaction in transactions
            if transaction['operationAmount']['currency']['name'].startswith('руб')]

def filter_transactions_by_description(transactions, search_string):
    """
    Фильтрует операции по описанию.

    :param transactions: Список словарей с данными о банковских операциях.
    :param search_string: Строка для поиска в описании операции.
    :return: Список операций, у которых в описании есть искомая строка.
    """
    return [transaction for transaction in transactions if search_string.lower() in transaction.get('description', '').lower()]


from collections import Counter

def count_operations_by_category(transactions, categories):
    """
    Подсчитывает количество операций по категориям.

    :param transactions: Список словарей с данными о банковских операциях.
    :param categories: Список категорий операций.
    :return: Словарь, где ключи — это названия категорий, а значения — количество операций в каждой категории.
    """
    counter = Counter()
    for transaction in transactions:
        description = transaction.get('description', '')
        for category in categories:
            if category.lower() in description.lower():
                counter[category] += 1
                break
    return dict(counter)


