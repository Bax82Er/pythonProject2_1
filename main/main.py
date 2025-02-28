import csv
import json
from typing import Any

import openpyxl
from ..src.transactions import filter_transactions_by_description


def load_json(filename):
    with open(filename, 'r') as file:
        data = json.load(file)
    return data


def load_csv(filename):
    transactions = []
    with open(filename, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            transactions.append(row)
    return transactions


def load_xlsx(filename):
    transactions = []
    workbook = openpyxl.load_workbook(filename)
    sheet = workbook.active
    for row in sheet.iter_rows(min_row=2, values_only=True):
        transactions.append({
            'date': row[0],
            'description': row[1],
            'account': row[2],
            'amount': row[3]
        })
    return transactions


def get_user_input(prompt, choices=None):
    while True:
        user_input = input(prompt).strip().lower()
        if choices is not None and user_input not in choices:
            print("Недопустимый выбор. Попробуйте снова.")
        else:
            return user_input


def sort_transactions_by_date(transactions, ascending=True):
    return sorted(transactions, key=lambda x: x['date'], reverse=not ascending)


def filter_rub_transactions(transactions):
    return [transaction for transaction in transactions if 'руб' in transaction['amount'].lower()]


def main():
    global transactions
    print("Привет! Добро пожаловать в программу работы с банковскими транзакциями.")
    print("Выберите необходимый пункт меню:")
    print("1. Получить информацию о транзакциях из JSON-файла")
    print("2. Получить информацию о транзакциях из CSV-файла")
    print("3. Получить информацию о транзакциях из XLSX-файла")

    choice = int(get_user_input("Ваш выбор: ", ['1', '2', '3']))

    if choice == 1:
        filename = 'data.json'
        transactions = load_json(filename)
        print(f"Для обработки выбран JSON-файл {filename}.")
    elif choice == 2:
        filename = 'data.csv'
        transactions = load_csv(filename)
        print(f"Для обработки выбран CSV-файл {filename}.")
    elif choice == 3:
        filename = 'data.xlsx'
        transactions = load_xlsx(filename)
        print(f"Для обработки выбран XLSX-файл {filename}.")

    available_statuses = ["EXECUTED", "CANCELED", "PENDING"]
    status = get_user_input(
        f"Введите статус, по которому необходимо выполнить фильтрацию.\nДоступные для фильтровки статусы: {', '.join(available_statuses)}: ",

        available_statuses
    )
    filtered_transactions: list[dict[str, Any] | Any] = [transaction for transaction in transactions if transaction['status'] == status]
    print(f"Операции отфильтрованы по статусу '{status}'.")

    sort_choice = get_user_input("Отсортировать операции по дате? Да/Нет: ", ['да', 'нет'])
    if sort_choice == 'да':
        order_choice = get_user_input("Отсортировать по возрастанию или по убыванию?: ", ['возрастание', 'убывание'])
        if order_choice == 'возрастание':
            filtered_transactions = sort_transactions_by_date(filtered_transactions)
        else:
            filtered_transactions = sort_transactions_by_date(filtered_transactions, False)

    rub_only_choice = get_user_input("Выводить только рублевые транзакции? Да/Нет: ", ['да', 'нет'])
    if rub_only_choice == 'да':
        filtered_transactions = filter_rub_transactions(filtered_transactions)

    word_filter_choice = get_user_input("Отфильтровать список транзакций по определенному слову в описании? Да/Нет: ", ['да', 'нет'])
    if word_filter_choice == 'да':
        search_word = input("Введите слово для фильтрации: ")
        filtered_transactions = filter_transactions_by_description(filtered_transactions, search_word)

    if len(filtered_transactions) > 0:
        print("\nРаспечатываем итоговый список транзакций...")
        for i, transaction in enumerate(filtered_transactions, start=1):
            print(f"{i}. {transaction['date']} {transaction['description']}")
            print(f"Счет: {transaction['account']}")
            print(f"Сумма: {transaction['amount']}\n")
        print(f"\nВсего банковских операций в выборке: {len(filtered_transactions)}.")
    else:
        print("Не найдено ни одной транзакции, подходящей под ваши условия фильтрации.")

if __name__ == "__main__":
    main()
