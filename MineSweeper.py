# coding: utf-8
import random



''' Skälvaste menyn till programet där användaren kan starta, ändra svårighetsgrad eller lämna'''
def menu(hardness = 1, win = 0):
    errorText = 'Du skrev inte in ett heltal mellan dom tillåtna värderna '
    print('--------------')
    if win == 'L': # När spelet slutas returneras 'L' eller 'W' beronde på om spelaren vann eller förlorade.
        print('Nep, där var en bomb du förlorade!')
    elif win == 'W':
        print('Yippi du tog bort allt!')
    elif win == 'dnf': # Detta värde kommer ifall användaren lämnade mitt i ett spel.
        print("Det var synd att du ville lämna.. skriv '3' ifall du vill lämna helt")
        
    print('Start            (1)')
    print('Svårgighetsgrad  (2)')
    print('Lämna            (3)')
    while True: # Loopar tills ett correkt värde har angäts.
        try:
            menuSelect = int(input('Skriv in vilket meny alternativ du vill välja (1, 2, eller 3): '))
            if menuSelect == 1:
                fullListMaker(hardness) # Anropar fullListMaker som gör fulla listan som sedan startar igång resten av pogrammet.
            elif menuSelect == 2:
                difficulty() # Anropar Difficulty där man ändrar svårigheten av spelet.
            elif menuSelect == 3:
                exit()  # Ifall man ångrar sig och vill lämna.
            else:
                print(errorText) # detta printas ut ifall ingen av dom tidigare värderna blev angätt. 
        except ValueError:
            print(errorText)  # Detta printas ut ifall användaren angav inte en siffra.
            
            
            
''' Här kan användaren välja svårighets graden detta sparas för att sedan programet ska veta vilken svårighetsgrad användaren kör på'''
def difficulty():
    print('Lätt   (1)')
    print('Medelsvårt (2)')
    print('Svårt  (3)')
    while True: # Loopar tills ett korekt värde har angäts .
        try:
            difficultySelect = int(input("Välj en av svårighets graderna genom att skriva '1' '2' eller '3': "))
            if difficultySelect > 0 and difficultySelect < 4: # Kollar att användaren skriver in ett värde mellan 1 och 3.
                break
            else:
                print(errorText) # Ifall användaren inte angav ett värde innom den frågade arean.
        except ValueError:
            print(errorText)
    menu(difficultySelect) # Anropar menu för att hoppa tillbaka till menyn där användaren kan igen välja samma val som förut.



'''Denna funktion skapar hela tomma listan av spelplanen användaren ser och riktiga spelplanen där den kollar efter vilken svårighets grad användaren ville köra'''
def fullListMaker(hardness):
    if hardness == 1:
        fullList = [[], [], [], [], [], [], [], [], [], []] # 10x10 fält med 10 bomber.
        playerMap = [[], [], [], [], [], [], [], [], [], []]
    elif hardness == 2:
        fullList = [[], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []] # 18x18 fält med 40 bomber.
        playerMap = [[], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []] 
    elif hardness == 3:
        fullList = [[], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []] # 24x24 fält med 99 bomber.
        playerMap = [[], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []]
    fieldMaker(hardness, fullList, playerMap) # Anropar fieldMaker som skapar fältet med siffror. 



'''Denna funktion skapar spelfältet samt lägger ut bomberna för spelfältet '''
def fieldMaker(hardness, fullList, playerMap):
    for i in range(0, len(fullList)): # Denna loop lägger ut alla noller och skapar fältet beronde på svårighets graden tex 10x10 alltså 100 noller.
        for k in range(0, len(fullList)):
            fullList[i].append(0)
    if hardness == 1: # Detta kollar svårighets graden och hur många bomber som ska finnas för den svårighets graden.
        bombs = 10 
    elif hardness == 2: # Detta kollar svårighets graden och hur många bomber som ska finnas för den svårighets graden.
        bombs = 40
    elif hardness == 3: # Detta kollar svårighets graden och hur många bomber som ska finnas för den svårighets graden.
        bombs = 99
    p = 0
    for j in range(0, bombs + p): # Denna funktion slumpar in bomberna någon stans i listan.
        randomList = random.randint(0, len(fullList) - 1) # För var i den ytre listan.
        randomMine = random.randint(0, len(fullList) - 1) # för var i den inre listan.
        if fullList[randomList][randomMine] != 'x': # Kollar så att stället är inte en bomb.
            fullList[randomList][randomMine] = 'x'
        else: # Ifall det var en bomb så får den loopa om igen så att man inte får förlite bomber.
            p += 1
    
    bombCalculator(hardness, fullList, playerMap) # Anropar bombCalculator för att räkna ut siffrorna som ska vara runt alla bomber.



