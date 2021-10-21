# Есть два файла: в одном хранятся ФИО пользователей сайта, а в другом — данные об их хобби.
# Известно, что при хранении данных используется принцип: одна строка — один пользователь,
# разделитель между значениями — запятая. Написать код, загружающий данные из обоих файлов и формирующий из них словарь:
# ключи — ФИО, значения — данные о хобби.
# Сохранить словарь в файл. Проверить сохранённые данные.
# Если в файле, хранящем данные о хобби, меньше записей, чем в файле с ФИО, задаём в словаре значение None.
# Если наоборот — выходим из скрипта с кодом «1».
# При решении задачи считать, что объём данных в файлах во много раз меньше объема ОЗУ.

from itertools import zip_longest

with open('users.csv', 'r', encoding='utf-8') as users:
    line_users = users.read().split('\n')
with open('hobby.csv', 'r', encoding='utf-8') as hobby:
    line_hobby = hobby.read().split('\n')
if len(line_hobby) > len(line_users):
    print('Error code 1')
    exit(1)
result_dict = dict(zip_longest(line_users, line_hobby))
txt = str(result_dict) + '\n'

with open('result_hobbies.csv', 'w', encoding='utf-8') as result_hobbies:
    result_hobbies.write(txt)
