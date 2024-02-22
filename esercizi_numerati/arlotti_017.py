"""
Esercizio 17
Scrivere un programma che passati in input n valori popoli una lista.
In seguito chiede all'utente di inserire un valore in modo tale da verificare che esso 
sia presente nella lista. Stampare a video ("Valore presente"/"Valore non presente").
"""
list_popol = []
for i <= cicli:
    dato = input("inserire dato da aggiungere alla lista    ")
    list_popol.append(dato)

controllo = input("inserisci valore da controllare  ")
if controllo in list_popol:
    print("dato presente")
else:
    print("dato NON presente")