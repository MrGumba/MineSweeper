# coding: utf-8
import random

def menu(hardness = 1, win = 0):
    errorText = 'Du skrev inte in ett heltal mellan dom tillåtna värderna '
    print('--------------')
    if win == 'L':
        print('Nep, där var en bomb du förlorade!')
    if win == 'W':
        print('Yippi du tog bort allt!')
    print('Start            (1)')
    print('Svårgighetsgrad  (2)')
    print('Lämna            (3)')
    while True:
        try:
            menuSelect = int(input('Skriv in vilket meny alternativ du vill välja (1, 2, eller 3): '))
            if menuSelect == 1:
                fullListMaker(hardness)
            elif menuSelect == 2:
                difficulty()
            elif menuSelect == 3:
                return
            else:
                print(errorText) 
        except ValueError:
            print(errorText)      

def difficulty():
    print('Lätt   (1)')
    print('Medelsvårt (2)')
    print('Svårt  (3)')
    while True:
        try:
            difficultySelect = int(input("Välj en av svårighets graderna genom att skriva '1' '2' eller '3': "))
            if difficultySelect > 0 and difficultySelect < 4:
                break
            else:
                print(errorText)
        except ValueError:
            print(errorText)
    menu(difficultySelect)

def fullListMaker(hardness):
    if hardness == 1:
        fullList = [[], [], [], [], [], [], [], [], [], []] # 10x10 fält med 10 bomber
        playerMap = [[], [], [], [], [], [], [], [], [], []]
    elif hardness == 2:
        fullList = [[], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []] # 18x18 fält med 40 bomber
        playerMap = [[], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []] 
    elif hardness == 3:
        fullList = [[], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []] # 24x24 fält med 99 bomber
        playerMap = [[], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []]
    fieldMaker(hardness, fullList, playerMap)

def fieldMaker(hardness, fullList, playerMap):
    for i in range(0, len(fullList)):
        for k in range(0, len(fullList)):
            fullList[i].append(0)
    if hardness == 1:
        bombs = 10
    elif hardness == 2:
        bombs = 40
    elif hardness == 3:
        bombs = 99
    p = 0
    for j in range(0, bombs + p):
        randomList = random.randint(0, len(fullList) - 1)
        randomMine = random.randint(0, len(fullList) - 1)
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
                    if k + 1 < len(fullList) and fullList[i - 1 + j][k + 1] != 'x':
                        fullList[i - 1 + j][k + 1] += 1 

    mapMaker(hardness, fullList, playerMap)
    
def mapMaker(hardness, fullList, playerMap):
    
    for i in range(0, len(fullList)):
        for k in range(0, len(fullList)):
            playerMap[i].append('#')
    
    if hardness == 1:
        freeSpace = [90]
        bombCount = [10]
    if hardness == 2:
        freeSpace = [284]
        bombCount = [40]
    if hardness == 3:
        freeSpace = [477]
        bombCount = [99]        
    mineHub(hardness, playerMap, fullList, freeSpace, bombCount)

def mapPrint(hardness, playerMap, bombCount, fullList):
    easyNumber = []
    for i in range(0, len(fullList)):
        if i < 10:
            easyNumber.append('0' + str(i))
        else:
            easyNumber.append(str(i))
    print(' ',' '.join(easyNumber))
    for l in range(0, len(fullList)):
        if l < 10:
            print('0' + str(l), '  '.join(playerMap[l]))
        elif l > 10:
            print(l, '  '.join(playerMap[l]))
    print("Det är",bombCount[0],"Bomber kvar")
            
def mineHub(hardness, playerMap, fullList, freeSpace, bombCount):
    while freeSpace != 0:
        mineMap = mapPrint(hardness, playerMap, bombCount, fullList)
        playerInput = playerChoice(hardness, fullList, playerMap)
        mapUpdate = mapReveal(playerInput, playerMap, fullList, freeSpace, bombCount)
    if freeSpace[0] == 0:
        menu(1, 'W')
    
        
    
