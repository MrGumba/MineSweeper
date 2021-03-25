#!/usr/bin/env python
# coding: utf-8

print("hello world")
name=input("Vad heter du: ")
print(name)
print("Hej",name,"!")
print("Hej "+name+"!")
print("Hej",name+"!")
print("6 + 3 =",6+3)
print("6 - 3 =",6-3)
print("6 * 3 =",6*3)
print("6 / 3 =",6/3)
print("6 upphöjt till 3 = ",6**3)
print("7 / 3 =",7/3)
print("7 / 3 =",7//3,"med",7%3,"i rest")
print(2+3*4)
print((2+3)*4)

x = 7/3
fStr = "Här är en formatterad sträng: {:.2f}".format(x)
print(fStr)


# variabler och operatorer
b=10
h=7
area=b*h/2
print(area)


pi = 3.1415
r=float(input("Radie = "))
area=pi*r**2
print("Area =",round(area,1))

year=int(input("Vilket år är du född? "))
age=2019-year
print("Du är",age,"år gammal i år")



secondsStr = input("Ange antal sekunder: ")
s = int(secondsStr)
h = s // 3600
s = s - h*3600
m = s // 60
s = s - m*60
print("Tid:",h,"timmar",m,"minuter",s,"sekunder")

secondsStr = input("Ange antal sekunder: ")
s = int(secondsStr)
h = s // 3600
s = s % 3600
m = s // 60
s = s % 60

print("Tid: "+str(h)+" timmar "+str(m)+" minuter "+str(s)+" sekunder")
print("Tid: {:02}:{:02}:{:02}".format(h,m,s))

secondsStr = input("Ange antal sekunder: ")
s = int(secondsStr)
h = s // 3600
s = s % 3600
m = s // 60
s = s % 60

outputStr = "Tid: ";
if h > 0:
  outputStr = outputStr + str(h)+" timmar "+str(m)+" minuter "+str(s)+" sekunder"
elif m > 0:
  outputStr = outputStr + str(m)+" minuter "+str(s)+" sekunder"
else:
  outputStr = outputStr +str(s)+" sekunder"

print(outputStr)

x = "hej"
y = "nonsens"
z = "zeeta"
print("Här är en formatterad sträng: {} {} {} knasilur".format(x,y,z))

print("Här är en formatterad sträng: {:10} {:10} {:10} knasilur".format(x,y,z))

print("Här är en formatterad sträng: {:10}{:10}{:10} knasilur".format("måndag","sfwejkl","werui"))
print("Här är en formatterad sträng: {:10}{:10}{:10} knasilur".format("tisdag","sfwejkl","werui"))
print("Här är en formatterad sträng: {:10}{:10}{:10} knasilur".format("onsdag","sfwejkl","werui"))


input("Press any key to continue...")

#from math import pi
#r=int(input("Radie = "))
#area=pi*r**2
#print("Area =",round(area,1))
