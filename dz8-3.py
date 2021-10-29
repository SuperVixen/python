# Написать декоратор для логирования типов позиционных аргументов функции, например:
# def type_logger...
#     ...
#
#
# @type_logger
# def calc_cube(x):
#    return x ** 3
#
# >>> a = calc_cube(5)
# 5: <class 'int'>
# Примечание: если аргументов несколько - выводить данные о каждом через запятую;
# можете ли вы вывести тип значения функции?
# Сможете ли решить задачу для именованных аргументов?
# Сможете ли вы замаскировать работу декоратора?
# Сможете ли вывести имя функции, например, в виде:
# >>> a = calc_cube(5)
# calc_cube(5: <class 'int'>)

from functools import wraps

def type_logger(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        num_list = [el for el in (*args, *kwargs.values())]
        n = [f'{func.__name__}({el}: {type(el)})' for el in num_list]
        print(*n, *func(*args, **kwargs), sep=',\n')

    return wrapper

@type_logger
def calc_cube(*x, **y):
    num_list = [el for el in (*x, *y.values()) if isinstance(el, int) or isinstance(el, float)]
    return [i ** 3 for i in num_list]

# print(calc_cube.__name__)
# help(calc_cube)
a = calc_cube(4, 16, 13.3, 75, {'num': 3}, (2, 'ghost'), {4, 45}, [12, 34], 'строка')
# a = calc_cube(1, {'num': 3}, (2, 'ghost'), {4, 4}, [12, 34], 'строка')
# calc_cube(2)