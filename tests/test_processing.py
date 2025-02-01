import pytest
from src.processing import filter_by_state, sort_by_date

# Фикстуры для обоих тестов
@pytest.fixture
def operations():
    return [
        {'id': 1, 'state': 'EXECUTED', 'date': '2023-10-01T12:00:00.000'},
        {'id': 2, 'state': 'PENDING', 'date': '2023-10-02T13:00:00.000'},
        {'id': 3, 'state': 'CANCELED', 'date': '2023-10-03T14:00:00.000'},
        {'id': 4, 'state': 'EXECUTED', 'date': '2023-10-04T15:00:00.000'}
    ]

# Тесты для функции filter_by_state
def test_filter_by_state_default(operations):
    result = filter_by_state(operations)
    assert result == [{'id': 1, 'state': 'EXECUTED', 'date': '2023-10-01T12:00:00.000'}, {'id': 4, 'state': 'EXECUTED', 'date': '2023-10-04T15:00:00.000'}]

def test_filter_by_state_pending(operations):
    result = filter_by_state(operations, state='PENDING')
    assert result == [{'id': 2, 'state': 'PENDING', 'date': '2023-10-02T13:00:00.000'}]

def test_filter_by_state_canceled(operations):
    result = filter_by_state(operations, state='CANCELED')
    assert result == [{'id': 3, 'state': 'CANCELED', 'date': '2023-10-03T14:00:00.000'}]

# Тесты для функции sort_by_date
def test_sort_by_date_ascending(operations):
    result = sort_by_date(operations)
    expected_result = [
        {'id': 1, 'state': 'EXECUTED', 'date': '2023-10-01T12:00:00.000'},
        {'id': 2, 'state': 'PENDING', 'date': '2023-10-02T13:00:00.000'},
        {'id': 3, 'state': 'CANCELED', 'date': '2023-10-03T14:00:00.000'},
        {'id': 4, 'state': 'EXECUTED', 'date': '2023-10-04T15:00:00.000'}
    ]
    assert result == expected_result

def test_sort_by_date_descending(operations):
    result = sort_by_date(operations, order=False)
    expected_result = [
        {'id': 4, 'state': 'EXECUTED', 'date': '2023-10-04T15:00:00.000'},
        {'id': 3, 'state': 'CANCELED', 'date': '2023-10-03T14:00:00.000'},
        {'id': 2, 'state': 'PENDING', 'date': '2023-10-02T13:00:00.000'},
        {'id': 1, 'state': 'EXECUTED', 'date': '2023-10-01T12:00:00.000'}
    ]
    assert result == expected_result