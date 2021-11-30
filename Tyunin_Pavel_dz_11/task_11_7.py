class ComplexNum():
    def __init__(self, com_num):
        self.com_num = com_num

    def __str__(self):
        return f'{self.com_num}'

    def __add__(self, other):
        a = int(self.check_num['a'])
        b = int(self.check_num['b'])
        c = int(other.check_num['a'])
        d = int(other.check_num['b'])
        if b == 0 and d == 0:
            return self.__class__(f'{a + c}')
        return self.__class__(f"{a + c} + {b + d}i")

    def __mul__(self, other):
        a = int(self.check_num['a'])
        b = int(self.check_num['b'])
        c = int(other.check_num['a'])
        d = int(other.check_num['b'])
        if b == 0 and d == 0:
            return self.__class__(f'{a * c}')
        return self.__class__(f"{a * c - b * d} + {a * d + b * c}i")

    @property
    def check_num(self):
        import re
        pattern = re.compile(r'(?P<a>\d+)\s*\+\s*(?P<b>\d+)i')
        result = pattern.search(f'{self.com_num}')
        if result:
            return result.groupdict()
        elif str(self.com_num).isdigit:
            return {'a': self.com_num, 'b': '0'}
        raise ValueError(f'Не верная запись: {self.com_num}')


num_1 = ComplexNum('3 + 6i')
num_2 = ComplexNum('8 + 11i')
print(num_1 + num_2)
print(num_1 * num_2)
