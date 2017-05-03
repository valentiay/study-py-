import sys

from functools import wraps
from time import time


def profiler(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if not wrapper.recursion:
            wrapper.depth = 0
            wrapper.calls = 0
            wrapper.last_time_taken = -time()
            wrapper.recursion = True
        wrapper.depth += 1

        wrapper.calls += 1
        ans = func(*args, **kwargs)

        wrapper.depth -= 1
        if wrapper.depth == 0:
            wrapper.last_time_taken += time()
            wrapper.recursion = False

        return ans

    wrapper.recursion = False
    return wrapper

exec(sys.stdin.read())

