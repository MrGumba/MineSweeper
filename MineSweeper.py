# coding: utf-8
import random

''' Skälvaste menyn till programet där användaren kan starta, ändra svårighetsgrad eller lämna'''
def menu(hardness = 1, win = 0):
    errorText = 'Du skrev inte in ett heltal mellan dom tillåtna värderna '
    print('--------------')
    if win == 'L': # När spelet slutas returneras 'L' eller 'W' beronde på om spelaren vann eller förlorade
        print('Nep, där var en bomb du förlorade!')
    elif win == 'W':
        print('Yippi du tog bort allt!')
    elif win == 'dnf': # Detta värde kommer ifall användaren lämnade mitt i ett spel.
        print("Det var synd att du ville lämna.. skriv '3' ifall du vill lämna helt")
        
    print('Start            (1)')
    print('Svårgighetsgrad  (2)')
    print('Lämna            (3)')
    while True: # Loopar tills ett correkt värde har angäts
        try:
            menuSelect = int(input('Skriv in vilket meny alternativ du vill välja (1, 2, eller 3): '))
            if menuSelect == 1:
                fullListMaker(hardness) # Startar igång resten av pogrammet och leder vidare.
            elif menuSelect == 2:
                difficulty() # Difficulty är där man ändrar svårigheten av spelet
            elif menuSelect == 3:
                return  # Ifall man ångrar sig och vill lämna
            else:
                print(errorText) # detta printas ut ifall ingen av dom tidigare värderna blev angätt. 
        except ValueError:
            print(errorText)  # Detta printas ut ifall användaren angav inte en siffra.

''' Här kan användaren välja svårighets graden detta sparas för att sedan programet ska veta vilken svårighetsgrad användaren kör på'''
def difficulty():
    print('Lätt   (1)')
    print('Medelsvårt (2)')
    print('Svårt  (3)')
    while True: # Loopar tills ett korekt värde har angäts 
        try:
            difficultySelect = int(input("Välj en av svårighets graderna genom att skriva '1' '2' eller '3': "))
            if difficultySelect > 0 and difficultySelect < 4: # Kollar att användaren skriver in ett värde mellan 1 och 3
                break
            else:
                print(errorText) # Ifall användaren inte angav ett värde innom den frågade arean
        except ValueError:
            print(errorText)
    menu(difficultySelect) # Hoppar tillbaka till menyn där användaren kan nu starta spelet lämna eller ångra och välja en annan svårighetsgrad

'''Denna funktion skapar hela tomma listan av spelplanen användaren ser och riktiga spelplanen där den kollar efter vilken svårighets grad användaren ville köra'''
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
    fieldMaker(hardness, fullList, playerMap) # Går sedan vidare till denna funktion som skapar fältet

'''Denna funktion skapar spelfältet samt lägger ut bomberna för spelfältet '''
def fieldMaker(hardness, fullList, playerMap):
    for i in range(0, len(fullList)): # Denna loop lägger ut alla noller och skappar fältet beronde på svårighets graden tex 10x10 alltså 100 noller
        for k in range(0, len(fullList)):
            fullList[i].append(0)
    if hardness == 1: # Detta kollar svårighets graden och hur många bomber som ska finnas för den svårighets graden.
        bombs = 10 
    elif hardness == 2: # Detta kollar svårighets graden och hur många bomber som ska finnas för den svårighets graden.
        bombs = 40
    elif hardness == 3: # Detta kollar svårighets graden och hur många bomber som ska finnas för den svårighets graden.
        bombs = 99
    p = 0
    for j in range(0, bombs + p): # Denna funktion slumpar in bomberna någon stans i listan
        randomList = random.randint(0, len(fullList) - 1) # För var i den ytre listan
        randomMine = random.randint(0, len(fullList) - 1) # för var i den inre listan
        if fullList[randomList][randomMine] != 'x': # Kollar så att stället är inte en bomb
            fullList[randomList][randomMine] = 'x'
        else: # Ifall det var en bomb så får den loopa om igen så att man inte får förlite bomber
            p += 1
    
    bombCalculator(hardness, fullList, playerMap) # Kallar till nästa funktion som är för att räkna ut siffrorna som ska vara runt alla bomber

''' Räknar ut vilka numer som ska vara runt en bomb genom att +1 alla siffror runt en bomb'''
def bombCalculator(hardness, fullList, playerMap):
    for i in range(0, len(fullList)): # Kollar igenom varje ytre lista
        back = 0
        front = 3
        if i == 0: # Ifall det är den första listan ändras värdet så att den inte söker utanför listorna
            back = 1
        elif i == len(fullList) - 1: # Ifall den är på den sista listan så ändras värdet så att den inte söker utanför listorna
            front = 2        
        for k in range(0, len(fullList)): # Kollar igenom alla värden i den inre listan
            if fullList[i][k] == 'x': # Ifall den hittar en bomb (markerat som 'x') så gör den följande.
                for j in range(back, front):  # Kollar vänster höger och mitt så länge inget spesefikt värde angätts.
                    if k - 1 > -1 and fullList[i - 1 + j][k - 1] != 'x': # Kollar/ändrar vänster 
                        fullList[i - 1 + j][k - 1] += 1
                    if fullList[i - 1 + j][k] != 'x': # Kollar/ändrar mitten
                        fullList[i - 1 + j][k] += 1                     
                    if k + 1 < len(fullList) and fullList[i - 1 + j][k + 1] != 'x': # Kollar/Ändrar höger
                        fullList[i - 1 + j][k + 1] += 1
    mapMaker(hardness, fullList, playerMap) # Kallar till nästa funktion för att skapa kartan spelaren ser

