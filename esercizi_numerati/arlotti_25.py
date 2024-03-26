"""
Progettare un applicativo che permetta di gestire il parco auto di una azienda di noleggio.
Si consiglia di creare un dizionario al fine di modellare le caratteristiche/attributi di ogni singola
auto(marca, modello, cilindrata, potenza_kw, anno_immatricolazione, costo_gestione, giorni_affitto, prezzo_giornaliero).
Il parco auto sarà quindi memorizzato in una lista.
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


"""
Percentuale = (parte / totale) × 100
Ad esempio, se il biglietto del concerto costa 30 euro e hai uno sconto del 20%, puoi calcolare quanto è il 20% di 30 euro:
20% di 30 euro = (30 × 20) / 100 = 6 euro.
"""
id = 0 #crea id
parco_auto = []
def chiedi_valori(id,parco_auto) -> list[str]:
                    id = id+1
                    a = str(input("la marca della auto che si vuole aggiungere\n"))    #presa dei valori in input
                    b = str(input("il modello\n"))
                    c = str(input("la cilindrata\n"))
                    d = float(input("la potenza\n"))
                    e = int(input("l'anno di immatricolazione\n"))
                    f = float(input("il costo della gestione\n"))
                    g = int(input("i giorni che starà in affitto\n"))
                    h = float(input("il prezzo giornaliero\n"))
                    auto = {   
                    "marca":a,
                    "modello":b,
                    "cilindrata":c,
                    "potenza_kw":d,
                    "anno_immatricolazione":e,
                    "costo_gestione":f,
                    "giorni_affitto":g,
                    "prezzo_giornaliero":h,
                    "id":id
                    }
                    parco_auto.append(auto)
                    return id
                

def rimuovi_auto(id,parco_auto):
    id_scelto = int(input(""))
    conta = 0
    for auto in parco_auto:
        
            if auto["id"] == id_scelto:
                break
            else:
                conta = conta + 1    
    parco_auto.pop(conta)
    print(parco_auto)
    return parco_auto



def calcolo_bollo(kw):
    #2,58*kw max 100kw
    #3,87*kw oltre 100
    #+20kw oltre i 185kw
    if kw < 101:
        bollo = 2,58*kw
    elif kw > 101:
        eccesso = kw - 100 
        bollo_non_eccesso = 2,58 * kw
        bollo_eccesso = eccesso * 3,87
        bollo = bollo_non_eccesso + bollo_eccesso
    elif kw > 185:
        kw = kw + 20
        eccesso = kw - 100 
        bollo_non_eccesso = 2,58 * kw
        bollo_eccesso = eccesso * 3,87
        bollo = bollo_non_eccesso + bollo_eccesso
    return bollo
        


def profitto_veicolo(parco_auto,auto): #giorno_affitto * (prezzo_giornaliero - IVA) - costo_gestione-bollo
    """
    "marca":a,
    "modello":b,
    "cilindrata":c,
    "potenza_kw":d,
    "anno_immatricolazione":e,
    "costo_gestione":f,
    "giorni_affitto":g,
    "prezzo_giornaliero":h,
    "id":id
    """
    gestione_bollo = auto["gestione_bollo"]
    giorni_affitto= auto["giorni_affitto"]
    prezzo_giornaliero = auto["prezzo_giornaliero"]
    iva = (22 / prezzo_giornaliero) * 100
    profitto = giorni_affitto * (prezzo_giornaliero - iva) - gestione_bollo
    return profitto



while True:
    case = str(input("\ncosa si vuole fare?\n1 per aggiungere/rimuovere un veicolo\n2 calcolo del bollo\n3 visualizzare il profitto di un veicolo\n4 visualizzare il profitto (prima delle tasse) del parco auto"))
    match case:
        case "1":
            scelta = str(input("\nsi vuole rimuovere o aggiungere?\n(SCRIVERE \"rimuovere\" o\"aggiungere\")\n\n"))
            if scelta == "aggiungere": #caso che si vuole aggiungere un auto
                
                
                id = chiedi_valori(id,parco_auto)
                print(f"l'auto che è appena stata creata gli è stata assegnata l'id :{id}")
                
                print(parco_auto)


            elif scelta == "rimuovere":

                print("quale auto si vuole rimuovere?\nscrivere l'id dell'auto:")
                
                parco_auto = rimuovi_auto(id,parco_auto)
        case "2":
            for auto in parco_auto:
                kw = auto["potenza_kw"]
                bollo = calcolo_bollo(kw)
                id_momentaneo = auto["id"]
                print(f"il bollo dell'auto con id: {id_momentaneo} è di: {bollo} euro")
        case "3":
            for auto in parco_auto:
                id_momentaneo = auto["id"]
                profitto = profitto_veicolo(parco_auto,auto)
                print(f"il profitto è di: {profitto}, dell'auto di id: {id_momentaneo}")
                
                tot = profitto + tot
        case "4":
            print(f"il profitto totale è di {tot}")