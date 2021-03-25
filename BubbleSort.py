# coding: utf-8
import random


''' Denna funktion utför sorterings algoritmen bubblesort, som sorterar en lista och skickar sorterad version av listan genom att gå tal för tal
    och gämföra ifall den till vänster är större än den till höger och sedan swapa plats på dom ifall dom är det.'''
def bubble(numbers):
    for i in range (0, len(numbers)):
        isSorted = True # Denna gör så när hela listan värkar vara sorterad så kan programmet veta att den är sorterad.
        for j in range (1, len(numbers) - i): # Konstant sorterar listan tills allt är sorterad där den hoppar över att sortera något som redan är sorterad.
            if numbers[j] < numbers [j - 1]:
                swap(numbers, j)
                isSorted = False # Detta gör så att programet vet att listan inte är sorterad så länge denna sak upprepas.
        if isSorted:
            return numbers # Returnerar listan ifall den är sorterad.
    return numbers # Returnerar listan ifall listan är tom.
        
        
        
''' Denna funktion byter plats på två tal i listan ifall talet till vänster är störe än talet till höger '''
def swap(numbers, j):
    numberHolder = numbers[j] # Skapar en plats hållare för tallet i [j].
    numbers[j] = numbers [j - 1] # Byter ut talet i [j] mot det störe talet.
    numbers [j - 1] = numberHolder # Lägger in det mindre talet till vänster om det störe talet.
    
    
    
''' Denna funktion genererar en lista genom att generera en mängd tal som är lika med numret i element '''     
def generateList(element):
    numbers = [] 
    for z in range(0,element): 
        randomNumber = random.randint(0,20) # Genererar ett tal mellan 0-20 som lägs in sedan i listan.
        numbers.append(randomNumber) # Lägger in det slumpade talet i listan.
    return numbers # Returnerar den slump gjorda listan. 



''' Test Kod som visar att programmet fungerar genom att visa den sorterade och osorterade listan '''
def runTestCode(element):
    print('-'*50)
    numbers = generateList(element) # Kallar till generateList för att skapa en lista
    print("Din lista:",numbers)
    numbers = bubble(numbers) # Kallar till bubble för att sortera listan.
    print('Din lista fast sorterad:',numbers)

runTestCode(20)
runTestCode(0)