def thesaurus(*names):
    staff = {}
    for name in names:
        if name[0] not in staff:
            staff[name[0]] = [name]
        else:
            staff[name[0]].append(name)
    return staff


print(thesaurus('Иван', 'Мария', 'Петр', 'Илья'))
