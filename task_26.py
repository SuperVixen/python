# Задача 26:
# Напишите программу, которая на вход принимает два числа A и B,
# и возводит число А в целую степень B с помощью рекурсии.
#
# *Пример:*
# A = 3; B = 5 -> 243 (3⁵)
#     A = 2; B = 3 -> 8

def power(base, degree: int) -> int:
    if degree == 1:
        return base
    else:
        return base * power(base, degree - 1)

bas = int(input('Введите основание степени: '))
degre = int(input('Введите показатель степени: '))
print(f'Число {bas} в степени {degre} = {power(bas, degre)}')
# FIN
