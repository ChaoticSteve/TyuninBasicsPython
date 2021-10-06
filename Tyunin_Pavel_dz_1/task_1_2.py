numbers = []
sum_digits = 0
sum_digits_17 = 0
sum_all = 0
sum_all_17 = 0

for number in range(1, 1001, 2):
    number = number ** 3  # возодим в куб нечетное число
    test_number = number  # вводим переменную для вычисления суммы цифр числа
    while test_number != 0:  # циклом вычислем сумму цифр числа
        sum_digits = sum_digits + test_number % 10
        test_number = test_number // 10
    if sum_digits % 7 == 0:  # проверяем, что сумма цифр числа делится нацело на 7
        sum_all += number  # считаем сумму подходящих нам чисел
    number_17 = number + 17  # вводим переменную для вычисления суммы цифр числа, увеличенного на 17
    while number_17 != 0:  # циклом вычислем сумму цифр числа
        sum_digits_17 = sum_digits_17 + number_17 % 10
        number_17 = number_17 // 10
    if sum_digits_17 % 7 == 0:  # проверяем, что сумма цифр числа делится нацело на 7
        sum_all_17 += (number + 17)  # считаем сумму подходящих нам чисел

    numbers.append(number)  # заполняем список нечетными числами возведёнными в кубк

print(f'Сумма элементов, сумма чисел которых делится нацело на 7 = {sum_all}. '
      f'Сумма элементов, увеличенных на 17, сумма цифр котрых делится нацело на 7 = {sum_all_17}.')
