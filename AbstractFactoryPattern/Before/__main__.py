from factories.gm import GMMega, GMShiteo
from factories.ford import FordFiesta, FordMustang
from random import randint

makers = ('gm','ford')
editions = ('Economy', 'Sport')
maker = makers[randint(0,1)]
edition = editions[randint(0,1)]

print(maker)
print(edition)

if maker == 'gm':
    if edition == 'Economy':
        car = 'GMShiteo'
    elif edition == 'Sport':
        car = 'GMMega'
    else:
        raise ValueError('Unknown car')
elif maker == 'ford':
    if edition == 'Economy':
        car = 'FordFiesta'
    elif edition == 'Sport':
        car = 'FordMustang'
    else:
        raise ValueError('Unknown car')