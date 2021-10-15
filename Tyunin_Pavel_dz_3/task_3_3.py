def thesaurus(*names):
    staff = {}
    for name in names:
        if name[0] not in staff:
            staff[name[0]] = [name]
        else:
            staff[name[0]].append(name)
    return staff


print(thesaurus('Иван', 'Мария', 'Петр', 'Илья'))

# staff = {}
# letter = 'B'
# name = 'Bob'
# staff[letter] = [name]
# print(staff)
# name_2 = 'Bib'
# staff[letter].append(name_2)
# print(staff)
