"""Модуль для работы с виджетами."""

from datetime import datetime
from typing import Optional


def mask_account_card(account_info: str) -> str:
    """
    Функция для маскирования номера карты или счета.

    :param account_info: Строка, содержащая тип и номер карты или счета.
    :return: Строка с замаскированным номером.
    """
    if account_info.startswith('Счет'):
        return f"Счет {'*' * (len(account_info) - 10)} {account_info[-4:]}"
    else:
        card_number = account_info.split()[-1]
        masked_number = f"{card_number[:6]} {'*' * 7} {card_number[-4:]}"
        return ' '.join([account_info.split()[0], masked_number])


def get_date(date_str: str) -> Optional[str]:
    """
    Преобразование даты из ISO 8601 в формат ДД.ММ.ГГГГ.

    :param date_str: Строка с датой в формате ISO 8601.
    :return: Дата в формате ДД.ММ.ГГГГ или None, если дата неверного формата.
    """
    try:
        date_obj = datetime.fromisoformat(date_str)
        return date_obj.strftime("%d.%m.%Y")
    except ValueError:
        return None
