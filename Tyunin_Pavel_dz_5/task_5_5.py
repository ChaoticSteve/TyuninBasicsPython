"""
Task %
Подумайте, как можно сделать оптимизацию кода по памяти, по скорости.
Представлен список чисел. Определить элементы списка, не имеющие повторений.
Сформировать из этих элементов список с сохранением порядка их следования в исходном списке, например:
"""
from itertools import islice
from time import perf_counter
from sys import getsizeof
from decimal import Decimal

# этот вариант не оптимален, т.к. уступает по скорости List Comprehension, а по памяти получается 2 объекта(генератор и список)
src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
start = perf_counter()
unique_nums_gen = (num for num in src if src.count(num) == 1)  # решение поставленной задачи
print([*islice(unique_nums_gen, len(src))], Decimal(perf_counter() - start))
print(getsizeof(unique_nums_gen))
print(getsizeof([*islice(unique_nums_gen, len(src))]))

# самый оптимальный по скорости, по памяти на мой взгляд вариант
src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
start = perf_counter()
unique_nums = [num for num in src if src.count(num) == 1]  # решение поставленной задачи
print(unique_nums, Decimal(perf_counter() - start))
print(getsizeof(unique_nums))

# Подскажите, верно ли я понял задачу с оптимизацией?
