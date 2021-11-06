# Создайте собственный класс-исключение, обрабатывающий ситуацию деления на ноль. Проверьте его работу на данных, вводимых пользователем.
# При вводе нуля в качестве делителя программа должна корректно обработать эту ситуацию и не завершиться с ошибкой.

class Zero_Divizion_Marduk(Exception):
    def __init__(self, text):
        self.text = text

num_1 = input('Введите делимое: ')
num_2 = input('Введите делитель: ')
try:
    num_1 = int(num_1)
    num_2 = int(num_2)
    if num_2 == 0:
        raise Zero_Divizion_Marduk('На ноль не делим! Бесконечность ∞ получится!')

except (ValueError, Zero_Divizion_Marduk) as error:
    print(error)
else:
    print(num_1, ' / ', num_2, '=', num_1 / num_2)