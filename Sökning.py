# coding: utf-8

''' kollar varje plats i listan tills den hittar det den vill och avslutar funktionen '''
def find(numbers, n): 
    position = -1 # Gör så att ifall talet inte hittas så kommer programmet förstå att talet inte är med i listan
    for i in range(len(numbers)): 
        if numbers[i] == n:
            position = i + 1
            return position
    return position # Två return positions där den andra funkar some en else: och avslutar funktionen.



def runTestCode(numbers, n): # Test kod för programmet som visar för användaren var numret fanns. 
    print('-'*50)
    print("Din lista: ",numbers)
    print("Det första talet :",n)
    position = find(numbers, n)
    if (position >= 0):
        print(n, "Finns på plats", position)
    else:
        print(n, "finns inte med i listan")
        
        
numbers = [5, 3, 2, 4, 1, 7, 9]

runTestCode(numbers, 1)
runTestCode(numbers, 9)
runTestCode(numbers, 42)

'''”Hur många jämförelser krävs för linjär sökning för en lista med 1000 element?”. 
    Svar: Allt mellan 0 - 1000 beronde på hur tidigt I listan det sökta elementet är där ifall den är på 1000 platsen tar det 1000
    jämförelser'''