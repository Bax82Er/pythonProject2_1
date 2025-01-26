def filter_by_state(transactions: list, state='EXECUTED') -> list:
    """
    Фильтрует список транзакций по состоянию.

    :transactions: Список словарей с транзакциями.
    :state: Состояние транзакции для фильтрации (по умолчанию 'EXECUTED').
    :return: Новый список словарей, соответствующих переданному состоянию.
    """
    return [transaction for transaction in transactions if transaction['state'] == state]


from datetime import datetime


def sort_by_date(transactions: list, descending=True) -> list:
    """
    Сортирует список транзакций по дате.

    :transactions: Список словарей с транзакциями.
    :descending: Порядок сортировки (по умолчанию True - по убыванию).
    :return: Отсортированный список словарей.
    """

    def get_date(transaction):
        return datetime.strptime(transaction['date'], '%Y-%m-%dT%H:%M:%S.%f')

    sorted_transactions = sorted(transactions, key=get_date, reverse=descending)
    return sorted_transactions

