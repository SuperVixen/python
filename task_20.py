# *Задача 20:
# * В настольной игре Скрабл (Scrabble) каждая буква
# имеет определенную ценность.
# В случае с английским алфавитом очки распределяются так:
# A, E, I, O, U, L, N, S, T, R – 1 очко;
# D, G – 2 очка;
# B, C, M, P – 3 очка;
# F, H, V, W, Y – 4 очка;
# K – 5 очков;
# J, X – 8 очков;
# Q, Z – 10 очков.
#
# А русские буквы оцениваются так:
# А, В, Е, И, Н, О, Р, С, Т – 1 очко;
# Д, К, Л, М, П, У – 2 очка;
# Б, Г, Ё, Ь, Я – 3 очка;
# Й, Ы – 4 очка;
# Ж, З, Х, Ц, Ч – 5 очков;
# Ш, Э, Ю – 8 очков;
# Ф, Щ, Ъ – 10 очков.
#
# Напишите программу, которая вычисляет стоимость
# введенного пользователем слова.
# Будем считать, что на вход подается только одно слово,
# которое содержит либо только английские, либо только русские буквы.
#
# *Пример:*
# ноутбук
#     12

one = 'A, E, I, O, U, L, N, S, T, R, А, В, Е, И, Н, О, Р, С, Т'
two = 'D, G, Д, К, Л, М, П, У'
three = 'B, C, M, P, Б, Г, Ё, Ь, Я'
four = 'F, H, V, W, Y, Й, Ы'
five = 'K, Ж, З, Х, Ц, Ч'
eight = 'J, X, Ш, Э, Ю'
ten = 'Q, Z, Ф, Щ, Ъ'

list_one = list(one.replace(',', '').replace(' ', ''))
list_two = list(two.replace(',', '').replace(' ', ''))
list_three = list(three.replace(',', '').replace(' ', ''))
list_four = list(four.replace(',', '').replace(' ', ''))
list_five = list(five.replace(',', '').replace(' ', ''))
list_eight = list(eight.replace(',', '').replace(' ', ''))
list_ten = list(ten.replace(',', '').replace(' ', ''))

my_dict = {1:list_one, 2:list_two, 3:list_three, 4:list_four, 5:list_five, 8:list_eight, 10:list_ten}

word = list(str(input("Введите слово для подсчёта: ")).upper())
count = 0

for letter in word:
     for key in my_dict.keys():
        for value in my_dict[key]:
            if letter == value:
                # print(letter, key)
                count += key

print(count)
# FIN
