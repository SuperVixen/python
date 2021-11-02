# Реализуйте базовый класс Car.
# у класса должны быть следующие атрибуты: speed, color, name, is_police(булево).
# А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда);
# опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar;
# добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля;
# для классов TownCar и WorkCar переопределите метод show_speed.
# При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
# Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
# Вызовите методы и покажите результат.

from random import choice


class Car:
    """Main  Car"""
    direction = ['north', 'northeast', 'east', 'southeast', 'south', 'southwest', 'west', 'northwest']

    def __init__(self, n, c, s, p=False):
        self.name = n
        self.color = c
        self.speed = s
        self.is_police = p
        print('New car:', n, 'has a color', c, '\n', 'Is the car a police car?', p)

    def go(self):
        print(self.name, 'Car went.')

    def stop(self):
        print(self.name, 'Car stopped!')

    def turn(self):
        print(self.name, 'Car turned toward', choice(self.direction))

    def show_speed(self):
        print(self.name, 'Car speed:', self.speed)

class TownCar(Car):
    """City Car"""

    def show_speed(self):
        return f'{self.name}: Car speed: {self.speed}. Speeding!' if self.speed > 60 else super().show_speed()


class WorkCar(Car):
    """Cargo truck"""

    def show_speed(self):
        return f'{self.name}: Car speed: {self.speed}. Speeding!' if self.speed > 40 else super().show_speed()


class SportCar(Car):
    """Sports Car"""


class PoliceCar(Car):
    """Patrol Car"""

    def __init__(self, n, c, s, p=True):
        super().__init__(n, c, s, p=True)

police_car = PoliceCar('Патриот', 'небесно-голубой, 83 года', 80)
work_car = WorkCar('Автобус', 'оранжевый', 45)
sport_car = SportCar('Что-то быстрое', 'с перламутровыми ручками', 120)
town_car = TownCar('Матиз', 'серебристый, как сабля самурая', 50)

list_of_cars = [police_car, work_car, sport_car, town_car]

for i in list_of_cars:
    i.go()
    print(i.show_speed())
    i.turn()
    i.stop()
    print()

