from random import randrange 
valeurs = [i for i in range (1,11)]
couleurs = [i for i in range (1,5)]
nbTours = 7
score = 0
paquet = [(v,c)for v in valeurs for c in couleurs] 
main1, main2 = [], []
for i in range(nbTours):
    x = paquet [randrange(len(paquet))]
    main1.append(x)
    paquet.remove(x)
    y = paquet [randrange(len(paquet))]
    main2.append(y)
    paquet.remove(y)
    
def PlusGrandQue (carte1, carte2):
    if carte1[i][0] > carte2[i][0] or (
    carte1[i][0] == carte2[i][0] and carte1[i][1] > carte2[i][1]):
        score += 1
    else :
        score -= 1
    print ("Vainqueur :"+("joueur 1" if score > 0 else "joueur 2"))