Alledagen = ['Ma', 'Di', 'Wo', 'Do', 'Vr', 'Za', 'Zo']
print(Alledagen[:]) #Alle dagen
print(Alledagen[0:5]) #Werkdagen
print(Alledagen[5:7]) #Weekend

Alledagen.reverse()

print(Alledagen[:]) #Alle dagen
print(Alledagen[2:7]) #Werkdagen
print(Alledagen[0:2]) #Weekend

print('=======================================================================')

Listone = [1,2,3,4,5,6,7,8,9,10]
Listtwo = [2,4,6,8,10,12,14,16,18,20]

def optellen(Listone, Listtwo):
    for i in range(len(Listone)):
        print(Listone[i], '+', Listtwo[i], '=', Listone[i] + Listtwo[i])
optellen(Listone, Listtwo)
print('')
def optellen(Listone, Listtwo):
    for i in range(len(Listone)):
        print(Listone[i], '-', Listtwo[i], '=', Listone[i] - Listtwo[i])
optellen(Listone, Listtwo)
print('')
def optellen(Listone, Listtwo):
    for i in range(len(Listone)):
        print(Listone[i], '*', Listtwo[i], '=', Listone[i] * Listtwo[i])
optellen(Listone, Listtwo)
print('')
def optellen(Listone, Listtwo):
    for i in range(len(Listone)):
        print(Listone[i], '/', Listtwo[i], '=', Listone[i] / Listtwo[i])
optellen(Listone, Listtwo)

print('=======================================================================')

def spel():
    import random
    for i in range(3):
        spellist = ["Yathzee", "Bridge", "Poker", "Pesten", "Mens erger je niet","Cluedo"]
        print(random.choice(spellist))

spel()
