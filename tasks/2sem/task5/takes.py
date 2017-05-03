import sys

from functools import wraps


def takes(*types):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            for a, b in zip(args, types):
                if not isinstance(a, b):
                    raise TypeError
            return func(*args, **kwargs)
        return wrapper
    return decorator

exec(sys.stdin.read())

