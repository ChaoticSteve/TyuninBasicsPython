"""
Task 1
Написать генератор нечётных чисел от 1 до n (включительно), используя ключевое слово yield
"""


def odd_nums(n):
    for num in range(1, n + 1, 2):
        yield num


print(type(odd_nums(15)))

"""
Task 2
Решить задачу генерации нечётных чисел от 1 до n (включительно), не используя ключевое слово yield.
"""


def odd_nums_adv(n):
    return (num for num in range(1, n + 1, 2))


print(type(odd_nums_adv(20)))
