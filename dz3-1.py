# Написать функцию num_translate(), переводящую числительные от 0 до 10 c английского на русский язык.
# Например:
# >>> num_translate("one")
# "один"
# >>> num_translate("eight")
# "восемь"
# Если перевод сделать невозможно, вернуть None

dict_ru_eng = {'zero': 'ноль', 'one': 'один', 'two': 'два', 'three': 'три', 'four': 'четыре', 'five': 'пять', 'six': 'шесть', 'seven': 'семь', 'eight': 'восемь', 'nine': 'девять', 'ten': 'десять'}

def num_translate(inglish):
    return dict_ru_eng.get(inglish)

word = input('Enter number from 0 to 10: ')
print(word, 'at Russian looks like',num_translate(word))
