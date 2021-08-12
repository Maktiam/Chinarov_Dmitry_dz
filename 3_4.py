
def thesaurus_adv(*args):
    namelist = list(map(str, args))
    dict_surnames = {}
    dict_main = {}
    for name in namelist:
        surname = name.split(' ')[-1].title()
        first_letter_surname = surname[0]
        dict_surnames[first_letter_surname] = dict_surnames.get(first_letter_surname, []) + [name]
    for namelist in dict_surnames.values():
        dict_names = {}
        for name in namelist:
            surname = name.split(' ')[-1].title()
            first_letter_surname = surname[0]
            first_latter = name[0]
            dict_names[first_latter] = sorted(dict_names.get(first_latter, []) + [name])
            dict_main[first_letter_surname] = dict_main.get(first_letter_surname, dict_names)
    return print(dict(sorted(dict_main.items())))

thesaurus_adv("Алексей Иванов", "Ольга Сергеева", "Михаил Мишустин", "Наталья Власова", "Владимир Кузнецов")