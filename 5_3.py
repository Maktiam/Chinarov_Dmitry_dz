from itertools import zip_longest, islice

tutors = ['Иван', 'Анастасия', 'Петр', 'Сергей','Дмитрий', 'Борис', 'Елена']
klasses = ['9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А']


my_gen = ((tutors, klasses) for tutors, klasses in zip_longest(tutors, klasses, fillvalue=None))

print(*islice(my_gen, len(tutors)), sep='\n')