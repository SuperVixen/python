# Задача 32:
# Определить индексы элементов массива (списка),
# значения которых принадлежат заданному диапазону
# (т.е. не меньше заданного минимума и не больше заданного максимума)

import random

my_list = [random.randint(0, 20) for i in range(10)]
print(my_list)
min_num = int(input('Введите нижний предел: '))
max_num = int(input('Введите верхний предел: '))

print([i for i in range(len(my_list)) if min_num <= my_list[i] <= max_num])
# FIN
