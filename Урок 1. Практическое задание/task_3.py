"""
Задание 3.

Узнайте у пользователя целое положительное число n.
Найдите сумму чисел n + nn + nnn.

Пример:
Введите число n: 3
n + nn + nnn = 369
"""


def exercise_3():
    number = int(input("Введите число: "))
    result = str(number) + str(number*2) + str(number*3)
    print(result)


exercise_3()
