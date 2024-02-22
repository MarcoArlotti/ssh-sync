"""
Esercizio 2 – Anno bisestile
Chiesto all’utente un anno in input controllare la validità dell’input (0<anno<2100) e
dire se esso è bisestile o no.
A tal fine, implementare il seguente algoritmo:
Un anno è bisestile se esso è divisibile per 400 altrimenti è bisestile se è divisibile per
4 e non divisibile per 100. Non è bisestile negli altri casi.
N.B.
L’algoritmo può essere implementato anche con un unico blocco if/else con una
condizione composta.
"""
anno = int(input("inserisci anno:   "))
if not 0 <anno< 2100:
    print("VALORI NON CORRETTI!")
else:
    if anno % 400 == 0:
        print("l'anno è bisestile")
    elif not anno % 400 == 0:
        print("l'anno è non bisestile")
    else:
        if anno % 4 == 0:
            diviso_4 = anno / 4
        else:
            print("l'anno è non bisestile")
            if not diviso_4 % 100 == 0:
                print("l'anno è bisestile")
            else:
                print ("l'anno è non bisestile")
         