import unittest

# Реализация функций из модуля src.transactions
def filter_transactions_by_description(transactions, keyword):
    return [transaction for transaction in transactions if keyword in transaction['description']]

def count_operations_by_category(transactions, categories):
    counts = {}
    for category in categories:
        counts[category] = sum(category in transaction['description'] for transaction in transactions)
    return counts

class TestTransactions(unittest.TestCase):
    def setUp(self):
        self.transactions = [
            {'description': 'Перевод с карты на карту'},
            {'description': 'Открытие вклада'},
            {'description': 'Перевод организации'}
        ]

    def test_filter_transactions_by_description(self):
        result = filter_transactions_by_description(self.transactions, 'Перевод')
        expected = [
            {'description': 'Перевод с карты на карту'},
            {'description': 'Перевод организации'}
        ]
        self.assertEqual(result, expected)

    def test_count_operations_by_category(self):
        categories = ['Перевод', 'Открытие']
        result = count_operations_by_category(self.transactions, categories)
        expected = {
            'Перевод': 2,
            'Открытие': 1
        }
        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()
