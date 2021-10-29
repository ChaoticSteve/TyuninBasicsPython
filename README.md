import sys
params = sys.argv[1:]
with open('bakery.csv', 'r+', encoding='utf-8') as f:
    start = int(params[0])
    i = 1
    line = f.readline()
    while line:
        if start == i:
            len_string = sum(1 for symbol in line)
            f.seek(f.tell() - len_string - 1)
            f.write(params[1])
            break
        line = f.readline()
        i += 1
Возможное решение 7-го задания
Возникла проблема в том чтоб стереть старое значение и записать новое. Была мысль в скрипте add_sale.py задать параметр на определённое количество символов в числе.
Это решает проблему с перезаписью. Т.к. длина строки не меняется. Но в таком случае страдает универсальность ввода, если число будет превышать заданную нами длину строки.