''' Räknar ut vilka numer som ska vara runt en bomb genom att +1 alla siffror runt en bomb'''
def bombCalculator(hardness, fullList, playerMap):
    for i in range(0, len(fullList)): # Kollar igenom varje ytre lista.
        back = 0
        front = 3
        if i == 0: # Ifall det är den första listan ändras värdet så att den inte söker utanför listorna.
            back = 1
        elif i == len(fullList) - 1: # Ifall den är på den sista listan så ändras värdet så att den inte söker utanför listorna.
            front = 2        
        for k in range(0, len(fullList)): # Kollar igenom alla värden i den inre listan.
            if fullList[i][k] == 'x': # Ifall den hittar en bomb (markerat som 'x') så gör den följande.
                for j in range(back, front):  # Kollar vänster höger och mitt så länge inget spesefikt värde angätts.
                    if k - 1 > -1 and fullList[i - 1 + j][k - 1] != 'x': # Kollar/ändrar vänster.
                        fullList[i - 1 + j][k - 1] += 1
                    if fullList[i - 1 + j][k] != 'x': # Kollar/ändrar mitten.
                        fullList[i - 1 + j][k] += 1                     
                    if k + 1 < len(fullList) and fullList[i - 1 + j][k + 1] != 'x': # Kollar/Ändrar höger.
                        fullList[i - 1 + j][k + 1] += 1
    mapMaker(hardness, fullList, playerMap) # Anropar mapMaker för att skapa kartan spelaren ser.



''' Denna funktion skapar kartan spelaren ser samt lägger in värden för hur många bomber som finns och hur många tomma utrymen som är kvar '''
def mapMaker(hardness, fullList, playerMap):
    
    for i in range(0, len(fullList)): # Detta lägger in ett '#' för varje utryme som ska vara på kartan som ifall kartan är 10x10 har den 100st '#'.
        for k in range(0, len(fullList)):
            playerMap[i].append('#')
    
    if hardness == 1: # Bomberna och toma utrymet för denna svårighetsgrad.
        freeSpace = [90]
        bombCount = [10]
    if hardness == 2: # Bomberna och toma utrymet för denna svårighetsgrad.
        freeSpace = [284]
        bombCount = [40]
    if hardness == 3: # Bomberna och toma utrymet för denna svårighetsgrad.
        freeSpace = [477]
        bombCount = [99]        
    mineHub(hardness, playerMap, fullList, freeSpace, bombCount) # Anropar mineHub som är hubben för hela spelet.




'''mineHub är hubben som Anropar funktionerna som aktivts behövs medans man köra spelet'''
def mineHub(hardness, playerMap, fullList, freeSpace, bombCount):
    while freeSpace[0] != 0: # Kollar så spelet är inte redan över.
        mapPrint(hardness, playerMap, bombCount, fullList) # Anropar mapPrint för att visa kartan för spelaren.
        playerInput = playerChoice(hardness, fullList, playerMap) # Anropar playerChoice för att få veta vad användaren vill göra. 
        mapReveal(playerInput, playerMap, fullList, freeSpace, bombCount) # Anropar mapReveal som ändrar till kartan efter användarens input.
    if freeSpace[0] == 0: # Kollar ifall det är inga utrymen kvar där man vinner ifall inga är kvar (som inte är bomber).
        menu(1, 'W') # Anropar menu för att gå till menyn med informationen att användaren har vunnit. 
    
    