def playerChoice(hardness, fullList, playerMap):
    print("Skriv in positionen separerad av ett mellanslag 'x y', eller 'lämna' för att lämna")
    print("Du kan också flagga en position genom att skriva 'f x y' eller 'of x y' för att ta bort en flagga")
    while True:
        try:
            playerInput = input("Skriv här vilken position du vill visa eller flagga: ")
            playerInput = playerInput.split(" ")
            if playerInput[0] == 'flagga' and playerMap[int(playerInput[2])][int(playerInput[1])] == '#':
                return playerInput
            elif playerInput[0] == 'oflagga' and playerMap[int(playerInput[2])][int(playerInput[1])] == '¤':
                return playerInput
            elif playerMap[int(playerInput[1])][int(playerInput[0])] == '#':
                return playerInput
            elif playerInput[0] == 'lämna':
                break
            else:
                int('y')
        except (ValueError, IndexError): # Skickar denna felkod ifall användaren inte ger ut två heltal som värde.
            print("Oops.. Du skrev inte in en posision innom kartan.")

def mapReveal(playerInput, playerMap, fullList, freeSpace, bombCount):
    if playerInput[0] == 'f':
        playerMap[int(playerInput[2])][int(playerInput[1])] = '¤'
        bombCount[0] -= 1
    elif playerInput[0] == 'of':
        playerMap[int(playerInput[2])][int(playerInput[1])] = '#'
    elif fullList[int(playerInput[1])][int(playerInput[0])] == 'x':
        win = 'L'
        menu(1, win)
         
    elif fullList[int(playerInput[1])][int(playerInput[0])] == 0:
        zeroChecker(playerInput, freeSpace, playerMap, fullList)
    else: 
        playerMap[int(playerInput[1])][int(playerInput[0])] = str(fullList[int(playerInput[1])][int(playerInput[0])])
        freeSpace[0] = -1   

def zeroChecker(playerInput, freeSpace, playerMap, fullList, zeroFinderX = 0, zeroFinderY = 0):
    back = 0
    front = 3            
    if int(playerInput[1]) + zeroFinderY == 0:
        back = 1
    elif int(playerInput[1]) + zeroFinderY == len(playerMap) - 1:
        front = 2        
    for j in range(back, front):
        if int(playerInput[0]) - 1 + zeroFinderX > -1:
            playerMap[int(playerInput[1]) - 1 + j + zeroFinderY][int(playerInput[0]) - 1 + zeroFinderX] = str(fullList[int(playerInput[1]) - 1 + j + zeroFinderY][int(playerInput[0]) - 1 + zeroFinderX])
            freeSpace[0] -= 1
            if playerMap[int(playerInput[1]) - 1 + j + zeroFinderY][int(playerInput[0]) - 1 + zeroFinderX] == '0':
                zeroChecker(playerInput, freeSpace, playerMap, fullList, -1 + zeroFinderX, -1 + j + zeroFinderY)
        if playerMap[int(playerInput[1]) - 1 + j + zeroFinderY][int(playerInput[0]) + zeroFinderX] == '#':
            playerMap[int(playerInput[1]) - 1 + j + zeroFinderY][int(playerInput[0]) + zeroFinderX] = str(fullList[int(playerInput[1]) - 1 + j + zeroFinderY][int(playerInput[0]) + zeroFinderX])                    
            freeSpace[0] -= 1
            if playerMap[int(playerInput[1]) - 1 + j + zeroFinderY][int(playerInput[0]) + zeroFinderX] == '0':
                zeroChecker(playerInput, freeSpace, playerMap, fullList, 0 + zeroFinderX, -1 + j + zeroFinderY)
        if int(playerInput[0]) + zeroFinderX + 1 < len(fullList) and playerMap[int(playerInput[1]) - 1 + j + zeroFinderY][int(playerInput[0]) + 1 + zeroFinderX] == '#':
            playerMap[int(playerInput[1]) - 1 + j + zeroFinderY][int(playerInput[0]) + 1 + zeroFinderX] = str(fullList[int(playerInput[1]) - 1 + j + zeroFinderY][int(playerInput[0]) + 1 + zeroFinderX])  
            freeSpace[0] -= 1
            if playerMap[int(playerInput[1]) - 1 + j + zeroFinderY][int(playerInput[0]) + 1 + zeroFinderX] == '0':
                zeroChecker(playerInput, freeSpace, playerMap, fullList, 1 + zeroFinderX, -1 + j + zeroFinderY)
menu()