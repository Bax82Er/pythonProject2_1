import unittest
from unittest.mock import mock_open, patch

import self

from src.utils import read_json_file

class TestUtils(unittest.TestCase):
    def setUp(self):
        self.file_content = '[{"transaction_id": 1, "amount": 100, "currency": "USD"}]'
        self.empty_file_content = ''
        self.invalid_file_content = '{"key": "value"}'

    @patch('builtins.open', new_callable=mock_open, read_data=self.file_content)
    def test_read_json_file_valid(self, mock_file):
        result = read_json_file('path/to/file.json')
        self.assertEqual(result, [{'transaction_id': 1, 'amount': 100, 'currency': 'USD'}])

    @patch('builtins.open', new_callable=mock_open, read_data=self.empty_file_content)
    def test_read_json_file_empty(self, mock_file):
        result = read_json_file('path/to/file.json')
        self.assertEqual(result, [])

    @patch('builtins.open', new_callable=mock_open, read_data=self.invalid_file_content)
    def test_read_json_file_invalid(self, mock_file):
        result = read_json_file('path/to/file.json')
        self.assertEqual(result, [])

if __name__ == '__main__':
    unittest.main()
