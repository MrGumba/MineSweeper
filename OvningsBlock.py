#coding: utf-8

'''uppgift 1
print("Hello World")
name=input("Vad heter du:  ")
print(name,"är bäst!")
'''

'''uppgift 2
print(123 + 345 - 456)
print(12 + 3 * 8)
print(7**6)
print((6+8)*(2+5))
'''

'''uppgift 3
meter=float(input("Skriv hur många meter: "))
mile=meter/1609.334
yard=meter/0.9144
foot=meter/0.3048
inch=meter/0.0254
print(mile,"mile")
print(yard,"yard")
print(foot,"foot")
print(inch,"inches")
'''

'''uppgift 4
meter=float(input("Skriv hur många meter: "))
mile=meter/1609.334
yard=meter/0.9144
foot=meter/0.3048
inch=meter/0.0254
print("mile = {:.3f}".format(mile))
print("yard = {:.3f}".format(yard))
print("foot = {:.3f}".format(foot))
print("inch = {:.3f}".format(inch))
'''

'''uppgift 5
rest=float(input("Vilket tal vill du dividera: "))
delning=float(input("Vad vill du dividera med: "))
print("det blir",rest//delning,"med",rest%delning,"i rest") 
'''

'''uppgift 6
rektangelbas = 5
rektangelhöjd = 7
print("omkrätsen är",rektangelbas * 2 + rektangelhöjd * 2)
print("arean är",rektangelbas * rektangelhöjd)
'''

'''uppgift 7
rektangelbas1=float(input("vad är basen på rektangeln: "))
rektangelhöjd1=float(input("vad är höjden på rektangeln: "))
print("omkrätsen är",rektangelbas1 * 2 + rektangelhöjd1 * 2)
print("arean är",rektangelbas1 * rektangelhöjd1)
'''

'''uppgift 8
vuxna=float(input("Ange antal vuxna "))
barn=float(input("Ange antal barn "))
barnkostnad=27.50
vuxnakostnad=50
print("Totala kostnaden är",vuxnakostnad * vuxna + barn * barnkostnad,"kr")
'''

'''uppgift 9
print('benkt "Bengan" jansson')
print("Tecknet \\ kallas \'backslash\'")
'''

'''uppgift 10
Celsius=float(input("Ange antalet Celsius: "))
F=1.8*Celsius + 32
print("det blir",F,"Farenheit")
Farenheit=float(input("Ange antalet Farenheit "))
C=(((Farenheit - 32) * 5)/9)
print("det blir",C,"Celsius")
'''

'''uppgift 11
x=10
y=20
print(x<10)
print(y>=2*x)
print(y==10 and y==15)
print(y==10 and y>15)
print(y==10 and y==15)
'''

'''uppgift 12
regnar=input('rengnar det (j/n) ') 
if regnar=='j':
    print("ta paraply!")
else: 
    print("Bra för dig")
'''


'''uppgift 13
fråga=input('har du såvit minst 8 timmar i natt (j/n)')
if fråga=='j':
    print("bra jobbat!")
elif fråga=='n':
    print("För att må bra ska du såva 8 timmar!")
elif fråga!='n' or fråga!='j':
    print("jag förstår inte")
'''


'''uppgift 14
def meny ():
    print("1. skapa nytt")
    print("2. öppna")
    print("3. skriv ut")
    print("4. avsluta")
meny()
filer=input('vad vill du göra?: ')
if filer=='1':
    print('Du valde: skapa nytt')
elif filer=='2':
    print('Du valde: öppna')
elif filer=='3':
    print('Du valde: skriv ut')
elif filer=='4':
    print('Du valde: avsluta')
'''

'''uppgift 15
print('Du ska ange två tal, en täljare och en nämnare')
täljaren=float(input('Täljaren: '))
nämnaren=float(input('Nämnaren: '))
if nämnaren !=0:
    print(täljaren/nämnaren)
else:
    print('nämnaren kan inte vara 0!')
'''

'''uppgift 16
tal1=float(input('skriv in ett tal '))
tal2=float(input('skriv in ett till tal '))
if tal1==tal2:
    print("talen är lika stora")
elif tal1>tal2:
    print(tal1,"är större än",tal2)
elif tal1<tal2:
    print(tal1,"är mindre än",tal2)
'''

'''uppgift 17
tyngd=float(input('hur många kg väger vikten? '))
if tyngd==5:
    print("vikten är lika med 5kg")
elif tyngd>5:
    print("vikten är tyngre än 5kg")
elif tyngd<5:
    print("vikten är lättare än 5kg")
'''

'''uppgift 18
ålder=float(input('Hur gammal är du? '))
if ålder<18 or ålder<18:
    print("Du är omyndig och behöver vårdnadshavares godkännande")
elif ålder>17:
    print('Hej och välkommen!')
'''

'''uppgift 19
bussålder=float(input('Hur gammal är du? '))
if bussålder>14 and bussålder<66:
    print("Det kommer kosta 20kr")
elif bussålder<15 or bussålder>65:
    print("Det kommer kosta 10kr")
'''

