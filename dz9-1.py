# Создать класс TrafficLight (светофор).
# определить у него один атрибут color (цвет) и метод running (запуск);
# атрибут реализовать как приватный;
# в рамках метода реализовать переключение светофора в режимы: красный, жёлтый, зелёный;
# продолжительность первого состояния (красный) составляет 7 секунд, второго (жёлтый) — 2 секунды, третьего (зелёный) — на ваше усмотрение;
# переключение между режимами должно осуществляться только в указанном порядке (красный, жёлтый, зелёный);
# проверить работу примера, создав экземпляр и вызвав описанный метод.
# Задачу можно усложнить, реализовав проверку порядка режимов. При его нарушении выводить соответствующее сообщение и завершать скрипт.
# from time import sleep
# class TrafficLight:
#     color = 'Black'
#
#     def running(self):
#         while True:
#             print('Robot is Red')
#             sleep(4)
#             print('Robot is Yellow')
#             sleep(2)
#             print('Robot is Green') #GradMa, run!
#             sleep(4)
#             print('Robot is Yellow')
#             sleep(2)
#         # print('Light switch On')
#
# robot = TrafficLight()
# robot.running()

import time
import itertools

class TrafficLight:
    __color = [['red', [4, 31]], ['yellow', [2, 33]], ['green', [4, 32]], ['yellow', [2, 33]]]

    def running(self):
        for light in itertools.cycle(self.__color):
            print(f'\r\033[{light[1][1]}m\033[1m{light[0]}\033[0m', end='')
            time.sleep(light[1][0])


robot = TrafficLight()
robot.running()

