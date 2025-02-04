def filter_by_currency(transactions, currency_code):
    """Фильтрация транзакций по указанной валюте."""
    for transaction in transactions:
        if transaction["operationAmount"]["currency"]["code"] == currency_code:
            yield transaction


def transaction_descriptions(transactions):
    """Генерация описаний транзакций."""
    for transaction in transactions:
        yield transaction.get("description", "")


def card_number_generator(start=1, end=10000):
    """Генерация номеров банковских карт в формате 'XXXX XXXX XXXX XXXX'."""
    for i in range(start, end + 1):
        # Преобразуем число в строку формата '0000 0000 0000 000i'
        card_number = f"{i:016d}"
        # Разделяем каждую четвертую цифру пробелом
        formatted_card_number = " ".join([card_number[i:i+4] for i in range(0, len(card_number), 4)])
        yield formatted_card_number