import re
from collections import defaultdict

def filter_transactions_by_status(transactions, status_search):
    """
    Функция для фильтрации списка словарей операций по статусу.

    :param transactions: Список словарей с данными о банковских операциях.
    :param status_search: Строка для поиска статуса операции.
    :return: Список словарей с операциями, у которых статус совпадает с указанной строкой.

    """
    # Создаем регулярное выражение для поиска статуса, игнорируя регистр
    pattern = re.compile(status_search, re.IGNORECASE)

    # Фильтруем операции по совпадению статуса
    return [transaction
        for transaction in transactions
        if transaction.get('status') is not None and pattern.search(transaction['status'])]


def count_operations_by_categories(transactions, categories):
    """
    Функция для подсчёта количества операций в каждой категории.

    :param transactions: Список словарей с данными о банковских операциях.
    :param categories: Список категорий операций.
    :return: Словарь, где ключи — это названия категорий, а значения — это количество операций в каждой категории.
    """
    # Создаем словарь для хранения результата, начальные значения равны нулю
    result = defaultdict(int)

    # Проходим по каждому словарю в списке операций
    for transaction in transactions:
        description = transaction.get('description', '')

        # Проверяем, содержится ли хотя бы одна категория в описании операции
        for category in categories:
            if category.lower() in description.lower():  # Игнорируем регистр
                result[category] += 1
                break  # Как только нашли категорию, переходим к следующей операции

    return dict(result)  # Преобразуем defaultdict в обычный словарь


def filter_transactions_by_description():
    return None