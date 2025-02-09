import os
from dotenv import load_dotenv
import requests

load_dotenv()  # Загружаем переменные окружения из .env

API_KEY = os.getenv('API_KEY')
BASE_URL = 'http://api.exchangeratesapi.io/v1/latest'


def convert_to_rub(transaction):
    """
    Конвертирует сумму транзакции в рубли.

    :param transaction: Словарь с данными о транзакции.
    :return: Сумма транзакции в рублях (тип float).
    """
    amount = transaction['amount']
    currency = transaction.get('currency', 'RUB').upper()

    if currency == 'RUB':
        return float(amount)

    response = requests.get(
        BASE_URL,
        params={'access_key': API_KEY}
    )

    if response.status_code != 200:
        raise Exception(f'Не удалось получить курс валют: {response.text}')

    rates = response.json()['rates']
    rate = rates[currency]

    return round(float(amount) * rate, 2)