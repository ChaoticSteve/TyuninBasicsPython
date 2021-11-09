class Car:
    def __init__(self, speed, colour, name):
        self.speed = float(speed)
        self.colour = colour
        self.name = name
        self.police = False

    def go(self):
        return f'Машина поехала'

    def stop(self):
        return f'Машина остановилась'

    def turn(self, direction):
        return f'Машина поворачивает {direction}'

    def show_speed(self):
        return self.speed


class TownCar(Car):
    def __init__(self, speed, colour, name):
        super().__init__(speed, colour, name)
        if self.speed > 60:
            print(f'Превышение скорости на {self.speed - 60}')


class SportCar(Car):
    pass


class WorkCar(Car):
    def __init__(self, speed, colour, name):
        super().__init__(speed, colour, name)
        if self.speed > 40:
            print(f'Превышение скорости на {self.speed - 40}')


class PoliceCar(Car):
    def __init__(self, speed, colour, name):
        super().__init__(speed, colour, name)
        self.police = True


work_car = WorkCar('66.5', 'желтая', 'KAMAZ')
print(work_car)
print(work_car.go())
print(work_car.show_speed())
print(work_car.turn('влево'))
print(work_car.turn('вправо'))
print(work_car.stop())

town_car = TownCar('50', 'белая', 'Kia Rio')
print(town_car)
print(town_car.speed)
print(town_car.colour)
print(town_car.name)
print(town_car.police)

sport_car = SportCar('270', 'красная', 'McLaren F1') # Cause red goez fasta!
print(sport_car)

police_car = PoliceCar('240', 'сине-белая', 'Skoda Octavia')
print(police_car)
print(police_car.police)
