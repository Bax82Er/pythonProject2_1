import datetime
from typing import Any
from typing import List, Dict

def filter_by_state(transactions: List[Dict[str, Any]], status: str = 'EXECUTED') -> List[Dict[str, Any]]:


#def filter_by_state(transactions: list, status: str = 'EXECUTED') -> list:
    """Фильтрует список операций по статусу.

    Аргументы:
    operations (list): Список словарей с операциями.
    state (str): Статус, по которому производится фильтрация. По умолчанию 'EXECUTED'.

    Возвращает:
    list: Отфильтрованный список операций.
    """
    return [transaction for transaction in transactions if transaction['status'] == status]


def sort_by_date(operations: list, order: bool = True) -> list:
    """Сортирует список операций по дате.

    Аргументы:
    operations (list): Список словарей с операциями.
    order (bool): Порядок сортировки. True - по возрастанию, False - по убыванию. По умолчанию True.

    Возвращает:
    list: Отсортированный список операций.
    """
    def date_key(operation):
        return datetime.datetime.strptime(operation['date'], "%Y-%m-%dT%H:%M:%S.%f")

    return sorted(operations, key=date_key, reverse=order)
