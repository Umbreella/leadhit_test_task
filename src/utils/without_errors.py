from typing import Callable


def without_errors(func: Callable, *args, **kwargs) -> bool:
    def wrapper():
        try:
            func(*args, *kwargs)
        except Exception:
            return False

        return True

    return wrapper()
