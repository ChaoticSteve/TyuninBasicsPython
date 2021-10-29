from itertools import zip_longest
import sys
import json

users, hobby, out = sys.argv[1:]
with open(users, encoding='utf-8') as users:
    with open(hobby, encoding='utf-8') as hobbies:
        if sum(1 for user in users) < sum(1 for hobby in hobbies):
            exit(1)
        else:
            users.seek(0)
            hobbies.seek(0)
            my_dict = {user.replace(',', ' ').replace('\n', ''): hobby.replace(',', ', ').replace('\n', '') \
                if hobby is not None else hobby for user, hobby in zip_longest(users, hobbies)}

with open(out, 'w', encoding='utf-8') as f:
    json.dump(my_dict, f, ensure_ascii=False)
