class Date:
    def __init__(self, date):
        self.date = date
        self.real_date(date)
    def __str__(self):
        return f'{self.date}'

    @classmethod
    def real_date(cls, date):
        import re
        pattern = re.compile(r'(?P<day>\d{2})-(?P<month>\d{2})-(?P<year>\d+)$')
        check_date = pattern.match(date)
        if not check_date:
            raise ValueError('Дата введена не верно')
        date_dict = check_date.groupdict()
        for key in date_dict:
            date_dict[key] = int(date_dict[key])
        cls.date_valid(date_dict)
        return date_dict

    @staticmethod
    def date_valid(date):
        if date['day'] < 0 or date['day'] > 31:
            raise ValueError('Некорректное количество дней')
        elif date['month'] < 0 or date['month'] > 12:
            raise ValueError('Некорректное количество месяцев')
        elif date['year'] < 0:
            raise ValueError('Некорректное количество лет')


date = Date('15-11-2021')
print(date)
try:
    date_2 = Date('35-11-2021')
except ValueError as e:
    print(e)
try:
    date_3 = Date('15-14-2021')
except ValueError as e:
    print(e)