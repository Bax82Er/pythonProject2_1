from datetime import datetime


def mask_account_card(account_info: str) -> str:
    """Функция для маскирования номера карты или счета."""

    if account_info.startswith('Счет'):
        # Если это счет, то оставляем только последние 4 цифры
        return f"Счет {'*' * (len(account_info) - 10)} {account_info[-4:]}"
    else:
        # Если это карта, то показываем первые 6 и последние 4 цифры
        card_number = account_info.split()[-1]
        masked_number = f"{card_number[:6]} {'*' * 7} {card_number[-4:]}"

        # Возвращаем строку с типом карты и замаскированным номером
        return ' '.join([account_info.split()[0], masked_number])


def get_date(date_str: str) -> str:
    """Преобразование даты из ISO 8601 в формат ДД.ММ.ГГГГ"""
    try:
        date_obj = datetime.fromisoformat(date_str)
        return date_obj.strftime("%d.%m.%Y")
    except ValueError as e:
        raise ValueError(f"Неверный формат даты: {date_str}") from e


