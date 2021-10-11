def get_message(prices):  # создал функцию для вывода цен через запятую в одну строку
    prices_str = ''
    prices_list = prices.copy()
    for i in range(len(prices_list)):
        prices_list[i] = str(prices_list[i])  # меняем тип объекта
        prices_list[i] = prices_list[i].split('.')  # делим на разные числа
        if len(prices_list[i]) < 2:  # проверяем коичество элементов во вложенном списке
            prices_str += f'{int(prices_list[i][0])}руб 00коп, '  # заполняем строку нужным нам текстом
        else:
            if len(prices_list[i][1]) < 2:  # проверяем количество цифр в числе
                prices_str += f'{int(prices_list[i][0])}руб {int(prices_list[i][len(prices_list[i]) - 1])}0коп, '
            else:
                prices_str += f'{int(prices_list[i][0])}руб {int(prices_list[i][len(prices_list[i]) - 1]):02d}коп, '
    return prices_str


prices = [57.8, 46.51, 97, 5, 3.03, 33.33, 94.06, 12.91, 9, 15, 64.1, 58.4]

print(get_message(prices))  # вывод на экран цены из списка prices
print(f'Id списка до сортировки {id(prices)}, сам список: {prices}')
prices.sort()  # сортировка списка
print(f'Id списка после сортировки {id(prices)}, сам список: {prices}')
print(get_message(prices))  # вывод на экран цены сортированного списка prices

price_decreasing = sorted(prices, reverse=True)  # создание нового списка отсортированного по убыванию
print(price_decreasing)  # вывод нвого списка на экран

price_decreasing = price_decreasing[0:5]  # создание списка с 5-ю самыми дорогими товарами
print(get_message(price_decreasing))  # вывод этих цен на экран
price_decreasing.sort()  # сортировка эти цен по возрастанию
print(get_message(price_decreasing))  # вывод на экран отсортированных цен
