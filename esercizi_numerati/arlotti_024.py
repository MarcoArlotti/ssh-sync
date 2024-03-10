"""
Gestione di una Azienda:

Immagina di dover gestire le risorse umane e finanziarie di un'azienda con dipendenti e progetti. Crea un programma che:

1. Inizializza una lista di dizionari, ognuno rappresentante un dipendente con nome, ruolo e stipendio iniziale.
2. Stampa la lista di dipendenti.
3. Aggiungi un nuovo progetto alla tua azienda con un budget iniziale e costo orario per ora di lavoro su di esso.
4. Assegna a ciascun dipendente un impegno in ore su questo nuovo progetto, sottraendo dal budget del progetto il costo dei dipendenti per le ore svolte e sommando allo stipendio iniziale i compensi accessori per i progetti su cui ha lavorato.
5. Stampa la lista dei dipendenti con i relativi stipendi totali e le ore lavorate per ciascun progetto.
6. Stampa le ore lavorate totali e il budget rimanente per ogni progetto.

Questo esercizio richiede una gestione avanzata delle liste e dei dizionari, tenendo conto sia delle risorse umane che di quelle finanziarie. Buona gestione aziendale!
"""


def main():
    pass
def choice():
    scelta = input(str("1\n2\n3\n4\n5\n6\n\n"))
    match scelta:
        case "1":
            crea_dipendente(): #TODO
        case "2":
            print_solo_nomi_dipendenti(): #TODO
        case "3":
            aggiungi_dipendenti(): #TODO
        case "4":
            assegna_impiego(): #TODO
        case "5":
            print_dipendenti_e_stipendi(): #TODO
        case "6":
            print_ore_lavorate_tot_e_budget(): #TODO
