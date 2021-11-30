class ObjectError(Exception):
    def __init__(self, text):
        self.text = text


class Storage:
    def __init__(self):
        self.storage = []

    def __str__(self):
        return f'{[str(_) for _ in self.storage]}'

    def receiving(self, *equipments):
        for equipment in equipments:
            self.storage.append(equipment)

    def transfer(self, division, *equipments):
        for equipment in equipments:
            if equipment not in self.storage:
                raise ObjectError('Данной техники на складе нет')
            division.list_equipment.append(equipment)
            self.storage.remove(equipment)
        return self.storage


class Division:
    def __init__(self):
        self.equipments = []

    def __str__(self):
        return f'{[str(_) for _ in self.equipments]}'

    @property
    def list_equipment(self):
        return self.equipments


class PRDepartment(Division):
    pass


class HRDepartment(Division):
    pass


class OfficeEquipment:
    def __init__(self, model, un_id):
        self.model = model
        self._un_id = self.id_check(un_id)


    def __str__(self):
        return f'{self.model}'

    @staticmethod
    def id_check(un_id):
        if not un_id.isdigit():
            raise ValueError('Не верная запись ID')
        else:
            return un_id


class Printer(OfficeEquipment):
    def __init__(self, model, un_id, print_color):
        super().__init__(model, un_id)
        self.print_color = print_color

    def __str__(self):
        return f'{self.model}, {self.print_color}'


class Scanner(OfficeEquipment):
    def __init__(self, model, un_id, optical_density):
        super().__init__(model, un_id)
        self.optcial_density = optical_density

    def __str__(self):
        return f'{self.model}, {self.optcial_density}'


class Xerox(OfficeEquipment):
    def __init__(self, model, un_id, copy_speed):
        super().__init__(model, un_id)
        self.copy_speed = copy_speed

    def __str__(self):
        return f'{self.model}, {self.copy_speed}'


printer = Printer('HP Printer', '56478', 'white-black')
print(printer)
try:
    printer = Printer('HP Printer', '56nh478', 'white-black')
except ValueError as e:
    print(e)
scanner = Scanner('Canon SuperScan', '54545', '4000*5000dpi')
print(scanner)
xerox = Xerox('Xerox Copy', '698556', '40 page/min')
print(xerox)
storage = Storage()
storage.receiving(printer, scanner, xerox)
print(storage)
pr = PRDepartment()
storage.transfer(pr, xerox)
print(storage)
print(pr)
hr = HRDepartment()
try:
    storage.transfer(hr, xerox)
except ObjectError as e:
    print(e)
