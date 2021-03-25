#coding: utf-8
''' Hjälpfunktion åt övriga funktioner'''
def startCrypt(key):
    smallLetters = "abcdefghijklmnopqrstuvwxyzåäö" # alphabetet som även inkluderar åäö 
    key = key.lower() # Ser till att nyckeln blir läsbar av programet även om man skrev stora bokstäver
    return smallLetters, key



''' Hjälpfunktion till encrypt och decrypt '''
def cryptInIt(text, key, i):
    smallLetters, key = startCrypt(key)
    keyNumber = i 
    while keyNumber >= (len(key) - 1): # Gör så att key kan vara kortare en text
        keyNumber = keyNumber - (len(key) - 1) 
    smallLettersTemp = ""
    x = smallLetters.index(key[keyNumber])
    
    ''' Denna for in range loop skapar en temporär alphabete som börjar från bokstaven som är i x '''
    for k in range(0,len(smallLetters)): 
        if  k + x <= (len(smallLetters) - 1): 
            smallLettersTemp += smallLetters[k + x]
        else:
            smallLettersTemp += smallLetters[k + x - len(smallLetters)]    
    return smallLettersTemp



''' Denna funktion Krypterar det man har skrivit i text, genom att jemföra förhållandet mellan bokstäverna
    i text och key '''        
def encrypt(text, key): 
    smallLetters, key = startCrypt(key)
    crypted = ""
    for i in range(0,len(text)): 
        smallLettersTemp = cryptInIt(text, key, i)  
        if text[i] in smallLetters.upper(): # Gör så att krypteringen kan handtera stora bokstäver
            lettersTemp = smallLettersTemp.upper() 
            keycard = smallLetters.upper().index(text[i])
            crypted += lettersTemp[keycard] 
        elif text[i] in smallLetters: # Gör så att krypteringen kan handtera små bokstäver
            lettersTemp = smallLettersTemp
            keycard = smallLetters.index(text[i]) 
            crypted += lettersTemp[keycard]
        else:
            crypted += text[i] #Fixar så att speciala tecken fungerar som , . - # !
    return crypted



''' Denna funktion avkrypterar texten, genom att gemföra förhållandet mellan krypterade text och key sedan
    jämföra det med aplhabetet'''
def decrypt(text, key):
    smallLetters, key = startCrypt(key)
    decrypted = ""
    for i in range(0,len(text)):
        smallLettersTemp = cryptInIt(text, key, i)
        if text[i] in smallLetters.upper(): # Gör så att avkrypteringen kan handtera stora bokstäver
            lettersTemp = smallLettersTemp.upper()
            uncard = lettersTemp.index(text[i]) 
            decrypted += smallLetters.upper()[uncard]
        elif text[i] in smallLetters: # Gör så att avkrypteringen kan handtera små bokstäver
            lettersTemp = smallLettersTemp
            uncard = lettersTemp.index(text[i])
            decrypted += smallLetters[uncard]
        else:
            decrypted += text[i] #Fixar så att speciala tecken fungerar som , . - # !           
    return decrypted



''' Test funktion för att testa övriga funktioner '''
def runTestCode(text, key):
    print('-'*50)
    print("klartext :",text,"key:",key)
    etext = encrypt(text, key)
    print("Krypterat:",etext)
    dtext = decrypt(etext, key)
    print("Avkodat :",dtext)
runTestCode("'Knas' i äpplet, säger Sara", "Spaggeti")

        
    