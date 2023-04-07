import time
import sys

nums = [n for _ in range(2) for n in (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1)]


if __name__ == '__main__':
    msg = sys.argv[1]
    wind = ' '
    for num in nums:
        time.sleep(0.1)
        print(wind * num + msg)
