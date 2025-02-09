import unittest
from unittest.mock import patch
from src.external_api import convert_to_rub

class TestExternalApi(unittest.TestCase):
    def setUp(self):
        self.transaction_usd = {'amount': 100, 'currency': 'USD'}
        self.transaction_eur = {'amount': 150, 'currency': 'EUR'}
        self.transaction_rub = {'amount': 5000, 'currency': 'RUB'}

    @patch('src.external_api.requests.get')
    def test_convert_to_rub_usd(self, mock_get):
        mock_response = {
            'json.return_value': {
                'rates': {
                    'USD': 75.00
                }
            },
            'status_code': 200
        }
        mock_get.return_value = mock_response
        result = convert_to_rub(self.transaction_usd)
        self.assertAlmostEqual(result, 7500.00, places=2)

    @patch('src.external_api.requests.get')
    def test_convert_to_rub_eur(self, mock_get):
        mock_response = {
            'json.return_value': {
                'rates': {
                    'EUR': 90.00
                }
            },
            'status_code': 200
        }
        mock_get.return_value = mock_response
        result = convert_to_rub(self.transaction_eur)
        self.assertAlmostEqual(result, 13500.00, places=2)

    def test_convert_to_rub_rub(self):
        result = convert_to_rub(self.transaction_rub)
        self.assertEqual(result, 5000.00)

if __name__ == '__main__':
    unittest.main()
