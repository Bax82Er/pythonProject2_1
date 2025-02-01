import pytest
import src.processing

@pytest.fixture
def operations_with_states():
    return [
        {"id": 1, "date": "2023-01-15T12:34:56.000", "state": "PENDING"},
        {"id": 2, "date": "2023-02-20T09:30:00.000", "state": "EXECUTED"},
        {"id": 3, "date": "2023-03-05T18:40:25.500", "state": "CANCELED"},
        {"id": 4, "date": "2023-04-10T06:50:35.250", "state": "EXECUTED"}
    ]

def test_filter_by_state_default(operations_with_states):
    result = src.processing.filter_by_state(operations_with_states)
    assert len(result) == 2
    assert all(op["state"] == "EXECUTED" for op in result)

def test_filter_by_state_pending(operations_with_states):
    result = src.processing.filter_by_state(operations_with_states, state="PENDING")
    assert len(result) == 1
    assert all(op["state"] == "PENDING" for op in result)

def test_filter_by_state_canceled(operations_with_states):
    result = src.processing.filter_by_state(operations_with_states, state="CANCELED")
    assert len(result) == 1
    assert all(op["state"] == "CANCELED" for op in result)
