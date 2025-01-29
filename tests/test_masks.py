import pytest

# Импортируем функции для тестирования
from src.masks import get_mask_card_number, get_mask_account


@pytest.mark.parametrize(
    'card_number, expected',
    [
        ('1234567890123456', '123456 **** **** 3456'),
        ('9876543210987654', '987654 **** **** 7654')
    ]
)
def test_get_mask_card_number(card_number, expected):
    # Тестируем функцию get_mask_card_number
    assert get_mask_card_number(card_number) == expected


@pytest.mark.parametrize(
    'invalid_card_number, exception_message',
    [
        ('12345', 'Неверная длина номера карты'),  # Слишком короткая карта
        ('12345678901234567890', 'Неверная длина номера карты')  # Слишком длинная карта
    ]
)
def test_invalid_length_card_number(invalid_card_number, exception_message):
    with pytest.raises(ValueError) as exc_info:
        get_mask_card_number(invalid_card_number)

    assert str(exc_info.value) == exception_message


@pytest.mark.parametrize(
    'account_number, expected',
    [
        ('12345678', '****5678'),
        ('98765432', '****5432'),
        ('99999999', '****9999')
    ]
)
def test_get_mask_account(account_number, expected):
    # Тестируем функцию get_mask_account
    assert get_mask_account(account_number) == expected


@pytest.mark.parametrize(
    'invalid_account_number, exception_message',
    [
        ('1234567', 'Неверная длина номера счета'),  # Слишком короткий счет
        (None, 'Номер счета не может быть пустым')  # Передан None
    ]
)
def test_invalid_length_account_number(invalid_account_number, exception_message):
    with pytest.raises(ValueError) as exc_info:
        get_mask_account(invalid_account_number)

    assert str(exc_info.value) == exception_message
