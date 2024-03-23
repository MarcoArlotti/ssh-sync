"""
Gestione di una Azienda:

Immagina di dover gestire le risorse umane e finanziarie di un'azienda con dipendenti e progetti. Crea un programma che:

1. Inizializza una lista di dizionari, ognuno rappresentante un dipendente con nome, ruolo e stipendio iniziale.
2. Stampa la lista di dipendenti.
3. Aggiungi un nuovo progetto alla tua azienda con un budget iniziale e costo orario per ora di lavoro su di esso.
4. Assegna a ciascun dipendente un impegno in ore su questo nuovo progetto, sottraendo dal budget del progetto 
    il costo dei dipendenti per le ore svolte e sommando allo stipendio iniziale i compensi accessori per i progetti su cui ha lavorato.
5. Stampa la lista dei dipendenti con i relativi stipendi totali e le ore lavorate per ciascun progetto.
6. Stampa le ore lavorate totali e il budget rimanente per ogni progetto.

Questo esercizio richiede una gestione avanzata delle liste e dei dizionari, tenendo conto sia delle risorse umane che di quelle finanziarie. 
Buona gestione aziendale!
"""
lista_dipendenti = []
lista_progetti = []
def main():
    scelta = input(str("1\n2\n3\n4\n5\n6\n\n"))
    match scelta:
        case "1":
            crea_dipendente()
        case "2":
            print_solo_nomi_dipendenti()
        case "3":
            aggiungi_progetto_e_costo_orario()
        case "4":
            assegna_impiego(lista_dipendenti)
#        case "5":
#            print_dipendenti_e_stipendi(): #TODO
#        case "6":
#            print_ore_lavorate_tot_e_budget(): #TODO

def crea_dipendente():
    nome = str(input("inserire il nome del dipendente che si vuole aggiungere\n\n"))
    #ruolo = str(input("inserire che ruolo assegnargli\n\n"))
    #stip_iniz = float(input("inserire lo stipendio iniziale da assegnarli\n\n"))

    dipendente = {
        "nome":nome,
        #"ruolo":ruolo, #TODO da cavare il commento!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        #"stipendio_iniziale":stip_iniz,
    }
    lista_dipendenti.append(dipendente)



def print_solo_nomi_dipendenti():
    print("lista dipendenti;\n")
    for i in lista_dipendenti:
        nome = i["nome"]
        print(nome)


def aggiungi_progetto_e_costo_orario():
    nome = str(input("inserire il nome per il progetto\n\n"))
    budget = float(input("inserire il budget del progetto\n\n"))
    costo_all_ora = float(input("inserisci il costo per ora del progetto\n\n"))
    progetto = {
        "costo_all_ora":costo_all_ora, 
        "nome":nome,
        "budget":budget,
    #    "costo_orario":costo_orario, !!!per ogni ora di lavoro viene sottratto tot dal budget
    }
    lista_progetti.append(progetto)


def assegna_impiego(lista_dipendenti):
    dip_scelto = str(input("inserire il nome del dipendente a cui assegnarlo a un progetto\n\n"))
    progetto = str(input("inserire a che progetto assegnare il suddetto dipendente\n\n"))
    for i in lista_dipendenti:
        x = lista_dipendenti[i] #BUG
        n = x["nome"]
        if dip_scelto == n:
            progetto.append(x)
            print(progetto)








while True:
    x = str(input("\n\ncontinuare ad eseguire il programma?\n\nyes,no\n\n"))
    if x == "yes":
        pass
    else:
        print("\n\nuscendo dal programma...")
        break
    main()