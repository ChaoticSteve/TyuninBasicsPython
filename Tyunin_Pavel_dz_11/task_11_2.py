class ZeroDivision(Exception):
    def __str__(self):
        return f'На 0 делить нелья'


try:
    num = int(input('Введите делитель: '))
    if num == 0:
        raise ZeroDivision
except ZeroDivision as e:
    print(e)
else:
    num_2 = int(input('Введите делимое: '))
    print(f'{(num_2 / num):.2f}')

'''Еще пришел в голову такой вариант, но упадёт с ошибкой, если забыть передать текст ошибки в блок except'''
# class ZeroDivision(Exception):
#     def __init__(self, text):
#         self.text = text
#
# try:
#     num = int(input('Введите делитель: '))
#     if num == 0:
#         raise ZeroDivision('Делить на 0 нельзя')
# except ZeroDivision as e:
#     print(e)
# else:
#     num_2 = int(input('Введите делимое: '))
#     print(f'{(num_2 / num):.2f}')
