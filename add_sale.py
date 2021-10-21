from sys import argv

if __name__ == "__main__":
    sale = argv[1]
    txt = str(sale) + '\n'
    with open('bakery.csv', 'a', encoding='utf-8') as bakery:
        # txt = str(sale+/n)
        bakery.write(txt)
        # bakery.write(/n)
        # bakery.write()

