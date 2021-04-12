# coding: utf-8
import random

def menu(hardness = 1, win = 0):
    errorText = 'Du skrev inte in ett heltal mellan dom tillåtna värderna '
    print('--------------')
    if win == 'L':
        print('Sorry, you lost!')    
    print('Start       (1)')
    print('Difficulty  (2)')
    print('Exit        (3)')
    while True:
        try:
            menuSelect = int(input('Skriv in vilket meny alternativ du vill välja (1, 2, eller 3): '))
            if menuSelect == 1:
                fieldMaker(hardness)
            elif menuSelect == 2:
                difficulty()
            elif menuSelect == 3:
                return            
            break
        except ValueError:
            print(errorText)      

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

    mapMaker(hardness, fullList)
    
def mapMaker(hardness, fullList):
    playerMap = [[], [], [], [], [], [], [], [], [], []]
    if hardness == 1:
        for i in range(0, 10):
            for k in range(0, 10):
                playerMap[i].append('#')
    mineHub(hardness, playerMap, fullList)

def mapPrint(hardness, playerMap):
    if hardness == 1:
        easyNumber = ['0','1','2','3','4','5','6','7','8','9']
        print(' ',' '.join(easyNumber))
        for l in range(0, 10):
            print(l, ' '.join(playerMap[l]))
            
def mineHub(hardness, playerMap, fullList):
    mineMap = mapPrint(hardness, playerMap)
    playerInput = playerChoice(hardness, fullList)
    mapUpdate = mapReveal(playerInput, playerMap, fullList)
    mineMap = mapPrint(hardness, playerMap)
        
    
def playerChoice(hardness, fullList):
    if hardness == 1:
        print("Skriv in positionen separerad av ett mellanslag (x y), eller 'lämna' för att lämna")
        print("Du kan också flagga en position genom att skriva 'flagga x y'")
        while True:
            try:
                playerInput = input("Skriv här vilken position du vill visa eller flagga: ")
                playerInput = playerInput.split(" ")
                if playerInput[0] == 'flagga' and playerMap[int(playerInput[0])][int(playerInput[1])] == '#':
                    mark = 1
                    return playerInput
                elif playerMap[int(playerInput[0])][int(playerInput[1])] == '#':
                    mark = 0
                    return playerInput
                else:
                    int('y')
            except (ValueError, IndexError): # Skickar denna felkod ifall användaren inte ger ut två heltal som värde.
                print("Oops.. Du skrev inte in en posision innom kartan.")

def mapReveal(playerInput, playerMap, fullList):
    if playerInput[0] == 'flagga' and playerMap[int(playerInput[1])][int(playerInput[2])] != int:
        playerMap[int(playerInput[1])][int(playerInput[2])] = '¤'
        return playerMap
    else:
        if fullList[int(playerInput[0])][int(playerInput[1])] == 'x':
            win = 'L'
            menu(1, win)
        playerMap[int(playerInput[0])][int(playerInput[1])] = str(fullList[int(playerInput[0])][int(playerInput[1])])

    

menu()