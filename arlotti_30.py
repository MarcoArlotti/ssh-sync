"""
Sulla base di quanto visto a lezione sul modulo random realizzare un programma che implementi il gioco della tombola o del bingo. 
Al fine di far ciò, lo studente implementi le seguenti funzioni:
1) def genera_cartella(id: int)->dict:
La funzione genera una cartella della tombola/bingo e la restituisce come dizionario. Dare un id alla cartella.
N.B.
La cartella ha le seguenti caratteristiche:
1) 3 righe e 9 colonne
2) 15 numeri in totale (5 per riga)
3) ogni colonna ha solo i numeri della decina di riferimento: la prima dall'1 al 9, la seconda dal 10 al 19....l'ultima dall'80 al 90


2) def estrai_numero(numeri_estratti: list[])->int:
La funzione estrae un nuovo numero, lo inserisce nella lista passata come parametro, controllando che non sia duplicato, e restituisce tale numero come intero.

3) def controlla_cartella(cartella: dict, numeri_estratti[])->list[bool]:
Data come parametro una cartella e la lista di numeri estratti restituisca lo stato di tale cartella. Potrebbe restituire una lista di bool dove l'elemento 0 si riferisce all'ambo, l'1 al terno fino ad arrivare al 4 che si riferisce alla tombola/bingo.
es.
[True, True, False, False, False] per una cartella che ha fatto terno(naturalmente per fare terno bisogna aver fatto anche ambo....)

Realizzare un programma che implementi la logica di funzionamento:
a) Utilizzando le opportune variabili di stato (es. una lista di cartelle, la lista dei numeri estratti, lo stato del gioco(ambo, terno,....))
b) Utilizzando le funzioni precedentemente definite al fine di gestire le varie fasi del gioco.

Buona fortuna.
"""


import random





   
    
def dichiara_cartella() -> list[int]:
    c0 = [1,2,3,4,5,6,7,8,9]
    c1 = [10,11,12,13,14,15,16,17,18,19]
    c2 = [20,21,22,23,24,25,26,27,28,29]
    c3 = [30,31,32,33,34,35,36,37,38,39]
    c4 = [40,41,42,43,44,45,46,47,48,49]
    c5 = [50,51,52,53,54,55,56,57,58,59]
    c6 = [60,61,62,63,64,65,66,67,68,69]
    c7 = [70,71,72,73,74,75,76,77,78,79]
    c8 = [80,81,82,83,84,85,86,87,88,89,90]
    c_e0 = []
    c_e1 = []
    c_e2 = []
    c_e3 = []
    c_e4 = []
    c_e5 = []
    c_e6 = []
    c_e7 = []
    c_e8 = []
    return c0,c1,c2,c3,c4,c5,c6,c7,c8,c_e0,c_e1,c_e2,c_e3,c_e4,c_e5,c_e6,c_e7,c_e8



