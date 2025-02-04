import pytest
from src.generators import filter_by_currency, transaction_descriptions, card_number_generator

# Пример данных для тестирования
transactions = (
    [
        {
            "id": 939719570,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
            "operationAmount": {
                "amount": "9824.07",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод организации",
            "from": "Счет 75106830613657916952",
            "to": "Счет 11776614605963066702"
        },
        {
            "id": 142264268,
            "state": "EXECUTED",
            "date": "2019-04-04T23:20:05.206878",
            "operationAmount": {
                "amount": "79114.93",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод со счета на счет",
            "from": "Счет 19708645243227258542",
            "to": "Счет 75651667383060284188"
        },
        {
            "id": 873106923,
            "state": "EXECUTED",
            "date": "2019-03-23T01:09:46.296404",
            "operationAmount": {
                "amount": "43318.34",
                "currency": {
                    "name": "руб.",
                    "code": "RUB"
                }
            },
            "description": "Перевод со счета на счет",
            "from": "Счет 44812258784861134719",
            "to": "Счет 74489636417521191160"
        },
        {
            "id": 895315941,
            "state": "EXECUTED",
            "date": "2018-08-19T04:27:37.904916",
            "operationAmount": {
                "amount": "56883.54",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод с карты на карту",
            "from": "Visa Classic 6831982476737658",
            "to": "Visa Platinum 8990922113665229"
        },
        {
            "id": 594226727,
            "state": "CANCELED",
            "date": "2018-09-12T21:27:25.241689",
            "operationAmount": {
                "amount": "67314.70",
                "currency": {
                    "name": "руб.",
                    "code": "RUB"
                }
            },
            "description": "Перевод организации",
            "from": "Visa Platinum 1246377376343588",
            "to": "Счет 14211924144426031657"
        }
    ]
)

@pytest.fixture
def usd_transactions():
    return list(filter_by_currency(transactions, "USD"))

@pytest.fixture
def rub_transactions():
    return list(filter_by_currency(transactions, "RUB"))

@pytest.mark.parametrize(
    "currency_code, expected_count",
    [
        ("USD", 3),
        ("RUB", 2),
        ("EUR", 0),
    ],
)
def test_filter_by_currency(currency_code, expected_count):
    filtered_transactions = list(filter_by_currency(transactions, currency_code))
    assert len(filtered_transactions) == expected_count

def test_transaction_descriptions():
    descriptions = list(transaction_descriptions(transactions))
    assert descriptions == ["Перевод организации", "Перевод со счета на счет", "Перевод со счета на счет", "Перевод с карты на карту", "Перевод организации"]

@pytest.mark.parametrize(
    "start, end, expected_cards",
    [
        (1, 10, ['0000 0000 0000 0001', '0000 0000 0000 0002', '0000 0000 0000 0003', '0000 0000 0000 0004', '0000 0000 0000 0005',
                 '0000 0000 0000 0006', '0000 0000 0000 0007', '0000 0000 0000 0008', '0000 0000 0000 0009', '0000 0000 0000 0010']),
        (50, 55, ['0000 0000 0000 0050', '0000 0000 0000 0051', '0000 0000 0000 0052', '0000 0000 0000 0053', '0000 0000 0000 0054', '0000 0000 0000 0055'])
    ],
)
def test_card_number_generator(start, end, expected_cards):
    generated_cards = list(card_number_generator(start, end))
    assert generated_cards == expected_cards
