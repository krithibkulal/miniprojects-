import random as r
a=int(input("How many numbers you want in your password"))
b=int(input("How many letters you want in your password"))
c=int(input("How many symbols you want in your password"))
characters=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","P","q","r","s","t","u","v","w","x","y","z"]
symbols= ["!","@","#","$","%","^","&","*","(",")","[","]","{","}","\","<",">","?","+","-","*","/","_","~"]
numbers=["0","1","2","3","4","5","6","7","8","9"]

password= ""
for i in range(a):
    password +=r.choice(characters[:30])
for i in range(b):
    password +=r.choice(letters[:30])
for i in range(c):
    password +=r.choice(symbols[:30])