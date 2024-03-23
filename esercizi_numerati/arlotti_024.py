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
    scelta = input(str("1 crea dip\n2 print solo nomi\n3 aggiungi progetto e costo orario\n4 assegna impiego \n5 print dipendenti e stipendi (solo non assegnati)\n6 print ore lavorate totali e budget di un progetto e i dipendenti assegnati\n con relativi nomi e stipendi\n\n"))
    match scelta:
        case "1":
            crea_dipendente(lista_dipendenti)
        case "2":
            print_solo_nomi_dipendenti(lista_dipendenti)
        case "3":
            aggiungi_progetto_e_costo_orario(lista_progetti)
        case "4":
            assegna_impiego(lista_dipendenti,lista_progetti)
        case "5":
            print_dipendenti_e_stipendi(lista_dipendenti)
        case "6":
            print_ore_lavorate_tot_e_budget(lista_progetti)


def crea_dipendente(lista_dipendenti):
    nome = str(input("inserire il nome del dipendente che si vuole aggiungere\n\n"))
    ruolo = str(input("inserire che ruolo assegnargli\n\n"))
    stip_iniz = float(input("inserire lo stipendio iniziale da assegnarli\n\n"))

    dipendente = {
        "nome":nome,
        "ruolo":ruolo,
        "stipendio_iniziale":stip_iniz,
        "stipendio_finale":0
    }
    lista_dipendenti.append(dipendente)



def print_solo_nomi_dipendenti(lista_dipendenti):
    print("lista dipendenti;\n")
    for i in lista_dipendenti:
        nome = i["nome"]
        print(nome)
        


def print_dipendenti_e_stipendi(lista_dipendenti):
    print("lista dipendenti e stipendi;\n")
    for dipendente in lista_dipendenti:
        nome = dipendente["nome"]
        ruolo = dipendente["ruolo"]
        stipendio_iniziale = dipendente["stipendio_iniziale"]
        print(f"nome:{nome}, ruolo:{ruolo}, stipendio:{stipendio_iniziale} Euro.\n") # non va con quelli assegnati



def aggiungi_progetto_e_costo_orario(lista_progetti):
    nome = str(input("inserire il nome per il progetto\n\n"))
    budget = float(input("inserire il budget del progetto\n\n"))
    costo_all_ora = float(input("inserisci il costo per ora del progetto\n\n"))
    progetto = {
        "costo_all_ora":costo_all_ora, 
        "nome":nome,
        "budget":budget,  
        "dipendenti_assegnati":[]
    }
    lista_progetti.append(progetto)


def assegna_impiego(lista_dipendenti,lista_progetti):
    dip_scelto = str(input("inserire il nome del dipendente a cui assegnarlo a un progetto\n\n"))
    progetto_scelto = str(input("inserire a che progetto assegnare il suddetto dipendente\n\n"))

    dipendente_trovato = False

    for dipendente in lista_dipendenti:
        
        if dip_scelto == dipendente["nome"]:

            progetto_trovato = False
            for progetto in lista_progetti:
                if progetto["nome"] == progetto_scelto:
                    print(f"Trovato il dipendente {dip_scelto}")
                    progetto_trovato = True
                    break

            if progetto_trovato == False:
                print(f"Non trovato il progetto {progetto_scelto}")

            print(f"Trovato il dipendente {dip_scelto}")
            dipendente_trovato = True
            break


    if dipendente_trovato == False: #se il DIPENDENTE non viene trovato
        print(f"Non trovato il dipendente {dip_scelto}")
    elif progetto_trovato == False: #se il PROGETTO non viene trovato
        print(f"Non trovato il progetto {progetto_scelto}")
    elif progetto_trovato == True and dipendente_trovato == True:
        #aggiungere ore da assegnargli al dipendente

        ore_da_assegnare = int(input("inserire quante ore di lavoro assegnare per il suddetto dipendente(in ore, senza i minuti)"))

        dipendente["ore_assegnate"] = ore_da_assegnare #aggiunta una nuova KEY al dizionario dipendente (solo il dipendente scelto)

        progetto["dipendenti_assegnati"].append(dipendente)

        print(lista_progetti)

    for progetto in lista_progetti:
        for dipendente_asseganto in progetto["dipendenti_assegnati"]:
            #calcolo ore assegnate(del dipendente)*costo all'ora(del progetto) -> 
            #aggiungere il risultato alla chiave "costo_calcolato"(da aggiungre la chiave sul momento) e aggiornare lo stipendio dei dipendenti
            ore_lavoro_di_un_dipendente = dipendente_asseganto["ore_assegnate"]
            costo_all_ora_progetto = progetto["costo_all_ora"]

            momentaneo = ore_lavoro_di_un_dipendente * costo_all_ora_progetto # ore di lav * euro_all'ora -> momentaneo + stip_iniziale
            
            #diminuire il budget
            budget_prima = progetto["budget"]
            progetto["budget"] = budget_prima - momentaneo


            stip_iniziale = dipendente_asseganto["stipendio_iniziale"]
            momentaneo = momentaneo + stip_iniziale
            """
            thisdict =	{
            "brand": "Ford",
            "model": "Mustang",
            "year": 1964
            }
            thisdict["year"] = 2018
            """
            dipendente["stipendio_finale"] = momentaneo #aggiornato lo stipendio finale
            return lista_dipendenti,lista_progetti





def print_ore_lavorate_tot_e_budget(lista_progetti):
    print("lista dei progetti;\n\n")
    for progetto in lista_progetti:
        
        costo_all_ora_prog = progetto["costo_all_ora"]
        budget_prog = progetto["budget"]
        nome_prog = progetto["nome"]
        print(f"nome:{nome_prog}, budget:{budget_prog}, costo all'ora:{costo_all_ora_prog}.")

        dipendenti_assegani = progetto["dipendenti_assegnati"]
        print("lista dei dipendenti;\n\n")

        for dipendente in dipendenti_assegani:



            nome = dipendente["nome"]
            stipendio = dipendente["stipendio_finale"]
            ruolo = dipendente["ruolo"]
            print(f"nome:{nome}, stipendio:{stipendio}, ruolo: {ruolo}.\n")


while True:
    x = str(input("\n\ncontinuare ad eseguire il programma?\n\nyes,no\n\n"))
    if x == "yes":
        print()
        pass
    else:
        print("\n\nuscendo dal programma...")
        break
    main()