'''uppgift 20
import random
x = random.randint(1,6)
if x<6:
    print('Du fick',x)
elif x==6:
    print('Grattis du fick',x)
'''

'''uppgift 21
x=float(input('Vilket år '))
skåttår= x/4
påriktigtskåttår= x/100
if int(skåttår)==skåttår and int(påriktigtskåttår)!=påriktigtskåttår:
    print("Skått år")
else: 
    print("inte skått år")
'''

'''uppgift 22
skivor=float(input('Hur många skivor '))
if skivor<=10:
    print(skivor * 9.9)
elif skivor>10 and skivor<=50:
    print(skivor * 9.9 * 0.95,'kr')
elif skivor>50 and skivor<100:
    print(skivor * 9.9 * 0.90,'kr')
elif skivor>100:
    print(skivor * 9.9 * 0.85,'kr')
'''

'''uppgift 23
x=0
while x<20:
    print('hej')
    x+=1

'''

'''uppgift 24
x=1
while x<32:
    print(x)
    x+=1
'''

'''uppgift 25
avsluta=input('Vill du avsluta j/n ')
while avsluta=='n':
    avsluta=input('Vill du avsluta j/n ')
'''

'''uppgift26
år=0
summa=10000

while summa<10000 * 2: 
    år+=1
    summa*=1.03
print(år)
'''

'''uppgift27
lösenord='yogg'
x=input('Ange lösenord ')
while x!=lösenord:
    print('Felaktigt lösenord. Försök igen!')
    x=input('Ange lösenord ')
if x==lösenord:
    print('Rätt lösenord!')
'''

'''uppgift28
import random

x = random.randint(0,1000)
gissningar=0
guess=float(input('Vad gissar du på '))
while guess!=x:
    if guess>x:
        print('Mitt tal är lägre')
    elif guess<x:
        print('Mitt tal är störe')
    guess=float(input('Vad gissar du på '))
    gissningar+=1
if guess==x:
    print('Du gissade rätt på',gissningar,'försök!')
'''

'''uppgift29
for i in range(0, 10):
    print(i)
'''

'''uppgift30
for x in range(0,20):
    print(x)
'''

'''uppgift31
for i in range(1,101):
    print(i)
'''

'''uppgift32
for i in range (100,0,-1):
    print(i)
'''

'''uppgift33
for i in range (1,100,):
    if (i%2)!=0:
        print(i)
'''

'''uppgift34
tal=int(input('Skriv in tal '))
for i in range (1,11):
    print(i * tal)
'''

'''upppgift35
tal=int(input('skriv in tal '))
for i in range (1,tal+1):
    print('*' * i)
'''

'''uppgift36
öppna=int(input('Vilket månadsnummer är det? '))
months=["Januari","Februari","Mars","April","Maj","Juni","Juli","Augusti","September","Oktober","November","December"]
print(months[öppna - 1])
'''

'''uppgift37
z=[17,4,6,11,43,32,]
print('Detta är din lista',z)
z.sort()
print('Det lägsta talet är',z[0])
print('Det hösta talet är',z[5])
'''

'''uppgift38
z=[17,4,6,11,43,32,]
print('Detta är din lista',z)
z.sort(reverse=True)
print('Detta är din lista ordnad från störst till minst',z)
print('Det lägsta talet är',z[0])
print('Det hösta talet är',z[5])
'''

'''uppgift39
total = int(input('Hur många tal vill du ha i listan? '))
lista = []
for p in range(total):
    k = int(input('Skriv in ett tal: '))
    lista.append(k)
    #lista+=[k]
print(lista)
summa = 0
for i in lista:
    summa+=i
print('Summan är',summa)
medelvärde = summa/total
print('Medelvärdet är',medelvärde)
'''

'''uppgift40
lista = []
l = 0 
summa = 0
while l != 'q':
    l = input('Skriv in ett tal och du kan beräkna alla genom att skriva q: ')
    if l != 'q':
        l = int(l)
        summa+=l
        lista.append(l)
totala = len(lista)
print('detta är dina tal',lista)
print('Summan är',summa)
print('Medelvärdet är:',summa/totala)
'''

'''uppgift UTMANINGEN!
import random 
kortbanktotal = []
kortbank = random.randint(2,10)
kortbanktotal.append(kortbank)
kortspelaretotal = []
for i in range (0,2):
    kortspelare = random.randint(2,10)
    kortspelaretotal.append(kortspelare)
kortenspelare = sum(kortspelaretotal)
print('Dealern fick',kortbank)
print('Du har nu total av',kortenspelare)
svar= input('Vill du förtsätta? j/n: ') 
while svar=='j' and kortenspelare<=21:
    kortspelare = random.randint(2,10)
    kortspelaretotal.append(kortspelare)
    kortenspelare = sum(kortspelaretotal)
    print('Du har nu en total av',kortenspelare)    
    svar = input('Vill du förtsätta? j/n: ')
kortenbank = sum(kortbanktotal)
while kortenbank<17:
    kortbank = random.randint(2,10)
    kortbanktotal.append(kortbank)
    kortenbank = sum(kortbanktotal)
if kortenbank>kortenspelare and kortenbank<=21 or kortenspelare>21:
    print('Dealern fick',bank,'och du fick',kortenspelare,'så tyvar förlorade du')
elif kortenspelare>kortenbank and kortenspelare<=21:
    print('Dealern fick',kortenbank,'och du fick',kortenspelare,'så du vann!')
elif kortenspelare==kortenbank:
    print('Dealern fick',kortenbank,'så ni fick like mycket så där med blev det lika!')
'''

