class Car:
    show_speed = 70

    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print(f'Авто {self.name} поехало')

    def stop(self):
        print(f'Авто {self.name} остановилось')

    def turn(self, direction):
        print(f'Авто {self.name} повернуло {direction}')

class TownCar(Car):

    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        if self.speed > 40:
            print('Превышение скорости')


class SportCar(Car):

    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)



class WorkCar(Car):

    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        if self.speed > 60:
            print('Превышение скорости')

class PoliceCar(Car):

    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


tc = TownCar(41, 'black', 'BMW', False)
sc = SportCar(100, 'red', 'Toyota', False)
wc = WorkCar(61, 'brown', 'Lada', False)
pc = PoliceCar(100, 'white', 'Lamborgini', True)

print(tc.go(), tc.stop(), tc.turn('left'), tc.show_speed())
print(sc.go(), sc.stop(), sc.turn('right'))
print(wc.go(), wc.stop(), wc.turn('left'), wc.show_speed())
print(pc.go(), pc.stop(), pc.turn('right'))