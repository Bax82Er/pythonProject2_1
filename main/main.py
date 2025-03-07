import os
import json
import csv
import openpyxl
import pathlib

import pandas as pd

# Импортируем вспомогательные функции
from utils import(
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
            reader = csv.DictReader(f, delimiter=';')
            for row in reader:
                transactions.append(row)
        return transactions
    elif ext == ".xlsx":
        transactions = pd.read_excel(file_path).to_dict(orient='records')

        return transactions
    else:
        raise ValueError(f"Не поддерживаемый формат файла: {file_path}")


# Основная программа для тестирования функции


def get_file_path(choice):
    """Возвращает путь к файлу в зависимости от выбранного варианта."""
    if choice == 1:
        return pathlib.Path("main/data/transactions.json")
    elif choice == 2:
        return pathlib.Path("main/data/transactions.csv")
    elif choice == 3:
        return pathlib.Path("main/data/transactions.xlsx")
    else:
        return None

def main():
    print("Привет! Добро пожаловать в программу работы с банковскими транзакциями.")
    print("Выберите необходимый пункт меню:")
    print("1. Получить информацию о транзакциях из JSON-файла")
    print("2. Получить информацию о транзакциях из CSV-файла")
    print("3. Получить информацию о транзакциях из XLSX-файла")

    while True:
        try:
            choice = int(input("Ваш выбор: "))
            if 1 <= choice <= 3:
                break
            else:
                print("Ошибка ввода. Выберите правильный номер пункта меню.")
        except ValueError:
            print("Ошибка ввода. Пожалуйста, введите число.")

    file_path = get_file_path(choice)
    if file_path is not None:
        print(f"Для обработки выбран файл: {file_path}")
    else:
        print("Ошибка ввода. Выберите правильный номер пункта меню.")

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

    # Вывод транзакций после фильтрации по статусу
    print(f"Операции отфильтрованы по статусу: {status}")

    # Вопросы для уточнения выборки
    while True:
        answer = input("Отсортировать операции по дате? Да/Нет: ").lower()
        if answer == "да":
            while True:
                order = input("Отсортировать по возрастанию или по убыванию? ").lower()
                if order == "возрастание":
                    filtered_transactions = sort_transactions_by_date(filtered_transactions, "ascending")
                    break  # Выход из внутреннего цикла после успешной сортировки
                elif order == "убывание":
                    filtered_transactions = sort_transactions_by_date(filtered_transactions, "descending")
                    break  # Выход из внутреннего цикла после успешной сортировки
                else:
                    print("Неверный выбор. Пожалуйста, введите 'возрастание' или 'убывание'.")
                    continue  # Повторяем внутренний цикл для нового ввода
            break  # Выход из внешнего цикла после успешного выбора сортировки
        elif answer == "нет":
            break  # Выход из внешнего цикла, если сортировка не нужна
        else:
            print("Неверный ввод. Пожалуйста, введите 'Да' или 'Нет'.")
            continue  # Повторяем внешний цикл для нового ввода
    while True:
        answer = input("Выводить только рублевые транзакции? Да/Нет: ").lower()
        if answer == "да":
            filtered_transactions = filter_rub_transactions(filtered_transactions)
            break # Выход из внутреннего цикла после успешной сортировки
        elif answer == "нет":
            break  # Выход из внешнего цикла, если сортировка не нужна
        else:
            print("Неверный ввод. Пожалуйста, введите 'Да' или 'Нет'.")
            continue  # Повторяем внешний цикл для нового ввода
    answer = input("Отфильтровать список транзакций по определенному слову в описании? Да/Нет: ").lower()
    if answer == "да":
        search_term = input("Введите слово для фильтрации: ")
        filtered_transactions = filter_transactions_by_description(filtered_transactions, search_term)

    # Печать итогового списка транзакций
    if filtered_transactions:
        print("\nРаспечатываем итоговый список транзакций...")
        for idx, transaction in enumerate(filtered_transactions, start=1):
            print(f"{idx}. {transaction['date']} {transaction['description']}")
            print(f"Счет: {transaction.get('account', '-')}")  # Безопасное извлечение значения
            print(
                f"Сумма: {transaction.get('operationAmount', {}).get('amount', '-')}\n")  # Извлекаем сумму из вложенного словаря
        print(f"\nВсего банковских операций в выборке: {len(filtered_transactions)}.")
    else:
        print("Не найдено ни одной транзакции, подходящей под ваши условия фильтрации.")
if __name__ == "__main__":
    main()