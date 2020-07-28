class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        if self.is_police:
            print(f'полицейская машина {self.name} поехала')
        else:
            print(f'машина {self.name} поехала')

    def stop(self):
        if self.is_police:
            print(f'полицейская машина {self.name} остановилась')
        else:
            print(f'машина {self.name} остановилась')

    def turn(self, direction):
        if self.is_police:
            print(f'полицейская машина {self.name} повернула {direction}')
        else:
            print(f'машина {self.name} повернула {direction}')

    def show_speed(self):
        if self.is_police:
            print(f'текущая скорость полицейской машины {self.name} = {self.speed}')
        else:
            print(f'текущая скорость машины {self.name} = {self.speed}')


class TownCar(Car):
    def __init__(self, speed, color, name, is_police=False):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        if self.is_police:
            print(f'текущая скорость полицейской машины {self.name} = {self.speed}')
        else:
            if self.speed > 60:
                print(f'машина {self.name} превысила скорость на {self.speed - 60}, текущая скорость {self.speed}')
            else:
                print(f'текущая скорость машины {self.name} = {self.speed}')

    def stop(self):
        if self.is_police:
            print(f'полицейская машина {self.name} остановилась')
        else:
            if self.speed > 60:
                print(f'машина {self.name} остановлена за превышение')
            else:
                print(f'машина {self.name} остановилась')


class SportCar(Car):
    def __init__(self, speed, color, name, is_police=False):
        super().__init__(speed, color, name, is_police)


class WorkCar(Car):
    def __init__(self, speed, color, name, is_police=False):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        if self.is_police:
            print(f'текущая скорость полицейской машины {self.name} = {self.speed}')
        else:
            if self.speed > 40:
                print(f'машина {self.name} превысила скорость на {self.speed - 40}, текущая скорость {self.speed}')
            else:
                print(f'текущая скорость машины {self.name} = {self.speed}')

    def stop(self):
        if self.is_police:
            print(f'полицейская машина {self.name} остановилась')
        else:
            if self.speed > 40:
                print(f'машина {self.name} остановлена за превышение')
            else:
                print(f'машина {self.name} остановилась')


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police=True):
        super().__init__(speed, color, name, is_police)


town_car = TownCar(40, 'yellow', 'Taxi')
sport_car = SportCar(100, 'red', 'Nissan')
work_car = WorkCar(30, 'black', 'Kamaz')
police_car = PoliceCar(100, 'blue', 'FBR')

town_car.go()
town_car.turn('right')
town_car.show_speed()
town_car.turn('left')
town_car.speed = 80
town_car.show_speed()
police_car.go()
police_car.show_speed()
town_car.stop()
sport_car.go()
sport_car.show_speed()
work_car.go()
work_car.show_speed()
work_car.speed = 60
work_car.show_speed()
police_car.go()
police_car.show_speed()
work_car.stop()
