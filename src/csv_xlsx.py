import pandas as pd


def read_csv_transactions():
    """
    Функция для чтения финансовых операций из CSV файла.
    :return: Список словарей с транзакциями.
    """
    df = pd.read_csv('/data/transactions.csv')
    return df.to_dict('records')

def read_excel_transactions() -> list[dict]:
        """
        Функция для чтения финансовых операций из Excel файла.
        """
        df = pd.read_excel('/Users/batrerdnneev/my_prj/pythonProject2/src/transactions_excel.xlsx')
        return df.to_dict('records')

