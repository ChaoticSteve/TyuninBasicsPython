class IncorrectResult(Exception):
    def __str__(self):
        return f'Клеток не может быть меньше 0'


class Cell:
    def __init__(self, quantity):
        self.quantity = quantity
        if self.quantity < 0:
            raise IncorrectResult

    def __add__(self, other):
        new_cell = self.quantity + other.quantity
        return new_cell

    def __sub__(self, other):
        if self.quantity - other.quantity < 0:
            raise IncorrectResult
        else:
            new_cell = self.quantity - other.quantity
            return new_cell

    def __mul__(self, other):
        new_cell = self.quantity * other.quantity
        return new_cell

    def __truediv__(self, other):
        new_cell = self.quantity // other.quantity
        return new_cell

    def make_order(self, num_of_cells):
        structure_cell = ''
        for i in range(1, self.quantity+1):
            if i % num_of_cells == 0 and i != max(range(1, self.quantity+1)):
                structure_cell += '*\n'
            else:
                structure_cell += '*'
        return structure_cell


cell_1 = Cell(15)
cell_2 = Cell(5)
print(cell_1 + cell_2)
try:
    print(cell_2 - cell_1)
except IncorrectResult as e:
    print(e)
print(cell_1 * cell_2)
print(cell_1 / cell_2)
print(cell_1.make_order(4))
