import re


def email_parse(email_address):
    re_email = re.compile(r'(?P<username>([\w]+))@(?P<domain>[^&]+\.\w+)', re.IGNORECASE)
    if not re_email.match(email_address):
        raise ValueError(f'Not email')
    print(re_email.match(email_address).groupdict())

try:
    email_parse('someone@greekbrains.ru')
    email_parse('dfdsfsdf')
except ValueError as e:
    print(e)
