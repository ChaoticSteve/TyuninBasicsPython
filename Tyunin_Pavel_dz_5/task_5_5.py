from itertools import islice
from time import perf_counter
from sys import getsizeof
from decimal import Decimal

# оптимизация по скорости
src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
start = perf_counter()
unique_nums = [num for num in src if src.count(num) == 1]
print(unique_nums, Decimal(perf_counter() - start))
print(getsizeof(unique_nums))

# оптимизация по памяти
src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
start = perf_counter()
unique_nums_gen = (num for num in src if src.count(num) == 1)
print([*islice(unique_nums_gen, len(src))], Decimal(perf_counter() - start))
print(getsizeof(unique_nums_gen))
print(getsizeof([*islice(unique_nums_gen, len(src))]))