'''uppgift41
text = input("Skriv in en text ")
print(text.capitalize())
print(text.lower())
print(text.upper())
print(text.center(30))
print(text.rjust(30))
print(text.strip())
'''

'''uppgift42
a="banan"
print(len(a)) 
'''

'''uppgift43 INTE KLAR
text = "banan"[::-1]
print(text)
def backwards(text):
    btext = ""
    return btext
'''

'''uppgift44
förnamn = input('Skriv in ditt förnamn ')
efternamn = input('Skriv in ditt efternamn ')
btext = ""
for i in förnamn: 
    btext = i + btext
btext2 = ""
for j in efternamn:
    btext2 = j + btext2
print(förnamn, efternamn,'blir',btext,btext2,'baklänges')
'''

'''uppgift45
dagar = ["måndag", "tisdag", "onsdag", "torsdag", "fredag"]
varmrätt = []
vegetariskt = []
for day in dagar:
    mat = input("Ange varmrätt för "+day+": ")
    matveg = input("Ange veg. alternativ för "+day + ": ")
    varmrätt.append(mat)
    vegetariskt.append(matveg)
print("Dag".ljust(30)+"Varmrätt".ljust(30)+"Veg. Alternativ".ljust(30))
for i in range (0,len(dagar)):
    rad = dagar[i].ljust(30)+varmrätt[i].ljust(30)+vegetariskt[i].ljust(30)
    print(rad)
'''

'''uppgift46
consonants = "bcdfghjklmnpqrstvwxz"
text = input("Skriv in en mening ")
pirat = ""
for i in range(0,len(text)):
    if text[i] in consonants:
        pirat += text[i]+"o"+text[i]
    else:
        pirat += text[i]
print(pirat)
'''

'''uppgift47
vocaler = "aouåeiyöä"
text = input("Skriv in en mening ")
ispråk = ""
for i in range(0,len(text)):
    if text[i] in vocaler:
        ispråk += "i"
    else:
        ispråk += text[i]
print(ispråk)
'''

'''extrauppgift48
import random

dice = random.randint(1,6)
print('Du rullade',dice)
lastdice = dice
gissning = input('Kommer nästa tal vara högre eller lägre (svara med h eller l): ')
dice = random.randint(1,6)
print('Du rullade',dice)
poäng = 0
if lastdice < dice:
    svar = 'h'
elif lastdice > dice:
    svar = 'l'
elif lastdice == dice:
    svar = 'lika'
while svar == gissning: 
    lastdice = dice
    poäng += 1
    gissning = input('Kommer nästa tal vara högre eller lägre (svara med h eller l): ')
    dice = random.randint(1,6)
   
    print('Du rullade',dice)
    if lastdice < dice:
        svar = 'h'
    elif lastdice > dice:
        svar = 'l'
    elif lastdice == dice:
        svar = 'lika'
if svar != gissning:
    print('Fel svar! Du gissade',gissning,'men det blev',svar,'Du fick en total av',poäng,'poäng!')
'''

'''uppgift54
x = 12
y = 3
def addition(x, y): 
    k = x + y
    return k
res = addition(x, y)
print('Summan var:',res)
'''

'''uppgift55
a = 5
b = 5
def lika(a, b):
    k=bool(a == b)
    return k
print(lika(a, b))
'''

'''uppgift56
a = 5
b = 6
def olika(a, b):
    k = a!=b
    return k 
print(olika(a, b))
'''

'''uppgift57
def intinput():
    tal = input('Ange ett heltal: ')
    while not tal.isdigit():
        print('Du angav inte ett heltal')
        tal = input('Ange ett heltal: ')
    return tal
x = intinput()
print('Du angav heltalet',x)
'''

'''uppgift58
def intinput(p):
    tal = input(p)
    while not tal.isdigit():
        print('Du angav inte ett heltal')
        tal = input(p)
    return tal
x = intinput('skriv tal: ')
print('Du angav heltalet',x)
'''

'''uppgift59
def title(t):
    print(t)
    print('='*22)
def getnumber():
    tal = float(input('Ange ett tal: '))
    return tal
def average(x1, x2, x3):
    total = (x1 + x2 + x3)/3
    return total
def printresult():
    print('Medelvärdet är',m)
title('Medelvärdet')
x1 = getnumber()
x2 = getnumber()
x3 = getnumber()
m = average(x1, x2, x3)
printresult()
'''
