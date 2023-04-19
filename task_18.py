# Задача 18:
# Требуется найти в массиве A[1..N] самый близкий по величине элемент
# к заданному числу X.
# Пользователь в первой строке вводит натуральное число N –
# количество элементов в массиве.
# В последующих  строках записаны N целых чисел Ai.
# Последняя строка содержит число X
#
# *Пример:*
# 5
#     1 2 3 4 5
#     6
#     -> 5

import random
number = int(input("Введите количество элементов массива N: "))
number_find = int(input("Введите требуемое число X (положительное, от 1 до 20): "))
number_list = [] # сгенерированный список значений
my_list = [] # список разниц искомого числа с исходными

for i in range(0, number):
    elem = random.randint(1, 20)
    number_list.append(elem)
    my_list.append(abs(elem - number_find))
    print(f"{elem} ", end = "")
print("\n", number_find)
print("-->", number_list[my_list.index(min(my_list))])
# FIN
