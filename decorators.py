import time
from functools import wraps
'''
未使用裝飾器之前：
timer 函式扮演修飾別人的角色

dosomething 函式作為參數物件傳入 timer
dosomething 在 timer 裡面叫做 func
而 dosomething 的參數 sleep_time 會作為 wrap 的參數
'''

from functools import wraps


def timer(param: str):
    def timer_func(func):
        @wraps(func)
        def wrap(*args, **kwargs):
            t_start = time.time()
            print(param)
            value = func(*args, **kwargs)
            t_count = time.time() - t_start
            print(f"Function '{func.__name__}' spend: {t_count} s")
            return value

        return wrap

    return timer_func


@timer("Print before function start")
def dosomething(a, b):
    print(f"Count: {a + b}")


if __name__ == '__main__':
    dosomething(1, 2)
    print(dosomething.__name__)
