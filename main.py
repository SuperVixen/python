# Создать список, состоящий из кубов нечётных чисел от 1 до 1000 (куб X - третья степень числа X):
# Вычислить сумму тех чисел из этого списка, сумма цифр которых делится нацело на 7. Например, число «19 ^ 3 = 6859» будем
# включать в сумму, так как 6 + 8 + 5 + 9 = 28 – делится нацело на 7. Внимание: использовать только арифметические операции!
# К каждому элементу списка добавить 17 и заново вычислить сумму тех чисел из этого списка, сумма цифр которых делится нацело на 7.
# * Решить задачу под пунктом b, не создавая новый список.
#
# Ответики:
# 17 485 588 610
# 15 392 909 930

odd_cube = []
sum_of_digits_in_odd_cube = 0
total_sum = 0

for i in range(0,1001):
    if i % 2 != 0:
        odd_cube.append(i**3)

for n in range(0, len(odd_cube)):
    sum_of_digits_in_odd_cube = 0
    additional_odd_cube = odd_cube[n]
    while additional_odd_cube > 0:
        sum_of_digits_in_odd_cube += additional_odd_cube % 10
        additional_odd_cube = additional_odd_cube // 10
    if sum_of_digits_in_odd_cube % 7 == 0:
        total_sum += odd_cube[n]

print(total_sum)

# часть задания со звездочкой:

# не забываем обнулять переменные, потом мучаешься вылавливать блох
total_sum = 0

for n in range(0, len(odd_cube)):
    odd_cube[n] +=17 #это является созданием нового списка?
    sum_of_digits_in_odd_cube = 0
    additional_odd_cube = odd_cube[n]
    while additional_odd_cube > 0:
        sum_of_digits_in_odd_cube += additional_odd_cube % 10
        additional_odd_cube = additional_odd_cube // 10
    if sum_of_digits_in_odd_cube % 7 == 0:
        total_sum += odd_cube[n]

print(total_sum)

