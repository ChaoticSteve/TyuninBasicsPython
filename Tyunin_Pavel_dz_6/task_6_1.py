'''
Не используя библиотеки для парсинга, распарсить (получить определённые данные) файл логов web-сервера nginx_logs.txt
(https://github.com/elastic/examples/raw/master/Common%20Data%20Formats/nginx_logs/nginx_logs) — получить список кортежей вида: (<remote_addr>, <request_type>, <requested_resource>).
'''

import requests

response = requests.get('https://github.com/elastic/examples/raw/master/Common%20Data%20Formats/nginx_logs/nginx_logs')
with open('nginx_logs.txt', 'w+', encoding='UTF-8') as f_n:
    f_n.writelines(response.text)
    f_n.seek(0)
    message = [(string.split()[0], string.split()[5], string.split()[6]) for string in f_n]
    f_n.seek(0)
    search = [string.split()[0] for string in f_n]
print(message)

'''
Найти IP адрес спамера и количество отправленных им запросов по данным файла логов из предыдущего задания.
Примечания: спамер — это клиент, отправивший больше всех запросов; код должен работать даже с файлами, размер которых превышает объем ОЗУ компьютера.
'''

my_dict = {ip: 0 for ip in search}
for ip in search:
    my_dict[ip] += 1
max_requests = max(my_dict, key=my_dict.get)
print(f'Спаммер: {max_requests}')
