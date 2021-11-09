class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        return f'Запуск отрисовки'


class Pen(Stationery):
    def draw(self):
        return f'Ручка пишет слова'


class Pencil(Stationery):
    def draw(self):
        return f'Карандаш чертит линии'


class Handle(Stationery):
    def draw(self):
        return f'Маркер выделяет текст'


stationery = Stationery('Великолепный по смыслу и тексту заголовок')
print(stationery.draw())
pen = Pen('Ещё один заголовок')
print(pen.draw())
pencil = Pencil('И снова заголовок')
print(pencil.draw())
handle = Handle('Не поверите, это заголовок')
print(handle.draw())