#ESERCIZIO 10
#Dati in input il voto in trentesimi e il numero di crediti di tre esami, calcolare la media ponderata
#Nota bene
#Fare il controllo che il voto sia da 1 a 30 e che i crediti siano da 1 a 12
vototrentesimi1 = int(input("mettere voto 1 in trentesimi "))
vototrentesimi2 = int(input("mettere voto 2 in trentesimi "))
vototrentesimi3 = int(input("mettere voto 3 in trentesimi "))

numcrediti1 = int(input("metettere primo credito "))
numcrediti2 = int(input("metettere secondo credito "))
numcrediti3 = int(input("metettere terzo credito "))

tot1 = int(vototrentesimi1*numcrediti1)
tot2 = int(vototrentesimi2*numcrediti2)
tot3 = int(vototrentesimi3*numcrediti3)