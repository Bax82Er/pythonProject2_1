from datetime import datetime
from functools import wraps


def log(filename=None):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            global result
            start_time = datetime.now()
            try:
                result = func(*args, **kwargs)
                end_time = datetime.now()
                duration = (end_time - start_time).total_seconds() * 1000
                message = f"{func.__name__} ok. Result: {result}. Duration: {duration:.2f} ms."
            except Exception as e:
                message = f"{func.__name__} error: {type(e).__name__}. Message: {e}. Inputs: {args}, {kwargs}."

            if filename is not None:
                with open(filename, 'a') as file:
                    file.write(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')[:-3]}]: {message}\n")
            else:
                print(message)

            return result

        return wrapper

    return decorator