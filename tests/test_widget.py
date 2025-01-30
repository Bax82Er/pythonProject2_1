import pytest
from src.widget import mask_account_card, get_date

@pytest.fixture
def account_infos():
    return [
        "Счет 1111222233334444",
        "Карта 5555666677778888",
    ]

@pytest.mark.parametrize("account_info, expected_result", [
    ("Счет 1111222233334444", "Счет ************4444"),
    ("Карта 5555666677778888", "Карта 5555*******8888"),
])
def test_mask_account_card(account_info, expected_result):
    assert mask_account_card(account_info) == expected_result


@pytest.fixture
def dates():
    return [
        "2023-07-23T22:33:44.000Z",
        "InvalidDateFormat",
    ]

@pytest.mark.parametrize("date_str, expected_result", [
    ("2023-07-23T22:33:44.000Z", "23.07.2023"),
    ("InvalidDateFormat", None),
])
def test_get_date(date_str, expected_result):
    assert get_date(date_str) == expected_result