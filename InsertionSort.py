# coding: utf-8
import random

''' Denna funktion sorterar en lista genom sorterings algoritment insertion sort. Där den tar ett tal från höger av den sorterade delen av listan och sedan 
    jämföra det talet med den till vänster och se om det tallet är störe. Ifall den är större swapar dom plats och den då kollar igen till vänster ifall den är störe och fortsätter
    så tills det talet är sorterad. När talet är sorterad tar den igen ett tal från höger och loopar till listan är sorterad.'''
def insertionSort(randomList):
    for i in range(1, len(randomList)): # Hoppar över första talet för att den är redan sorterad.
        unsortedNumber = randomList[i] 
        while randomList[i-1] > unsortedNumber and i>0: # Loopar så länge det osorterade nummret är mindre en dom sorterade samt att det inte är sista talet i listan.
            randomList[i-1], randomList[i] = randomList[i], randomList[i-1] # Swappar plats på talen genom att att använda sig av att = betyder att något blir något.
            i = i - 1 
    return randomList # Returnerar den sorterade listan.



''' Generate list genererar en lista efter hur många element som man skrev in till test koden samt genererar ett 
    nummer mellan 1-20.'''
def generateList(element):
    randomList = [] 
    for z in range(0,element): 
        randomNumber = random.randint(0,20) # Genererar ett tal mellan 0-20 som lägs in sedan i listan.
        randomList.append(randomNumber) # Lägger in det slumpade talet i listan.
    return randomList # Returnerar den slump gjorda listan. 


'''' Denna funktion är test kod för att kolla att programet fungerar samt kod för att göra det mer användarvänligt
     och lättare att förstå vad som hände. Samt gör denna test kod att rästen av programmet startas och får med sig rätta värden. ''' 
def runTestCode(element):
    print('-'*50)
    randomList = generateList(element) # Kallar till generateList för att skapa en lista
    print("Din lista:",randomList)
    randomList = insertionSort(randomList) # Kallar till insertionSort för att sortera listan.
    print('Din lista fast sorterad:',randomList)   
    
runTestCode(20) # Talet i runTestCode är hur många element man vill generera.
runTestCode(0)
runTestCode(2) 