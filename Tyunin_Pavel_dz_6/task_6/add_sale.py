import sys
price = sys.argv[1] + '\n'

with open('bakery.csv', 'a', encoding='utf-8') as f_n:
    f_n.write(price)
