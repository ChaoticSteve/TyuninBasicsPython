def num_translate_adv(name):
    if name.istitle():
        digit_translate = {'One': 'Один', 'Two': 'Два',
                           'Three': 'Три', 'Four': 'Четыре',
                           'Five': 'Пять', 'Six': 'Шесть',
                           'Seven': 'Семь', 'Eight': 'Восемь',
                           'Nine': 'Девять', 'Ten': 'Десять'}
        print(digit_translate.get(name))
    else:
        digit_translate = {'one': 'один', 'two': 'два',
                           'three': 'три', 'four': 'четыре',
                           'five': 'пять', 'six': 'шесть',
                           'seven': 'семь', 'eight': 'восемь',
                           'nine': 'девять', 'ten': 'десять'}
        print(digit_translate.get(name))


num_translate_adv('Six')
num_translate_adv('six')
num_translate_adv('eleven')