'''MapPrint printar ut kartan som användaren ska se samt mängden bomber som finns. '''
def mapPrint(hardness, playerMap, bombCount, fullList):
    easyNumber = []
    for i in range(0, len(fullList)): # Skapar ett x led med nummer mellan 0 - längden av listan.
        if i < 10:
            easyNumber.append('0' + str(i)) # Ifall numret är under 10 så ska den lägga till en 0 så att tex 28 och 01 ska ta up samma utryme.
        else:
            easyNumber.append(str(i))
    print(' ',' '.join(easyNumber))
    
    for l in range(0, len(fullList)): # Printar ut rästen av listan för användaren med y numrerna 0 - längden av listan brevid kartan.
        if l < 10:
            print('0' + str(l), '  '.join(playerMap[l]))
        elif l > 10:
            print(l, '  '.join(playerMap[l]))
    print("Det är",bombCount[0],"Bomber kvar") # Printar hur många bomber som är kvar.
    
    
    
'''playerChoice är där användaren kan skriva in vad på kartan den vill visa/flagga/oflagga.'''
def playerChoice(hardness, fullList, playerMap):
    wall = '-------------------------------------' # Wall är tillför att göra det lätt för användaren att se vad som är nytt.
    print("Skriv in positionen separerad av ett mellanslag 'x y', eller 'lämna' för att lämna")
    print("Du kan också flagga en position genom att skriva 'f x y' eller 'of x y' för att ta bort en flagga")
    while True:
        try:
            playerInput = input("Skriv här vilken position du vill visa eller flagga: ")
            playerInput = playerInput.strip() # Tar bort alla mellanrum på kanterna av inputen.
            playerInput = playerInput.split(" ")
            for i in range(len(playerInput) - 1, 0, -1): # Tar bort alla resternade mellanrumen användaren gjorde i inputen.
                if playerInput[i] == '':
                    playerInput.pop(i)
            if playerInput[0] == 'f' and playerMap[int(playerInput[2])][int(playerInput[1])] == '#': # Kollar ifall användaren flaggade en position.
                print(wall)
                print('Du valde att flagga', int(playerInput[1]), int(playerInput[2]))
                return playerInput
            elif playerInput[0] == 'of' and playerMap[int(playerInput[2])][int(playerInput[1])] == '¤': # Kollar ifall användaren oflaggar en position. 
                print(wall)
                print('Du valde att oflagga', int(playerInput[1]), int(playerInput[2]))
                return playerInput
            elif playerInput[0] == 'lämna': # Ifall användaren vill lämna mitt i programet kan den det.
                print(wall)
                menu(1, 'dnf')            
            elif playerMap[int(playerInput[1])][int(playerInput[0])] == '#': # Kollar ifall användarens värde är ett tomt utryme.
                print(wall)
                print('Du valde att visa postitionen', int(playerInput[0]), int(playerInput[1]))
                return playerInput
        except (ValueError, IndexError): # Skickar denna felkod ifall användaren inte ger ut två heltal som värde.
            print("Oops.. Du skrev inte in en posision innom kartan.")



'''mapReveal byter ut platsen som användaren angav till rätt sak där den ska antingen visa/flagga eller oflagga något.'''
def mapReveal(playerInput, playerMap, fullList, freeSpace, bombCount):
    if playerInput[0] == 'f': # Denna är tillför att flagga en position.
        playerMap[int(playerInput[2])][int(playerInput[1])] = '¤'
        bombCount[0] -= 1 # Visar att det finns 1 mindre bomb.
    elif playerInput[0] == 'of': # Oflaggar en position.
        playerMap[int(playerInput[2])][int(playerInput[1])] = '#'
        bombCount[0] += 1 # Visar att det finns 1 mer bomb för att en flagga försvan.
    elif fullList[int(playerInput[1])][int(playerInput[0])] == 'x': # Kollar om användaren träffade en bomb och isåfall så förlorar den.
        win = 'L'
        menu(1, win) # Anropar menu med informationen att användaren förlorade.
         
    elif fullList[int(playerInput[1])][int(playerInput[0])] == 0: # Kollar ifall platsen den ska visa var en nolla.
        zeroChecker(playerInput, freeSpace, playerMap, fullList) # Anropar zeroChecker för att vissa alla tal runt nollorna som visades.
    else: 
        playerMap[int(playerInput[1])][int(playerInput[0])] = str(fullList[int(playerInput[1])][int(playerInput[0])]) # Visar området användaren angav.
        freeSpace[0] -= 1 # Räknar att det finns 1 mindre plats kvar på planen.



