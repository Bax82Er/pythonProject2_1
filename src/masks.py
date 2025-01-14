from typing import Union


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
        raise ValueError("Неверная длина номера карты")

    return (
        f"{local_card_number[:6]} {local_card_number[6:10].replace(' ', '*')} "
        f"{local_card_number[10:14].replace(' ', '*')} {local_card_number[-4:]}"
    )


def get_mask_account(account_number: Union[str, int]) -> str:
    """
    Возвращает маску номера банковского счета.

    Маска формируется следующим образом: первые два символа заменяются звездочками (*),
    последние четыре цифры остаются неизменными.

    :account_number: Число или строка, представляющая номер счета (должен содержать минимум 8 цифр)
    :return: Маска номера счета
    :raises ValueError: Если длина номера счета меньше 8 цифр
    """
    if isinstance(account_number, int):
        account_number = str(account_number)

    if len(account_number) < 8:
        raise ValueError("Неверная длина номера счета")

    return f"**{account_number[-4:]}"
