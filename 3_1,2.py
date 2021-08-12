
def num_translate():
    number = input('Введите число на английском: ')
    if number.istitle():
        print(numbers.get(number.lower()).title())
    else:
        print(numbers.get(number))


numbers = {
    'one': 'один',
    'two': 'два',
    'three': 'три',
    'four': 'четыре',
    'five': 'пять',
    'six': 'шесть',
    'seven': 'семь',
    'eight': 'восемь',
    'nine': 'девять',
    'ten': 'десять',
}

num_translate()