''' zeroChecker kollar ifall användaren visar en nolla och då visar alla siffor runt nollan, där ifall det visar en nolla så repiteras denna funktion. '''
def zeroChecker(playerInput, freeSpace, playerMap, fullList, zeroFinderX = 0, zeroFinderY = 0):
    back = 0 # back och front är till för att programmet ska gå ett steg upp från positionen användaren angav till ett steg under.
    front = 3            
    if int(playerInput[1]) + zeroFinderY == 0: # ifall y värdet är 0 så ändras värdet så den inte kollar utanför listan.
        back = 1
    elif int(playerInput[1]) + zeroFinderY == len(playerMap) - 1: # ifall y värdet är lika stort som listan så ändras värdet så den inte kollar utanför listan.
        front = 2        
    for j in range(back, front): # Kollar listan ett up och ett steg ner i listorna.
        
        '''Kollar positionen ett steg till vänster i listan där den sedan visar postionen och kollar ifall den siffran var en nolla.'''
        if int(playerInput[0]) - 1 + zeroFinderX > -1 and playerMap[int(playerInput[1]) - 1 + j + zeroFinderY][int(playerInput[0]) - 1 + zeroFinderX] == '#': 
            holder = str(fullList[int(playerInput[1]) - 1 + j + zeroFinderY][int(playerInput[0]) - 1 + zeroFinderX])
            playerMap[int(playerInput[1]) - 1 + j + zeroFinderY][int(playerInput[0]) - 1 + zeroFinderX] = holder
            freeSpace[0] -= 1 # Räknar att det finns 1 mindre plats kvar på planen.
            if playerMap[int(playerInput[1]) - 1 + j + zeroFinderY][int(playerInput[0]) - 1 + zeroFinderX] == '0':
                zeroChecker(playerInput, freeSpace, playerMap, fullList, -1 + zeroFinderX, -1 + j + zeroFinderY) # ändrar zeroFinder x och y för att positionera funktionen mitt på den nya nollan.
                
        '''Kollar positionen i mitten av det angavt x värde i listan där den sedan visar postionen och kollar ifall den siffran var en nolla.'''     
        if playerMap[int(playerInput[1]) - 1 + j + zeroFinderY][int(playerInput[0]) + zeroFinderX] == '#':
            holder = str(fullList[int(playerInput[1]) - 1 + j + zeroFinderY][int(playerInput[0]) + zeroFinderX])   
            playerMap[int(playerInput[1]) - 1 + j + zeroFinderY][int(playerInput[0]) + zeroFinderX] = holder
            freeSpace[0] -= 1 # Räknar att det finns 1 mindre plats kvar på planen.
            if playerMap[int(playerInput[1]) - 1 + j + zeroFinderY][int(playerInput[0]) + zeroFinderX] == '0':
                zeroChecker(playerInput, freeSpace, playerMap, fullList, 0 + zeroFinderX, -1 + j + zeroFinderY) # ändrar zeroFinder x och y för att positionera funktionen mitt på den nya nollan.
        
        '''Kollar positionen ett steg till höger i listan där den sedan visar postionen och kollar ifall den siffran var en nolla.'''        
        if int(playerInput[0]) + zeroFinderX + 1 < len(fullList) and playerMap[int(playerInput[1]) - 1 + j + zeroFinderY][int(playerInput[0]) + 1 + zeroFinderX] == '#':
            holder = str(fullList[int(playerInput[1]) - 1 + j + zeroFinderY][int(playerInput[0]) + 1 + zeroFinderX])
            playerMap[int(playerInput[1]) - 1 + j + zeroFinderY][int(playerInput[0]) + 1 + zeroFinderX] = holder
            freeSpace[0] -= 1 # Räknar att det finns 1 mindre plats kvar på planen.
            if playerMap[int(playerInput[1]) - 1 + j + zeroFinderY][int(playerInput[0]) + 1 + zeroFinderX] == '0':
                zeroChecker(playerInput, freeSpace, playerMap, fullList, 1 + zeroFinderX, -1 + j + zeroFinderY) # ändrar zeroFinder x och y för att positionera funktionen mitt på den nya nollan.
menu()