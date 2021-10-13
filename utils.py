from requests import get, utils
from datetime import datetime


def currency_rates(code):

    response = get('http://www.cbr.ru/scripts/XML_daily.asp')
    encodings = utils.get_encoding_from_headers(response.headers)
    content = response.content.decode(encoding=encodings)



    my_list = content.split('<Valute ID=')
    # извлекаем дату, это брал уже из разбора
    data = datetime.strptime(my_list[0].split('"')[-4], '%d.%m.%Y').date()
    code = code.upper()
    for i in my_list:
        result = 0
        if code in i:
            i = i.split('Value>')
            result = str(i[1:2])
            print(data, code, result[2:-4])
            break
    if result == 0:
        print('None')

if __name__ == "__main__":
    print('Hi')
# else:
#     print("I'm a module")

# currency_rates('USD')