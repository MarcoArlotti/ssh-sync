"""
Progettare un applicativo che permetta di gestire il parco auto di una azienda di noleggio.
Si consiglia di creare un dizionario al fine di modellare le caratteristiche/attributi di ogni singola
auto(marca, modello, cilindrata, potenza_kw, anno_immatricolazione, costo_gestione, giorni_affitto, prezzo_giornaliero). Il parco auto sarà quindi memorizzato in una lista.
L'applicativo dovrà permettere:
1)aggiunta/rimozione di un veicolo
2)Calcolo del bollo 
3)Profitto del veicolo[giorno_affitto*(prezzo_giornaliero-IVA)- costo_gestione-bollo]
4)Profitto (prima delle tasse) di tutto il parco auto

Per il calcolo del bollo si consideri:
2,58 euro a kW fino a 100kW
3,87 euro per i kW eccedenti
aggiungere 
20 a kW oltre i 185kW 
"""
lista_auto = []
while True:
    case = str(input("\ncosa si vuole fare?\n1 per aggiungere/rimuovere un veicolo\n2 calcolo del bollo\n3 visualizzare il profitto di un veicolo\n4 visualizzare il profitto (prima delle tasse) del parco auto"))
    match case:
        case "1":
            scelta = str(input("\nsi vuole rimuovere o aggiungere?\n(SCRIVERE \"rimuovere\" o\"aggiungere\")\n\n"))
            if scelta == "aggiungere": #caso che si vuole aggiungere un auto
                def chiedi_valori() -> list[str]:
                    a = str(input("la marca della auto che si vuole aggiungere\n"))    #presa dei valori in input
                    b = str(input("il modello\n"))
                    c = str(input("la cilindrata\n"))
                    d = str(input("la potenza\n"))
                    e = str(input("l'anno di immatricolazione\n"))
                    f = str(input("il costo della gestione\n"))
                    g = str(input("i giorni che starà in affitto\n"))
                    h = str(input("il prezzo giornaliero\n"))
                    return [a,b,c,d,e,f,g,h]
                chiedi_valori()
                auto = {   #creazione del dizionario
                    "marca":a,
                    "modello":b,
                    "cilindrata":c,
                    "potenza_kw":d,
                    "anno_immatricolazione":e,
                    "costo_gestione":f,
                    "giorni_affitto":g,
                    "prezzo_giornaliero":h,
                }
                lista_auto.append(auto)
            else:
                print("quale auto si vuole rimuovere?\nsrivere marca, modello, cilindrata, potenza, anno della matricolazione, costo della gestione, giorni in afitto e prezzo giornaliero")
                chiedi_valori             