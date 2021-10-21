"""
Task 1
Написать генератор нечётных чисел от 1 до n (включительно), используя ключевое слово yield
"""


def nums_gen(n):
    for num in range(1, n + 1, 2):
        yield num


print(type(nums_gen(15)))

"""
Task 2
Решить задачу генерации нечётных чисел от 1 до n (включительно), не используя ключевое слово yield.
"""


def nums_gen_adv(n):
    return (num for num in range(1, n + 1, 2))


print(type(nums_gen_adv(20)))
