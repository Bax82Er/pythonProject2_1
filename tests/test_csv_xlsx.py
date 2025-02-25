from unittest.mock import patch

import pytest
from src.csv_xlsx import read_csv_transactions, read_excel_transactions


@pytest.fixture(scope="module")
def mock_df():
    # Создаем фикстуру для mock'ированного DataFrame
    data = [
        {"date": "2020-01-01", "amount": 100},
        {"date": "2020-02-01", "amount": 200}
    ]
    return data


@patch("pandas.read_csv")
def test_read_csv_transactions(mock_read_csv, mock_df):
    # Подменяем функцию read_csv
    [mock_read_csv.return_value] = mock_df
    result = read_csv_transactions()
    assert result == mock_df


@patch("pandas.read_excel")
def test_read_xlsx_transactions(mock_read_excel, mock_df):
    # Подменяем функцию read_excel
    [mock_read_excel.return_value] = mock_df
    result = read_excel_transactions()
    assert result == mock_df