# Найти IP адрес спамера и количество отправленных им запросов по данным файла логов из предыдущего задания.
# Примечания: спамер — это клиент, отправивший больше всех запросов; код должен работать даже с файлами,
# размер которых превышает объем ОЗУ компьютера
import collections

dict_from_line = {}
with open('nginx_logs.txt', 'r', encoding='utf-8') as f:
    line = f.readline()
    while line:
        line = line.strip().split(' ')[0] # чисто IP - адреса. Как их посчитать
        # print(line)
        if line in dict_from_line:
            dict_from_line[line] +=1
        else:
            dict_from_line[line] = 1
        line = f.readline()
print('Спамер is: ', max(dict_from_line, key=dict_from_line.get), 'выполнено', dict_from_line[max(dict_from_line, key=dict_from_line.get)], 'запросов')
