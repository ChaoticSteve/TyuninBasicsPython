class Clothes:
    def __init__(self, name, param):
        self.name = name
        self.param = param

    def __str__(self):
        if self.name == 'пальто':
            return f'{self.name.title()} {self.param} размера'
        elif self.name == 'костюм':
            return f'{self.name.title()} {self.param} роста'
        else:
            raise NameError('Такую одежду не шьём')

    @property
    def quantity_cloth(self):
        if self.name == 'пальто':
            result = self.param / 6.5 + 0.5
        elif self.name == 'костюм':
            result = self.param * 2 + 0.3
        else:
            raise NameError('Такую одежду не шьём!')
        return f'На {self.name} понадобится {result:.2f} ткани'

    def __del__(self):
        print('Рассчет окончен!')


coat = Clothes('пальто', 2)
print(coat)
print(coat.quantity_cloth)
suit = Clothes('костюм', 1.76)
print(suit)
print(suit.quantity_cloth)
try:
    shirt = Clothes('рубашка', 5)
    print(shirt.quantity_cloth)
except NameError as e:
    print(e)

from abc import ABC, abstractmethod


class Clothes(ABC):
    def __init__(self, name, param):
        self.name = name
        self.param = param

    @abstractmethod
    def quantity_cloth(self):
        pass


class Coat(Clothes):
    @property
    def quantity_cloth(self):
        result = self.param / 6.5 + 0.5
        return f'На {self.name} понадобится {result:.2f} ткани'


class Suit(Clothes):
    @property
    def quantity_cloth(self):
        result = self.param * 2 + 0.3
        return f'На {self.name} понадобится {result:.2f} ткани'

coat = Coat('пальто', 3)
print(coat.quantity_cloth)
suit = Suit('костюм', 1.76)
print(suit.quantity_cloth)
