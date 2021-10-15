from random import choice


def get_jokes(count, var=True):
    """
    Print random jokes.
    :count: number of jokes
    :var=True: coincidences of word in jokes
    """
    i = 0
    nouns = ['автомобиль', 'лес', 'огонь', 'город', 'дом']
    adverbs = ['сегодня', 'вчера', 'завтра', 'позавчера', 'ночью']
    adjectives = ['веселый', 'яркий', 'зеленый', 'утопичный', 'мягкий']
    if var:
        while i != count:
            joke = [choice(nouns), choice(adverbs), choice(adjectives)]
            print(joke)
            i += 1
    else:
        nouns_1, adverbs_1, adjectives_1 = nouns.copy(), adverbs.copy(), adjectives.copy()
        try:
            while i != count:
                noun, adverb, adjective = choice(nouns_1), choice(adverbs_1), choice(adjectives_1)
                nouns_1.remove(noun), adverbs_1.remove(adverb), adjectives_1.remove(adjective)
                print([noun, adverb, adjective])
                i += 1
        except IndexError:
            print('Возможно не больше 5 шуток. Держите 5 шуток!')


get_jokes(7, False)
