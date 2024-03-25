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
id = 0 #crea id
parco_auto = []
def chiedi_valori(id,parco_auto) -> list[str]:
                    id = id+1
                    a = str(input("la marca della auto che si vuole aggiungere\n"))    #presa dei valori in input
                    b = str(input("il modello\n"))
                    c = str(input("la cilindrata\n"))
                    d = str(input("la potenza\n"))
                    e = str(input("l'anno di immatricolazione\n"))
                    f = str(input("il costo della gestione\n"))
                    g = str(input("i giorni che starà in affitto\n"))
                    h = str(input("il prezzo giornaliero\n"))
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
        bollo = 2,58*kw
        




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
                calcolo_bollo(kw)