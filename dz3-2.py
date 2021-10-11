# Доработать предыдущую функцию в num_translate_adv(): реализовать корректную работу с числительными,
# начинающимися с заглавной буквы — результат тоже должен быть с заглавной. Например:
# >>> num_translate_adv("One")
# "Один"
# >>> num_translate_adv("two")
# "два"


dict_ru_eng = {'zero': 'ноль', 'one': 'один', 'two': 'два', 'three': 'три', 'four': 'четыре', 'five': 'пять', 'six': 'шесть', 'seven': 'семь', 'eight': 'восемь', 'nine': 'девять', 'ten': 'десять'}

def num_translate(inglish):
    if inglish.istitle():
        return str(dict_ru_eng.get(inglish.lower())).title()
    return dict_ru_eng.get(inglish)

word = input('Enter number from 0 to 10: ')
print(word, 'at Russian looks like',num_translate(word))