''' Denna funktion skapar kartan spelaren ser samt lägger in värden för hur många bomber som finns och hur många tomma utrymen som är kvar '''
def mapMaker(hardness, fullList, playerMap):
    
    for i in range(0, len(fullList)): # Detta lägger in ett '#' för varje utryme som ska vara på kartan som ifall kartan är 10x10 har den 100st '#'
        for k in range(0, len(fullList)):
            playerMap[i].append('#')
    
    if hardness == 1: # Bomberna och toma utrymet för denna svårighetsgrad
        freeSpace = [90]
        bombCount = [10]
    if hardness == 2: # Bomberna och toma utrymet för denna svårighetsgrad
        freeSpace = [284]
        bombCount = [40]
    if hardness == 3: # Bomberna och toma utrymet för denna svårighetsgrad
        freeSpace = [477]
        bombCount = [99]        
    mineHub(hardness, playerMap, fullList, freeSpace, bombCount) # Startar igång mineHub som är hubben för hela spelet

'''mineHub är hubben som kallar till funktionerna som aktivts behövs medans man köra spelet'''
def mineHub(hardness, playerMap, fullList, freeSpace, bombCount):
    while freeSpace != 0: # Kollar så spelet är inte redan över
        mineMap = mapPrint(hardness, playerMap, bombCount, fullList) # Kallar till mapPrint för att visa kartan för spelaren
        playerInput = playerChoice(hardness, fullList, playerMap) # Kallar till playerChoice för att få veta vad användaren vill göra 
        mapUpdate = mapReveal(playerInput, playerMap, fullList, freeSpace, bombCount) # Kallar till mapUpdate som ändrar till kartan efter användarens input
    if freeSpace[0] == 0: # Kollar ifall det är inga utrymen kvar där man vinner ifall inga är kvar (som inte är bomber)
        menu(1, 'W')
    
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
    
def playerChoice(hardness, fullList, playerMap):
    print("Skriv in positionen separerad av ett mellanslag 'x y', eller 'lämna' för att lämna")
    print("Du kan också flagga en position genom att skriva 'f x y' eller 'of x y' för att ta bort en flagga")
    while True:
        try:
            playerInput = input("Skriv här vilken position du vill visa eller flagga: ")
            playerInput = playerInput.split(" ")
            if playerInput[0] == 'f' and playerMap[int(playerInput[2])][int(playerInput[1])] == '#':
                return playerInput
            elif playerInput[0] == 'of' and playerMap[int(playerInput[2])][int(playerInput[1])] == '¤':
                return playerInput
            elif playerInput[0] == 'lämna':
                menu(1, 'dnf')            
            elif playerMap[int(playerInput[1])][int(playerInput[0])] == '#':
                return playerInput
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
        freeSpace[0] -= 1   

def zeroChecker(playerInput, freeSpace, playerMap, fullList, zeroFinderX = 0, zeroFinderY = 0):
    back = 0
    front = 3            
    if int(playerInput[1]) + zeroFinderY == 0:
        back = 1
    elif int(playerInput[1]) + zeroFinderY == len(playerMap) - 1:
        front = 2        
    for j in range(back, front):
        if int(playerInput[0]) - 1 + zeroFinderX > -1 and playerMap[int(playerInput[1]) - 1 + j + zeroFinderY][int(playerInput[0]) - 1 + zeroFinderX] == '#': 
            holder = str(fullList[int(playerInput[1]) - 1 + j + zeroFinderY][int(playerInput[0]) - 1 + zeroFinderX])
            playerMap[int(playerInput[1]) - 1 + j + zeroFinderY][int(playerInput[0]) - 1 + zeroFinderX] = holder
            freeSpace[0] -= 1
            if playerMap[int(playerInput[1]) - 1 + j + zeroFinderY][int(playerInput[0]) - 1 + zeroFinderX] == '0':
                zeroChecker(playerInput, freeSpace, playerMap, fullList, -1 + zeroFinderX, -1 + j + zeroFinderY)
                
        if playerMap[int(playerInput[1]) - 1 + j + zeroFinderY][int(playerInput[0]) + zeroFinderX] == '#':
            holder = str(fullList[int(playerInput[1]) - 1 + j + zeroFinderY][int(playerInput[0]) + zeroFinderX])   
            playerMap[int(playerInput[1]) - 1 + j + zeroFinderY][int(playerInput[0]) + zeroFinderX] = holder
            freeSpace[0] -= 1
            if playerMap[int(playerInput[1]) - 1 + j + zeroFinderY][int(playerInput[0]) + zeroFinderX] == '0':
                zeroChecker(playerInput, freeSpace, playerMap, fullList, 0 + zeroFinderX, -1 + j + zeroFinderY)
                
        if int(playerInput[0]) + zeroFinderX + 1 < len(fullList) and playerMap[int(playerInput[1]) - 1 + j + zeroFinderY][int(playerInput[0]) + 1 + zeroFinderX] == '#':
            holder = str(fullList[int(playerInput[1]) - 1 + j + zeroFinderY][int(playerInput[0]) + 1 + zeroFinderX])
            playerMap[int(playerInput[1]) - 1 + j + zeroFinderY][int(playerInput[0]) + 1 + zeroFinderX] = holder
            freeSpace[0] -= 1
            if playerMap[int(playerInput[1]) - 1 + j + zeroFinderY][int(playerInput[0]) + 1 + zeroFinderX] == '0':
                zeroChecker(playerInput, freeSpace, playerMap, fullList, 1 + zeroFinderX, -1 + j + zeroFinderY)
menu()