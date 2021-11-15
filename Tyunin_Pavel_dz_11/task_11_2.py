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

