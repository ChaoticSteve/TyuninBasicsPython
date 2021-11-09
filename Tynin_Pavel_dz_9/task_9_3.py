class Worker:
    def __init__(self, name, surname, position, wade, bonus=0):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {'wade': wade, 'bonus': bonus}


class Position(Worker):
    def get_full_name(self):
        return f'{self.name} {self.surname}'

    def total_income(self):
        return f'{(self._income["wade"] + self._income["bonus"])} bottle caps'


detective = Position('Nick', 'Valentine', 'detective', 300, 50)
print(detective.get_full_name())
print(detective.total_income())
