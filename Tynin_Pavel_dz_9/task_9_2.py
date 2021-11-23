class Road:
    def __init__(self, length, width):
        self._length = length
        self._width = width

    def get_mass(self, mass_in_m2, depth):
        return f'{(self._length * self._width * mass_in_m2 * depth) / 1000:.2f} т'


road = Road(20, 5000)
print(road.mass(25, 5))