def genera_numeri(c0:list[int],c1:list[int],c2:list[int],c3:list[int],c4:list[int],c5:list[int],c6:list[int],c7:list[int],c8:list[int],c_e0:list[int],c_e1:list[int],c_e2:list[int],c_e3:list[int],c_e4:list[int],c_e5:list[int],c_e6:list[int],c_e7:list[int],c_e8:list[int])-> list[int]:
    num = random.choice(c0)
    c0.remove(num)
    c_e0.append(num)

    num = random.choice(c0)
    c0.remove(num)
    c_e0.append(num)

    num = random.choice(c0)
    c0.remove(num)
    c_e0.append(num)


    num = random.choice(c1)
    c1.remove(num)
    c_e1.append(num)

    num = random.choice(c1)
    c1.remove(num)
    c_e1.append(num)

    num = random.choice(c1)
    c1.remove(num)
    c_e1.append(num)


    num = random.choice(c2)
    c2.remove(num)
    c_e2.append(num)

    num = random.choice(c2)
    c2.remove(num)
    c_e2.append(num)

    num = random.choice(c2)
    c2.remove(num)
    c_e2.append(num)


    num = random.choice(c3)
    c3.remove(num)
    c_e3.append(num)

    num = random.choice(c3)
    c3.remove(num)
    c_e3.append(num)

    num = random.choice(c3)
    c3.remove(num)
    c_e3.append(num)


    num = random.choice(c4)
    c4.remove(num)
    c_e4.append(num)

    num = random.choice(c4)
    c4.remove(num)
    c_e4.append(num)

    num = random.choice(c4)
    c4.remove(num)
    c_e4.append(num)


    num = random.choice(c5)
    c5.remove(num)
    c_e5.append(num)

    num = random.choice(c5)
    c5.remove(num)
    c_e5.append(num)

    num = random.choice(c5)
    c5.remove(num)
    c_e5.append(num)


    num = random.choice(c6)
    c6.remove(num)
    c_e6.append(num)

    num = random.choice(c6)
    c6.remove(num)
    c_e6.append(num)

    num = random.choice(c6)
    c6.remove(num)
    c_e6.append(num)


    num = random.choice(c7)
    c7.remove(num)
    c_e7.append(num)

    num = random.choice(c7)
    c7.remove(num)
    c_e7.append(num)

    num = random.choice(c7)
    c7.remove(num)
    c_e7.append(num)


    num = random.choice(c8)
    c8.remove(num)
    c_e8.append(num)

    num = random.choice(c8)
    c8.remove(num)
    c_e8.append(num)

    num = random.choice(c8)
    c8.remove(num)
    c_e8.append(num)
    return c0,c1,c2,c3,c4,c5,c6,c7,c8,c_e0,c_e1,c_e2,c_e3,c_e4,c_e5,c_e6,c_e7,c_e8
#con sort mette in ordine le liste(i valori)



def imposta_cartelle() -> dict[int]:
   pass
   



def random_spazi_vuoti(c_e0,c_e1,c_e2,c_e3,c_e4,c_e5,c_e6,c_e7,c_e8):
    canc_2 = 4   #volte da fare il ciclo della cancellazzione
    canc_1 = 4
    lista_cont = [c_e0,c_e1,c_e2,c_e3,c_e4,c_e5,c_e6,c_e7,c_e8] #colonne

    
    for i in range(canc_2):
        colonna = random.choice(lista_cont)
        lista_cont.remove(colonna)

        n = [0,1,2]
        l = random.choice(n)
        n.remove(l)
        colonna.pop(l)
        
        

        l = random.choice(n)
        n.remove(l)
        
        colonna.pop(l)
    


    #in teoria funziona
        
    #for _ in range(canc_1):
    #    colonna = random.choice(lista_cont)
    #    lista_cont.remove(colonna)
    #    n = [0,1,2]
    #    l = random.choice(n)
    #    n.remove(l)
    #    colonna.pop(l)

    return c_e0,c_e1,c_e2,c_e3,c_e4,c_e5,c_e6,c_e7,c_e8



c0,c1,c2,c3,c4,c5,c6,c7,c8,c_e0,c_e1,c_e2,c_e3,c_e4,c_e5,c_e6,c_e7,c_e8 = dichiara_cartella()
c0,c1,c2,c3,c4,c5,c6,c7,c8,c_e0,c_e1,c_e2,c_e3,c_e4,c_e5,c_e6,c_e7,c_e8 = genera_numeri(c0,c1,c2,c3,c4,c5,c6,c7,c8,c_e0,c_e1,c_e2,c_e3,c_e4,c_e5,c_e6,c_e7,c_e8)
c_e0,c_e1,c_e2,c_e3,c_e4,c_e5,c_e6,c_e7,c_e8 = random_spazi_vuoti(c_e0,c_e1,c_e2,c_e3,c_e4,c_e5,c_e6,c_e7,c_e8)
print(c_e0,c_e1,c_e2,c_e3,c_e4,c_e5,c_e6,c_e7,c_e8)
