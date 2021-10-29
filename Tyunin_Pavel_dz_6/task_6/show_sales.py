import sys

params = sys.argv[1:]

with open('bakery.csv', encoding='utf-8') as f:
    len_prices = (sum(1 for line in f))
    if len(params) == 0:
        start = 1
        stop = len_prices
        f.seek(0)
    elif len(params) == 1:
        start = int(params[0])
        stop = len_prices
        f.seek(0)
    elif len(params) == 2:
        start = int(params[0])
        stop = int(params[1])
        f.seek(0)
    else:
        print('Некорректное число параметров')
    i = 0
    while i < len_prices:
        line = f.readline()
        if start <= i + 1 <= stop:
            print(line.strip())
        i += 1