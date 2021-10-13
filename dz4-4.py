import utils
from sys import argv

if __name__ == "__main__":
    word = argv[1]
    utils.currency_rates(word)
# utils.currency_rates('eur')
# utils.currency_rates('CAD')