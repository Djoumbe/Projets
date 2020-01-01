from random import *
Naruto = []
for i in range (1):
    Naruto.append( randint(0,4000))
    shuffle(Naruto)
    N = choice(Naruto)
    print (Naruto)
if N >=2000:
    print ("Naruto est le plus puissant des Hokages")
    else N >2000:
    print ("T'es éclaté, on va pas se mentir")

