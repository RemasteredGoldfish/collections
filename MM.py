import random

sack = []

def datatype(sack):
    aantal = int(input('hoeveel wil je?'))
    color = ['orange', 'blue', 'green', 'brown']
    for i in range(aantal):
        x = random.choice(color)
        sack.append(x)
    return sack, color

def Dictionary(sack):
    DictionaryBag = {
    'orange' : '0',
    'blue'   : '0',
    'green'  : '0',
    'brown'  : '0'
    }

    aantal = int(input('Hoeveel M&M wil je?'))
    for x in range(aantal):
        color = random.choice(list(sack))
        print(color)
        sack[color] += 1
    print (sack)
    return DictionaryBag

Dictionary(sack)

