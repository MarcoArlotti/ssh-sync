"""
Funzione 1:

Scrivere una funzione che gestisca l'input di n valori (con n scelto dall'utente) e li restituisca in una lista_inp.
def input_n () -> list[int]:

Funzione 2:
Scrivere una funzione alla quale passato un numero intero restituisca True se esso è pari e False in caso contrario.
def is_pari(num: int) ->bool:

Funzione 3:
Scrivere una funzione che data in input una lista_inp. Calcoli la somma dei quadrati dei numeri pari presenti nella lista_inp e restituisca tale valore.
def somma_quadrati (lista_valori: list[int]) -> int:
"""

#funzione 1
def input_lista() -> list[int]:
    """
    questo def chiede in input tot valori quanti assegnati e li mette tutti in una lista_inp come ritorno
    """
    lista_inp = []
    
    quanti_i = int(input("inserire quanti valori si vuole aggiungere\n\n"))
    while not quanti_i == 0 :
        input_n = input("inserire un valore\n\n")
        lista_inp.append(input_n)
        quanti_i -= 1
    return lista_inp


#funzione 2 DA FARE Dopo da implementare con la lista_inp di prima
def is_pari(lista_inp) ->list[int]:
    """
    questa funziona calcola se il valore messo è pari o dispari assegnandogli True o False
    """
    i = 0
    while not len(lista_inp) == i:
        lista_pos = []
        ris = lista_inp[i,i] % 2
        lista_pos[i,i].append(ris)
        if ris == 0:
            lista_pos[i,i].append(ris)
            i += 1

    return lista_pos
lista_inp = input_lista()
lista_pos = is_pari(lista_inp)
print(lista_pos)

#funzione 3
#def somma_quadrati(lista_inp: list[int]) -> int:
#    lista_inp = input_lista(lista_inp)
#    ris = is_pari()