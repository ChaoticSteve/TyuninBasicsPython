import requests
import decimal
import datetime


def currency_rate(val):
    response = requests.get('http://www.cbr.ru/scripts/XML_daily.asp').text
    val = val.upper()
    date = response[response.find('Date="') + 6:response.find('"', response.find('Date="') + 6)].split('.')
    day, month, year = map(int, date)
    date_now = datetime.datetime(day=day, month=month, year=year)
    for string in (response.split('</Valute>')):
        if val in string:
            if '100' not in string:
                course = string[string.find('<Value>') + 7:string.find('<', string.find('<Value>') + 7)]
                print(f'Стоимость 1{val} = {decimal.Decimal(course.replace(",", "."))}RUB на момент {date_now}')
                break
            else:
                course = string[string.find('<Value>') + 7:string.find('<', string.find('<Value>') + 7)]
                print(f'Стоимость 100{val} = {decimal.Decimal(course.replace(",", "."))}RUB на момент {date_now}')
                break


currency_rate('eur')
currency_rate('USD')
