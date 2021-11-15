class NotDigit(ValueError):
    def __init__(self, text):
        self.text = text


list_numbers = []
while True:
    try:
        number = input('Введите число или stop: ')
        if number.isdigit():
            list_numbers.append(int(number))
        elif number == 'stop':
            print(list_numbers)
            break
        else:
            raise NotDigit('Это не число')
    except NotDigit as e:
        print(e)

'''Не воспринимайте это решение всерьёз, просто позабавился с классом-исключением.'''
# class CheckList(Exception):
#     def __init__(self):
#         list_number = []
#         while True:
#             number = input('Введите число или stop: ')
#             if number.isdigit():
#                 list_number.append(int(number))
#                 print(list_number)
#             elif number == 'stop':
#                 print(list_number)
#                 break
#             else:
#                 print('Это не число повтори ввод')
#
#
# try:
#     number = input('Введите число или stop: ')
#     if not number.isdigit() or number.isdigit():
#         raise CheckList
# except CheckList:
#     pass
