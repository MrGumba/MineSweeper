# coding: utf-8
import random

def menu(hardness = 1):
    errorText = 'Du skrev inte in ett heltal mellan dom tillåtna värderna '
    print('--------------')
    print('Start       (1)')
    print('Difficulty  (2)')
    print('Exit        (3)')
    while True:
        try:
            menuSelect = int(input('Skriv in vilket meny alternativ du vill välja (1, 2, eller 3): '))
            if menuSelect == 1:
                mineSweeper()
            elif menuSelect == 2:
                difficulty()
            elif menuSelect == 3:
                return            
            break
        except ValueError:
            print(errorText)      

def mineSweeper(hardness = 1):
    fieldMaker(hardness)

def difficulty():
    print('easy (1)')
    while True:
        try:
            difficultySelect = int(input('Välj en av svårighets graderna genom att skriva (1): '))
            if difficultySelect > 0 and difficultySelect < 2:
                break
        except ValueError:
            print(errorText)
    menu(difficultySelect)
        
def fieldMaker(hardness):
    fullList = [[], [], [], [], [], [], [], [], [], []]
    if hardness == 1:
        for i in range(0, 10):
            for k in range(0, 10):
                fullList[i].append(0)
        p = 0
        for j in range(0, 10 + p):
            randomList = random.randint(0, 9)
            randomMine = random.randint(0, 9)
            if fullList[randomList][randomMine] != 'x':
                fullList[randomList][randomMine] = 'x'
            else: 
                p += 1
    
    print(fullList)
    for i in range(0, len(fullList)):
        back = 0
        front = 3
        if i == 0:
            back = 1
        elif i == len(fullList) - 1:
            front = 2        
            
        for k in range(0, len(fullList)):
            if fullList[i][k] == 'x':             
                for j in range(back, front):
                    if k - 1 > -1 and fullList[i - 1 + j][k - 1] != 'x':
                        fullList[i - 1 + j][k - 1] += 1
                    if fullList[i - 1 + j][k] != 'x': 
                        fullList[i - 1 + j][k] += 1                     
                    if k + 1 < 10 and fullList[i - 1 + j][k + 1] != 'x':
                        fullList[i - 1 + j][k + 1] += 1 
    print(fullList)

            
    mapMaker(hardness, fullList)
    
def mapMaker(hardness, fullList):
    playerMap = [[], [], [], [], [], [], [], [], [], []]
    if hardness == 1:
        for i in range(0, 10):
            for k in range(0, 10):
                playerMap[i].append('#')
    mapPrint(hardness, playerMap)

def mapPrint(hardness, playerMap):
    if hardness == 1:
        esayNumber = ['0','1','2','3','4','5','6','7','8','9']
        print(' ',' '.join(esayNumber))
        for l in range(0, 10):
            print(l, ' '.join(playerMap[l]))
    

    

    

menu()