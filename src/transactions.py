import re
from collections import Counter


def filter_transactions_by_description(transactions, search_string):
    """
    Функция для фильтрации списка словарей операций по описанию.

    :param transactions: Список словарей с данными о банковских операциях.
    :param search_string: Строка для поиска в описании операции.
    :return: Список словарей с операциями, у которых в описании есть искомая строка.
    """
    # Используем регулярное выражение для поиска строки
    pattern = re.compile(search_string, flags =re.IGNORECASE)
    return [transaction for transaction in transactions if
            pattern.search(transaction.get('description', ''))]


    def count_operations_by_category(transactions, categories):
        """
        Функция для подсчета количества операций в каждой категории.

        :param transactions: Список словарей с данными о банковских операциях.
        :param categories: Список категорий операций.
        :return: Словарь, где ключами являются категории, а значениями - количество операций в каждой категории.
        """
        counter = Counter()
        for transaction in transactions:
            description = transaction['description']
            for category in categories:
                if category.lower() in description.lower():
                    description.lower()
                counter[category] += 1
                break

    return dict(counter)


def count_operations_by_category() -> object:
    return None