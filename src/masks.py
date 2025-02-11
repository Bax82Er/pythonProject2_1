import logging
from typing import Union

# Получение логгера
logger = logging.getLogger(__name__)


def get_mask_card_number(local_card_number: str) -> str:
    """
    Возвращает маску номера банковской карты.

    Маска формируется следующим образом: первые шесть цифр остаются неизменными,
    средние восемь цифр заменяются звездочками (*), последние четыре цифры остаются неизменными.
    Все блоки разделены пробелом.

    :local_card_number: Строка, представляющая номер карты (должен содержать 16 цифр)
    :return: Маска номера карты
    :raises ValueError: Если длина номера карты не равна 16 цифрам
    """
    if len(local_card_number) != 16:
        logger.error(
            f"Неверная длина номера карты: {len(local_card_number)} вместо 16."
        )
        raise ValueError("Неверная длина номера карты")

    mask = f"{local_card_number[:6]} {'*' * 4} {'*' * 4} {local_card_number[-4:]}"
    logger.info(f"Сформирована маска номера карты: {mask}")
    return mask


def get_mask_account(account_number: Union[str, int]) -> str:
    """
    Возвращает маску номера банковского счета.

    Маска формируется следующим образом: первые два символа заменяются звездочками (*),
    последние четыре цифры остаются неизменными.

    :account_number: Число или строка, представляющая номер счета (должен содержать минимум 8 цифр)
    :return: Маска номера счета
    :raises ValueError: Если длина номера счета меньше 8 цифр
    """
    if account_number is None:
        logger.error("Номер счета не может быть пустым")
        raise ValueError("Номер счета не может быть пустым")

    if isinstance(account_number, int):
        account_number = str(account_number)

    if len(account_number) < 8:
        logger.error(
            f"Неверная длина номера счета: {len(account_number)} вместо минимум 8."
        )
        raise ValueError("Неверная длина номера счета")

    mask = f"{'*' * (len(account_number) - 4)}{account_number[-4:]}"
    logger.info(f"Сформирована маска номера счета: {mask}")
    return mask
