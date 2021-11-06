# Реализовать класс «Дата», функция-конструктор которого должна принимать дату
# в виде строки формата «день-месяц-год». В рамках класса реализовать два метода.
# Первый, с декоратором @classmethod. Он должен извлекать число, месяц, год и преобразовывать их тип к типу «Число».
# Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца и года (например, месяц — от 1 до 12).
# Проверить работу полученной структуры на реальных данных.

class Date:
    @classmethod
    def go_to_number(self, other):
        print('Дата:', other)
        other = other.split('-')
        print('Числа из даты: ')
        for digit in other:
            print(int(digit), type(int(digit)), end=' ')
        return other

    @staticmethod
    def validol(data):
        data = Date.go_to_number(data)
        if (1 <= int(data[0]) <= 31) and (1 <= int(data[1]) <= 12) and int(data[2]) < 2020:
            print('\n', 'Дата введена корректно.', end='\n')
        else:
            print('\n', 'Дата введена не корректно.', '\n')
        pass


    #класс закончился

d_1 = '32-13-2030'
d_3 = '5-12-2002'
Date().validol(d_1)
Date().validol(d_3)
