from random import choice, randrange


nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]

def some_jokes(n,repeat=False):
    no, adv, adj = nouns.copy(), adverbs.copy(), adjectives.copy()
    jokes = []
    list_min = min(no, adv, adj)
    while n and len(list_min):
        number = randrange(len(list_min))
        if repeat:
            jokes.append(f"{no.pop(number)} {adv.pop(number)} {adj.pop(number)}")
        else:
            jokes.append(f"{choice(nouns)} {choice(adverbs)} {choice(adjectives)}")
        n += 1
    return jokes

print(some_jokes(5, True))