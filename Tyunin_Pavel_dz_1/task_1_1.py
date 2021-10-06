try:
    duration = int(input('Введите продолжительность в секундах: '))
    if duration < 60:
        sec = duration
        print(f'{sec} сек')
    elif 60 <= duration < 3600:  # равносильно записи duration >= 60 and duration < 3600
        minute = duration // 60
        sec = duration % 60
        print(f'{minute} мин {sec} сек')
    elif 3600 <= duration < 86400:  # равносильно записи duration >= 3600 and duration < 86400
        hour = duration // 3600
        minute = (duration % 3600) // 60
        sec = (duration % 3600) % 60
        print(f'{hour} час {minute} мин {sec} сек')
    else: # во всех остальных случаях
        day = duration // 86400
        hour = (duration % 86400) // 3600
        minute = ((duration % 3600) // 60)
        sec = (duration % 3600) % 60
        print(f'{day} дн {hour} час {minute} мин {sec} сек')
except ValueError:  # определил исключение, если пользоваетль введёт не число
    print('Нужно ввести числовое значение')
