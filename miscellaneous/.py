

"""
Gestione di una Azienda
Immagina di dover gestire le risorse umane e finanziarie di un'azienda con dipendenti e progetti. Crea un programma che:

1   Inizializza una lista di dizionari, ognuno rappresentante un dipendente con nome, ruolo e stipendio iniziale.
    Stampa la lista di dipendenti.
2       Aggiungi un nuovo progetto alla tua azienda con un budget iniziale e costo orario per ora di lavoro su di esso.
        Assegna a ciascun dipendente un impegno in ore su questo nuovo progetto, sottraendo dal budget del progetto il costo dei
        dipendenti per le ore svolte e sommando allo stipendio iniziale i compensi accessori per i progetti su cui ha lavorato.
3           Stampa la lista dei dipendenti con i relativi stipendi totali e le ore lavorate per ciascun progetto.
            Stampa le ore lavorate totali e il budget rimanente per ogni progetto.
4               Assegna a ciascun dipendente un impegno in ore su questo nuovo progetto, sottraendo dal budget del progetto 
                il costo dei dipendenti per le ore svolte e sommando allo stipendio iniziale i compensi accessori per i progetti su cui ha lavorato.
5                   Stampa la lista dei dipendenti con i relativi stipendi totali e le ore lavorate per ciascun progetto.
6                       Stampa le ore lavorate totali e il budget rimanente per ogni progetto.
Questo esercizio richiede una gestione avanzata delle liste e dei dizionari,
tenendo conto sia delle risorse umane che di quelle finanziarie. Buona gestione aziendale!
"""
dipendenti = []
progetti = []
dipendenti_in_carico = []
ore = []
while True:
    ram_ass_dipendenti = 0
    scelta = str(input("scegliere da 1-4\n1    per inserire un nuovo dipendente\n2    per un controllo dei dipendenti\n3    per aggiungere un nuovo progetto\n4    per assegnare delle ore dai dipendenti ad un progetto\n5    per effettuare un controllo dei budget dei vari progetti\n6    per terminare il programma "))
    match scelta:
        case "1":
           
            dipendente_singolo = {
                "nome_dipendente":"fabio",
                "ruolo":"python",
                "stipendio":1000,
                "ore_in_carico":[2,1],
            }
            dipendente_singolo = {
                "nome_dipendente":"sanchi",
                "ruolo":"python",
                "stipendio":1000,
                "ore_in_carico":[4,3],
            }

        case "2":
            print(f"lista dei dipendenti{dipendenti}")

        case"3":
            nome_progetto = str(input("inserire nome del nuovo progetto "))
            budget = float(input("inserire budget progetto  "))
            costo_per_ore = float(input("inserire costo di un dipendente all'ora sul progetto   "))        
            while True:
                si_o_no = str(input("assegnare un dipendente al progetto?\nyes\nno\n"))
                if si_o_no == "yes":
                    dipendente_assegnato = str(input("inserire nome del dipendente da assegnargli il lavoro nel progetto    "))
                    if dipendente_assegnato == dipendente_singolo["nome_dipendente"]:
                        dipendente_assegnato.append(dipendenti_in_carico)
                    else:
                        print("lavoratore non trovato")
                else:
                    break  
            progetto = {
                "nome_progetto":"python_blyat",
                "budget_del_progetto":10000,
                "costo_orario":300,
                "lista_di_dipendenti_che_ne_lavorano_dentro":[dipendente_singolo,dipendente_singolo],
                }
            progetto = {
                "nome_progetto":"assembly",
                "budget_del_progetto":12000,
                "costo_orario":400,
                "lista_di_dipendenti_che_ne_lavorano_dentro":[dipendente_singolo,dipendente_singolo],
                }
            
            progetti.append(progetto)
        
        
        case"4":
            progetto_selezionato = str(input("inserire il nome del progetto "))
            
            if  nome_progetto in progetti == progetto_selezionato:
                costo_del_progetto_in_ore = float(input("inserire il costo del progetto in ore  ")) 
                ore = int(input("inserire quante ore assegnare ai dipendenti nel progetto "))
                x =  x + ore
                tot_tra_budget_e_ore = costo_del_progetto_in_ore * 

                tot_tra_budget_e_ore -= progetto["budget_del_progetto"]

                #tot_tra_budget_e_ore + 
        case"5":
            print(dipendenti_in_carico)
            print(stipendio)

        case "6":
            break
