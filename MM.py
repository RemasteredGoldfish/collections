import random

blue = 0
yellow = 0
green = 0
red = 0

color = int(input('how much m&m do you want?'))
for i in range(color):
    x = random.randint(1,4)
    if x in [1]:
        blue = blue + 1
    if x in [2]:
        yellow = yellow + 1
    if x in [3]:
        red = red + 1
    if x in [4]:
        green = green + 1


sortmm = [{"color":"blue","total":blue},
{"color":"yellow","total":yellow},
{"color":"green","total":green},
{"color":"red","total":red}]
print('sack with: ')
for x in range(4):
    i = sortmm[x]['total']
    m = sortmm[x]['color']
    print('the color', m ,'got', i ,'m&m')