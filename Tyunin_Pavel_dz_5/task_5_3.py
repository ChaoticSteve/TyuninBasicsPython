from itertools import zip_longest

tutors = ['Иван', 'Анастасия', 'Петр', 'Сергей', 'Дмитрий', 'Борис', 'Елена']
klasses = ['9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А']

tutors_gen = (tutor_klass for tutor_klass in zip_longest(tutors, klasses[:len(tutors)]))
print(type(tutors_gen))
print(type(next(tutors_gen)))
try:
    i = 0
    while i != len(tutors):
        print(next(tutors_gen))
        i += 1
except StopIteration:
    print('Конец генератора')
