prices = [57.8, 46.51, 97, 5, 3.03, 33.33, 94.06, 12.91, 9, 15, 64.1, 58.4]
prices_str = ''
for i in range(len(prices)):
    prices[i] = str(prices[i])
    prices[i] = prices[i].split('.')
    if len(prices[i]) < 2:
        prices_str += f'{int(prices[i][0])}руб 00коп, '
    else:
        prices_str += f'{int(prices[i][0])}руб {int(prices[i][len(prices[i]) - 1]):02d}коп, '
print(prices_str)
print(prices)