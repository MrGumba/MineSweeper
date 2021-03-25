# coding: utf-8
import time
import random

''' computerGuesses är funktionen som utför gissningarna och sökningen till talet. Där den gör detta genom att gissa
    på ett tal mellan intervallet och sedan veta om talet är midnre eller störe och sedan sätta intervallet mellan
    talet den gissade + 1 och det andra talet som beror på om svaret var mindre eller störe.''' 
def computerGuesses(lowest, higest, answer = None):
    correct = 1 
    guessCount = 0 # guessCount räknar hur många gånger den har gissat på ett tal för att visa det senare.
    while correct != 0: # Denna whole loop loopar tills programet har gissat rätt på talet där programet får värdet 0.
        guess = random.randint(lowest, higest)
        guessCount += 1
        print('Jag gissar på att numret är',guess)
        if answer: # Program för att göra så att datorn kan köra koden genom att söka sig närmare och närmare nummret.
            if answer == guess:
                correct = 0
            elif answer < guess:
                correct = -1
            elif answer > guess:
                correct = 1
        else: # Programmet för att användaren kan manuelt låta datorn gissa talet.
            correct = helpToGuess()
        if correct == 0:
            print('Yey! Jag gissade rätt och det tog mig bara', guessCount,'försök!')
        elif correct > 0: # Kollar om nästa tal är störe.
            print('-'*50)
            print('Störe du säger? Okej låt mig gissa igen..')
            if lowest < guess: # Ifall den nya gissningen är störe en den förra så ändras värdet.
                lowest = guess + 1 
        elif correct < 0: # kollar om nästa tal är mindre
            print('-'*50)
            print('Mindre du säger? Okej låt mig gissa igen..')
            if higest > guess: # Ifall den nya gissningen är mindre en den förra så ändras värdet.
                higest = guess - 1
   
   
   
''' helpToGuess är en funktion som gör att användaren kan hjälpa datorn att gissa rätt på vilket tal du har tänkt på.
    Där användaren kan säga om det är rätt, eller om talet är större eller mindre. '''     
def helpToGuess():
    while True:
        try:
            print('Skriv 0 om det är korekt, 1 eller mer om det är större, och -1 eller mindre ifall det är mindre')
            correct = int(input('Svar (0, 1, -1): '))
            return correct # Returnerar vilket värde användaren skrev in tillbaka till computerGuesses
        except ValueError: # Ifall användaren inte ger ett korekt värde ältså ett heltal så skickas denna felkod.
            print('Oops! du skrev inte in ett tal testa igen!')    
            
            
            
''' Denna funktion tar hand om det mästa med interactivitet och när den körs kan användaren skriva in hur den
    vill att programmet ska köras.'''
def interactive():
    print('-'*50)
    while True:
        try:
            x = input("Ange sökintervall (ex '1-100'): ")
            x = x.replace(' ', '') # Tar bort ALLA mellan rum så även om användaren skriver 1 00 så blir det 100.
            x = x.split("-") # Tar bort - från ex 1-100 och delar up det i en lista av två värden. 
            x.sort() # Soterar listan så att om användaren skriver 100-1 tar programmet det som 1-100.
            lowest = int(x[0])
            higest = int(x[1])
            break
        except (ValueError, IndexError): # Skickar denna felkod ifall användaren inte ger ut två heltal som värde.
            print("Oops.. Du skrev inte in ett heltal testa igen")
    computerGuesses(lowest, higest)
    playerInput = ''
    while playerInput != 'n': # While loop som frågar användaren om dom vill köra igen eller inte.
        playerInput = input("Får jag köra en gång till? ('y' för ja och 'n' för nej): ")
        playerInput = playerInput.strip()
        if playerInput == 'y' or playerInput == 'n': # Detta kollar om användaren skrev 'n' eller 'y'.
            if playerInput == 'y':
                print("Yey! Då kör vi igen!")
                computerGuesses(lowest, higest)
            if playerInput == 'n': 
                print("Det var synd..")
        else: # Ifall användaren inte angav 'n' eller 'y' så skickas denna felkod ut.
            print("Du angav inte 'y' eller 'n' försök igen..")



''' Test kod som kollar om programmet fungerar genom automatiskt köra genom programmet med 3 värden 
    två för vilket intervall den ska gissa på och 1 för vad det korrekta gissningen är.'''
def runTestCode(lowest, higest, answer):
    print('-'*50)
    print('Talet datorn ska gissa är',answer)
    print('Samt är intervallet',str(lowest)+'-'+str(higest))
    print("Låt mig tänka", end='') 
    for i in range(5): # Denna loop skapar punkter som gör att programmet syns ut som att den tänker.
        time.sleep(0.5) # Även uppfyler detta att användaren kan läsa vilket intervall och vad svaret var.
        print('.', end='')
    print()
    computerGuesses(lowest, higest, answer)
    

interactive() # Kallar till interavtive så att användaren kan lägga in sina egna värden.

''' För att ändra värden i runTestCode så är lowest det minsta värdet datorn kan gissa och highest är största
    samt är answer vilket tal den ska försöka gissa på'''
runTestCode(20, 300, 42) # Används för att kalla till runTestCode för att testa programet där 