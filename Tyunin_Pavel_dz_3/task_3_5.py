from random import choice


def get_jokes(count):
    i = 0
    nouns = ['автомобиль', 'лес', 'огонь', 'город', 'дом']
    adverbs = ['сегодня', 'вчера', 'завтра', 'позавчера', 'ночью']
    adjectives = ['веселый', 'яркий', 'зеленый', 'утопичный', 'мягкий']
    while i != count:
        joke = [choice(nouns), choice(adverbs), choice(adjectives)]
        print(joke)
        i += 1


get_jokes(4)
