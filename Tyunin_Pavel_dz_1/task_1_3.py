for number in range(1, 101):
    if 4 < number % 100 <= 20:
        print(f'{number} процентов')
    elif number % 10 == 1:
        print(f'{number} процент')
    elif 1 < number % 10 < 5:
        print(f'{number} процента')
    else:
        print(f'{number} процентов')
