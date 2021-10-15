def thesaurus(names):
    my_dict_2 = {}
    for name in names:
        if name[0][0] not in my_dict_2:
            my_dict_2[name[0][0]] = [' '.join(name)]
        else:
            my_dict_2[name[0][0]].append(' '.join(name))
    return my_dict_2


def thesaurus_adv(*names):
    my_dict = {}
    for name in (name.split(' ') for name in names):
        if name[1][0] not in my_dict:
            my_dict[name[1][0]] = [name]
        else:
            my_dict[name[1][0]].append(name)
    for key in my_dict:
        my_dict[key] = thesaurus(my_dict[key])
    return my_dict


print(thesaurus_adv('Иван Сергеев', 'Инна Серова', 'Петр Алексеев', 'Илья Иванов', 'Анна Савельева'))
