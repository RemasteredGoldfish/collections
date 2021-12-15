Alledagen = ['Ma', 'Di', 'Wo', 'Do', 'Vr', 'Za', 'Zo']
print(Alledagen[:]) #Alle dagen
print(Alledagen[0:5]) #Werkdagen
print(Alledagen[5:7]) #Weekend

Alledagen.reverse()

print(Alledagen[:]) #Alle dagen
print(Alledagen[2:7]) #Werkdagen
print(Alledagen[0:2]) #Weekend

print('=======================================================================')

List1 = [1,2,3,4,5,6,7,8,9,10]
List2 = [2,4,6,8,10,12,14,16,18,20]

def addition(number1, number2):
    result = number1 + number2
    return result

def subtraction(number1, number2):
    result = number1 - number2
    return result


def multiplication(number1, number2):
    result = number1 * number2
    return result

def division(number1, number2):
    result = number1 / number2
    return result

def increment(number):
    result = number + 1
    return result

def decrement(number):
    result = number - 1
    return result



for teller in range(1,11):

    result = addition(List1[0],List2[0])
    print(List1[0], '+', List2[0], '=', result)
# for teller in range(1,11):
#     print(List1[0,9], 'x', List2[0,9], '=')
# print()


