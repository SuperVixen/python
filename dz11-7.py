# Реализовать проект «Операции с комплексными числами».
# Создайте класс «Комплексное число».
# Реализуйте перегрузку методов сложения и умножения комплексных чисел.
# Проверьте работу проекта.
# Для этого создаёте экземпляры класса (комплексные числа), выполните сложение и умножение созданных экземпляров.
# Проверьте корректность полученного результата.

class My_complex:

    def __init__(self, x, y):
        self.x = complex(x, y)
        print('Комплексное число: ', self.x)
        pass

    def __add__(self, other):
        print('Сумма: ', self.x, '+', other.x, '=', end=' ')
        x = self.x + other.x
        print( x)

    def __mul__(self, other):
        print('Произведение: ', self.x, '*', other.x, '=', end=' ')
        x = self.x * other.x
        print(x)

complex_1 = My_complex(3, 1)
complex_2 = My_complex(2, -3)
complex_1 + complex_2
complex_1 * complex_2  # 6 - 9j + 2j -3j**2 = 9 - 7j
