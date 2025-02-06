from __future__ import annotations
from typing import Any, Callable, Optional, TypeVar
from datetime import datetime
from functools import wraps
import sys

T = TypeVar('T', bound=Callable[..., Any])

def log(filename: Optional[str] = None) -> T:
    """Декоратор для автоматического логирования деталей выполнения функций.

    Аргументы:
        filename (Optional[str], optional): Имя файла для записи логов. Если не указан,
                                            логи будут выведены в консоль.

    Возвращает:
        T: Обёрнутую функцию.

    Примеры:
        >>> @log("mylog.txt")
        ... def my_function(x, y):
        ...     return x + y
        ...
        >>> my_function(1, 2)
        my_function ok. Result: 3. Duration: 0.01 ms.
    """
    def decorator(func: T) -> T:
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            start_time = datetime.now()
            try:
                result = func(*args, **kwargs)
                end_time = datetime.now()
                duration = (end_time - start_time).total_seconds() * 1000
                message = (
                    f"{func.__name__} ok. Result: {result}. Duration: {duration:.2f} ms."
                )
            except Exception as e:
                message = (
                    f"{func.__name__} error: {type(e).__name__}. Message: {e}. "
                    f"Inputs: {args}, {kwargs}."
                )

            if filename is not None:
                with open(filename, 'a') as file:
                    file.write(
                        f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')[:-3]}]: {message}\n"
                    )
            else:
                print(message)

            return result

        return wrapper  # type: ignore

    return decorator