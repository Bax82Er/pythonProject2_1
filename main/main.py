import os
import json
import csv
import openpyxl
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
# Импортируем вспомогательные функции
from src.generators import filter_by_currency
from src.processing import sort_by_date
from src.transactions import (
    filter_transactions_by_status,
    filter_transactions_by_description,
)



def load_data_from_file(file_path):
    """
    Загружает данные о транзакциях из указанного файла.
    :param file_path: Путь к файлу с данными.
    :return: Список словарей с данными о транзакциях.
    """
    _, ext = os.path.splitext(file_path)
    if ext == ".json":

        with open(file_path, 'r') as f:
            return json.load(f)
    elif ext == ".csv":
        transactions = []
        with open(file_path, newline='') as f:
            reader = csv.DictReader(f)
            for row in reader:
                transactions.append(row)
        return transactions
    elif ext == ".xlsx":
        transactions = []
        wb = openpyxl.load_workbook(file_path)
        ws = wb.active
        for row in ws.iter_rows(values_only=True):
            transactions.append(dict(zip(ws[1], row)))
        return transactions
    else:
        raise ValueError(f"Не поддерживаемый формат файла: {file_path}")
    transactions = load_data_from_file(file_path)
    print(f"Загружено транзакций: {len(transactions)}")


def main():
    print("Привет! Добро пожаловать в программу работы с банковскими транзакциями.")
    print("Выберите необходимый пункт меню:")
    print("1. Получить информацию о транзакциях из JSON-файла")
    print("2. Получить информацию о транзакциях из CSV-файла")
    print("3. Получить информацию о транзакциях из XLSX-файла")

    choice = int(input("Ваш выбор: "))
    if choice == 1:
        file_path = "./data/transactions.json"
        print(f"Для обработки выбран JSON-файл: ")
    elif choice == 2:
        file_path = "./data/transactions.csv"
        print(f"Для обработки выбран CSV-файл: {file_path}")
    elif choice == 3:
        file_path = "./data/transactions.xlsx"
        print(f"Для обработки выбран XLSX-файл: {file_path}")
    else:
        print("Ошибка ввода. Выберите правильный номер пункта меню.")
        return
    # Загрузка данных
    transactions = load_data_from_file(file_path)

    # Выбор статуса операции
    statuses = ["EXECUTED", "CANCELED", "PENDING"]
    while True:
        status = input("Введите статус, по которому необходимо выполнить фильтрацию:\n").upper()
        if status in statuses:
            break
        else:
            print(f"Недоступный статус. Доступные статусы: {', '.join(statuses)}")

    # Фильтрация по статусу
    filtered_transactions = filter_transactions_by_status(transactions, status)
    print(f"Операции отфильтрованы по статусу: {status}")

    # Вопросы для уточнения выборки
    answer = input("Отсортировать операции по дате? Да/Нет: ").lower().strip()
    if answer == 'да':
        order = input("Отсортировать по возрастанию или по убыванию? ").lower().strip()
        filtered_transactions = sort_by_date(filtered_transactions, order == "возрастание")
    else:
        pass  # Ничего не делаем, если сортировка не нужна

    answer = input("Выводить только рублевые транзакции? Да/Нет: ").lower()
    if answer == "да":
        filtered_transactions = filter_by_currency(filtered_transactions, 'RUB')

    answer = input("Отфильтровать список транзакций по определенному слову в описании? Да/Нет: ").lower()
    if answer == "да":
        search_term = input("Введите слово для фильтрации: ")
        filtered_transactions = filter_transactions_by_description(filtered_transactions, search_term)

    # Печать итогового списка транзакций
    if filtered_transactions:
        print("\nРаспечатываем итоговый список транзакций...")
        for idx, transaction in enumerate(filtered_transactions, start=1):
            print(f"{idx}. {transaction['date']} {transaction['description']}")
            print(f"Счет: {transaction['account']}")
            print(f"Сумма: {transaction['amount']}\n")
        filtered_transactions_list = list(filtered_transactions)
        print(f"\nВсего банковских операций в выборке: {len(filtered_transactions_list)}.")
    else:
        print("Не найдено ни одной транзакции, подходящей под ваши условия фильтрации.")


if __name__ == "__main__":
    main()
