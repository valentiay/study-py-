import sys

from functools import wraps


def memoize(func):
    mem = {}

    @wraps(func)
    def wrapper(*args, **kwargs):
        tmp = args + tuple(sorted(kwargs.items()))
        if tmp not in mem:
            mem[tmp] = func(*args, **kwargs)
        return mem[tmp]
    return wrapper

exec(sys.stdin.read())

