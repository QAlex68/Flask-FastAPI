# Синхронный подход пример 2

import time


def slow_function():
    print("Начало функции")
    time.sleep(5)
    print("Конец функции")


print("Начало программы")
slow_function()
print("Конец программы")
