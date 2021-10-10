raw_massage = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
i = 0
sign = ''
while i < len(raw_massage):
    if raw_massage[i][0] in '+-':
        sign = raw_massage[i][0]
    if raw_massage[i].isdigit() or (sign and raw_massage[i][1:].isdigit()):
        if sign:
            raw_massage[i] = sign + raw_massage[i][1:].zfill(2)
        else:
            raw_massage[i] = raw_massage[i].zfill(2)
        raw_massage.insert(i, '"')
        raw_massage.insert(i + 2, '"')
        i += 2
    i += 1
print(raw_massage)
print(' '.join(raw_massage))
