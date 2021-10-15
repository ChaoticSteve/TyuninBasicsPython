def thesaurus_adv(*names):
    my_list = []
    my_dict = {}
    my_dict_2 = {}
    for name in names:
        my_list.append(name.split(' '))
    for name in my_list:
        if name[1][0] not in my_dict:
            my_dict[name[1][0]] = [name]
        else:
            my_dict[name[1][0]].append(name)
    for key in my_dict:
        for name in my_dict[key]:
            if name[0][0] not in my_dict_2:
                my_dict_2[name[0][0]] = [' '.join(name)]
            else:
                my_dict_2[name[0][0]].append(' '.join(name))
        my_dict[key] = my_dict_2.copy()
        my_dict_2.clear()
    return my_dict


print(thesaurus_adv('Иван Сергеев', 'Инна Серова', 'Петр Алексеев', 'Илья Иванов', 'Анна Савельева'))
