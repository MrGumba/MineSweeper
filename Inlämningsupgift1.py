#coding: utf-8

'''def encrpt krypterar strängnen användaren skrivier in genom att gemföra den med en sträng som alphabete '''
def encrpyt(text, key):
    krypterat = ''
    bokstäversmå = "abcdefghijklmnopqrstuvwxyzåäö" # alphabetet för dom små bokstäverna 
    bokstäverstor = "ABCDEFGHIJKLMNOPQRSTUVWXYZÅÄÖ" # alphabetet för dom stora bokstäverna 
    
    ''' Denna while loop fixar så att man kan skriva in ett number över 29 på key utan att den krachar '''
    while key >= 29: 
        key = key - 29  
        
    ''' Denna for-loop kollar alla bokstäver man har skrivit in och går i genom varje en för en och byter ut
        bokstaven med en annan från alphabetet genom att gå fram key mäng  '''    
    for i in range(0,len(text)):
        if text[i] in bokstäversmå: # kollar små bokstäver
            x = bokstäversmå.index(text[i])
            if len(bokstäversmå) - (x+key) >= 0: 
                krypterat += bokstäversmå[x+key]
            else: 
                krypterat += bokstäversmå[(x+key)-len(bokstäversmå)]
        elif text[i] in bokstäverstor: # kollar stora bokstäver
            m = bokstäverstor.index(text[i])
            if len(bokstäverstor) - (m+key) >= 0:
                krypterat += bokstäverstor[m+key]
            else:
                krypterat += bokstäverstor[(m+key)-len(bokstäversmå)]
        else:
            krypterat += text[i] # lägger till alla special karaktärer som har skrivits in
    return krypterat



''' denna funktion decrypterar texten man skriver in genom att gemföra den med en sträng som innehåller alphabetet
    och backa tillbaka key mängd i alphabetet'''
def decrypt(user_crypt, key):
    avkrypterat = ''
    bokstäversmå = "abcdefghijklmnopqrstuvwxyzåäö" # alphabetet för dom små bokstäverna 
    bokstäverstor = "ABCDEFGHIJKLMNOPQRSTUVWXYZÅÄÖ" # alphabetet för dom stora bokstäverna 
    
    ''' Igen fixar key så att man kan skriva vilket number som hällst '''
    while key >= 29:
        key = key - 29   
        
    ''' Denna for-loop kollar alla bokstäver man har skrivit in och går i genom varje en för en och byter ut
        bokstaven med en annan från alphabetet genom att backa key mängd '''
    for i in range(0,len(user_crypt)):    
        if user_crypt[i] in bokstäversmå: # kollar små bokstäver
            x = bokstäversmå.index(user_crypt[i])
            if len(bokstäversmå) - (x-key) >= 0:
                avkrypterat += bokstäversmå[x-key]
            else: 
                avkrypterat += bokstäversmå[(x-key)+len(bokstäversmå)]
        elif user_crypt[i] in bokstäverstor:  # kollar stora bokstäver
            m = bokstäverstor.index(user_crypt[i])
            if len(bokstäverstor) - (m-key) >= 0:
                avkrypterat += bokstäverstor[m-key]
            else:
                avkrypterat += bokstäverstor[(m-key)+len(bokstäversmå)]
        else:
            avkrypterat += user_crypt[i] # lägger till alla special karaktärer som har skrivits in
    return avkrypterat



'''denna funktion är till för att tästa programet'''
def runtestcode(text, key):
    print('-'*50)
    print('Klartext :',text,"  key:", key)
    etext = encrpyt(text, key)
    print('Krypterat:',etext)
    dtext = decrypt(etext, key)
    print("Avkodat :",dtext)
    


''' testkod för att kolla om programet fungerar '''
runtestcode("knas", 7)
runtestcode("KnasBoll", 27)
runtestcode("'knas' i äpplet, säger Sara", 67)