'''Пока не закончил, кажется перемудрил с запросами, вернусь к этой версии позже.'''
class Storage:
    def __init__(self):
        self.storage = {}
    def __str__(self):
        return f'{self.storage}'
    def receiving(self, *equipments):
        for equipment in equipments:
            self.storage.setdefault(equipment.brand, [])
            self.storage[equipment.brand].append(equipment)
    def get_info(self, key):
        if key not in self.storage.keys():
            print('Оборудование такого бренда нет')
        else:
            i = 0
            for equipment in self.storage[key]:
                i += 1
                print(f'{i}. {(equipment)}')
            choose = input('Введите номер техники, которую хотите переместить: ')
            self.transfer(choose)

    def transfer(self, choose):
        print(choose)


class OfficeEquipment:
    def __init__(self, brand, model, serial_number):
        self.brand = brand
        self.model = model
        self._serial_number = serial_number


class Printer(OfficeEquipment):
    def __init__(self, brand, model, un_id, print_color):
        super(Printer, self).__init__(brand, model, un_id)
        self.print_color = print_color
    def __str__(self):
        return f'{self.brand} {self.model}, {self.print_color}'
class Scanner(OfficeEquipment):
    def __init__(self, brand, model, un_id, optical_density):
        super(Scanner, self).__init__(brand, model, un_id)
        self.optical_density = optical_density
    def __str__(self):
        return f'{self.brand} {self.model}, {self.optical_density}'
class Xerox(OfficeEquipment):
    def __init__(self, brand, model, un_id, copy_speed):
        super(Xerox, self).__init__(brand, model, un_id)
        self.copy_speed = copy_speed
    def __str__(self):
        return f'{self.brand} {self.model}, {self.copy_speed}'


printer = Printer('Hp', 'Printer', '2544', 'white-black')
# print(printer)
printer2 = Printer('Hp', 'Printer+', '26845', 'CYAN')
scanner = Scanner ('Canon', 'SuperScan', '59456', '4000*5000dpi')
# print(scanner)
xerox = Xerox('Xerox', 'MegaCopy', '96456', '40 page/min')
# print(xerox)
storage = Storage()
storage.receiving(printer, printer2, scanner, xerox)
# print(storage)
print(storage.get_info('Hp'))
