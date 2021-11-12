import random


class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix

    def __str__(self):
        message = '\n'.join([' '.join([str(num) for num in nums]) for nums in self.matrix])
        return f'{message}\n'

    def __add__(self, other):
        sum_nums = [[(num_1 + num_2) for num_1, num_2 in zip(matrix_1, matrix_2)] \
                    for matrix_1, matrix_2 in zip(self.matrix, other.matrix)]
        return f'Сумма:\n{self.__class__(sum_nums)}'


def random_nums(string, column):
    return [[random.randint(-5, 5) for _ in range(column)] for _ in range(string)]


matrix_1 = Matrix(random_nums(3, 3))
print(matrix_1)
matrix_2 = Matrix(random_nums(3, 3))
print(matrix_2)
print(matrix_1 + matrix_2)
