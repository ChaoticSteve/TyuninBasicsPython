staff = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА', 'токарь высшего разраяда нИКОЛАЙ', 'директор аэлита']
for i in range(len(staff)):
    staff[i] = staff[i].title().split(' ')
    print(f'Привет, {staff[i][len(staff[i]) - 1]}!')
