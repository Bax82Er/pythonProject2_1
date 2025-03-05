import os
import json
import csv
import openpyxl


# Импортируем вспомогательные функции
from utils import (
    filter_transactions_by_status,
    sort_transactions_by_date,
    filter_rub_transactions,
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


def main():
    print("Привет! Добро пожаловать в программу работы с банковскими транзакциями.")
    print("Выберите необходимый пункт меню:")
    print("1. Получить информацию о транзакциях из JSON-файла")
    print("2. Получить информацию о транзакциях из CSV-файла")
    print("3. Получить информацию о транзакциях из XLSX-файла")

    choice = int(input("Ваш выбор: "))

    if choice == 1:
        file_path = "main/data/transactions.json"
        print(f"Для обработки выбран JSON-файл: {file_path}")
    elif choice == 2:
        file_path = "main/data/transactions.csv"
        print(f"Для обработки выбран CSV-файл: {file_path}")
    elif choice == 3:
        file_path = "main/data/transactions.xlsx"
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
    answer = input("Отсортировать операции по дате? Да/Нет: ").lower()
    if answer == "да":
        order = input("Отсортировать по возрастанию или по убыванию? ").lower()
        if order == "возрастание":
            filtered_transactions = sort_transactions_by_date(filtered_transactions, True)
        elif order == "убывание":
            filtered_transactions = sort_transactions_by_date(filtered_transactions, False)
        else:
            print("Неверный выбор. Пожалуйста, введите 'возрастание' или 'убывание'.")

    answer = input("Выводить только рублевые транзакции? Да/Нет: ").lower()
    if answer == "да":
        filtered_transactions = filter_rub_transactions(filtered_transactions)

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
        print(f"\nВсего банковских операций в выборке: {len(filtered_transactions)}.")
    else:
        print("Не найдено ни одной транзакции, подходящей под ваши условия фильтрации.")


if __name__ == "__main__":
    main()