from typing import List, Any


def filter_by_state(data, state='EXECUTED'):
    """Возвращает список словарей, соответствующих состоянию."""
    return [item for item in data if item['state'] == state]


def sort_by_date(data, order='descending'):
    """Сортирует список словарей по дате."""
    sorted_data: list[Any] = sorted(data, key=lambda x: x['date'], reverse=order == 'descending')
    return sorted_data
