# coding: utf-8
import random 

''' Denna funktion är sorterings algoritment quick sort. Den fungerar genom att ta en punk i listan och använda den som sin
    pivit point, och sedan dela in alla number som är större en den till en lista, och alla som är mindre en den till en mindre
    lista. Efter det så tar den båda listerna och startar om programet med dom två sorterade listorna.''' 
def quickSort(randomList):
    if len(randomList) <= 1: # Ifall den orginela listan har blivit 1 eller mindre så vet man att listan är sorterad.
        return randomList # Returnerar den sorterade listan
    else:
        dividePoint = randomList.pop() # Tar ut ett nummer från listan som sedan kommer användas som pivit pointen.
    
        biggerNumber = []
        lowerNumber = []

        for number in randomList: # for number tar ut ett tal från vänster av listan som den inte tagit, sedan loopar tills den använt alla siffror.
            if number > dividePoint: # Detta sorterar listan efter en pivit point där alla som är större går in i större listan.
                biggerNumber.append(number)
            else:
                lowerNumber.append(number) # IFall tallet inte var större så var det mindre eller = så där med går den i mindre listan.
                
    # Detta return loopar funktionen fast tar den nya listan som är sorterad och går igenom programmet igen och igen till den är helt sorterad.
    return quickSort(lowerNumber) + [dividePoint] + quickSort(biggerNumber) 



''' Generate list genererar en slump mässig lista efter hur många tal användaren vill ha och vilka tal listan kan variera mellan '''
def generateList(element, numberSpan):
    randomList = [] 
    for z in range(0,element): # Loopar mängden gånger användaren eller testkoden sa åt den att göra.
        randomNumber = random.randint(0,numberSpan) # Genererar ett tal mellan 0-numberSpan som lägs in sedan i listan.
        randomList.append(randomNumber) # Lägger in det slumpade talet i listan.
    return randomList # Returnerar den slump gjorda listan. 



''' Denna funktion skapar interaktivitet med programmet där den tillåter dig att sätta in hur många tal du vill ha i din lista och hur stort tal den
    ska kunna generera.'''
def interactive():
    print('-'*50)
    validInput = False
    errorText = 'Hoppsan! Det där var inte ett heltal, försök igen..'
    
    # Denna while loop loopar konstant tills den tar sig till en break, där den bara kan göra det ifall den hittar ett heltal.
    while not validInput:
        try:
            element = int(input('Skriv in hur många heltal du vill generera: '))
            break
        except ValueError:
            print(errorText)     
    print('-'*50)
    
    # Denna while loop loopar konstant tills den tar sig till en break, där den bara kan göra det ifall den hittar ett heltal.
    while not validInput:
        try:
            numberSpan = int(input('Skriv hur stort heltal du vill kunna generera: '))
            break
        except ValueError:
            print(errorText)      
    runTestCode(element, numberSpan) # Kallar till runTestCode för att utföra resten av programmet. 



''' Denna funktion är test kod för att kolla att programet fungerar samt kod för att göra det mer användarvänligt
    och lättare att förstå vad som hände. Samt gör denna test kod att rästen av programmet startas och får med sig rätta värden. '''
def runTestCode(element, numberSpan):
    print('-'*50)
    randomList = generateList(element, numberSpan) # Kallar till generateList för att skapa en lista
    print("Din lista:",randomList)
    randomList = quickSort(randomList) # Kallar till quickSort för att sortera listan.
    print('Din lista fast sorterad:',randomList)  



runTestCode(20, 31) # Första värdet är mängden element och andra är hur stort tal den ska kunna generera
runTestCode(0, 0)
runTestCode(1, 0)
runTestCode(0, 1)
interactive()