import datetime
from typing import Any


def filter_by_state(operations: list, state: str = 'EXECUTED') -> list:
    """Фильтрует список операций по статусу.

    Аргументы:
    operations (list): Список словарей с операциями.
    state (str): Статус, по которому производится фильтрация. По умолчанию 'EXECUTED'.

    Возвращает:
    list: Отфильтрованный список операций.
    """
    filtered_operations: list['Any'] = []
    for operation in operations:
        if operation['state'] == state:
            filtered_operations.append(operation)
    return filtered_operations


def sort_by_date(operations: list, order: bool = True) -> list:
    """Сортирует список операций по дате.

    Аргументы:
    operations (list): Список словарей с операциями.
    order (bool): Порядок сортировки. True - по возрастанию, False - по убыванию. По умолчанию True.

    Возвращает:
    list: Отсортированный список операций.
    """
    def date_key(operation):
        return datetime.datetime.strptime(operation['date'], "%Y-%m-%dT%H:%M:%S")

    return sorted(operations, key=date_key, reverse=(not order))
