"""
Scrivere una programma che letto da file JSON una lista di dizionari contenenti le fatture di n utenti così formate:
{"id":"id_utente",
"importo":128.54,
"sconto_fattura":15}
svolga le seguenti funzioni:
1) Mostri tutte le fatture 
2) Permetta di aggiungere ad una fattura selezionata una nuova chiave "importo_scontato" al quale associa il valore dell'importo scontato in base alla percentuale indicata alla chiave "sconto_fattura";
3) Permetta di aggiungere una fattura alla lista (aggiornando il file JSON)

- Definire apposite funzioni di lettura e scrittura da/sul file JSON.
- Definire eventuali altre funzioni utili ai fini dell'esercizio.


"""
import json
#python -> json = .dumps
#json -> python = .loads
fatture = [
{"id":"Monticelli",
"importo":245.78,
"sconto_fattura":10
},
{"id":"Kola",
"importo":325.71,
"sconto_fattura":12
},
{"id":"romagna",
"importo":245.78,
"sconto_fattura":8
},
{"id":"Bilancioni",
"importo":245.78,
"sconto_fattura":15
},
{"id":"Sanchi",
"importo":245.78,
"sconto_fattura":5
},
{"id":"Pontellini",
"importo":245.78,
"sconto_fattura":18
},
{"id":"Clementi",
"importo":245.78,
"sconto_fattura":20
},
{"id":"Arlotti",
"importo":245.78,
"sconto_fattura":19
},
{"id":"Nedria",
"importo":245.78,
"sconto_fattura":7
},
{"id":"Santini",
"importo":245.78,
"sconto_fattura":22
},
]




def main(fatture):
    crea_json(fatture)
    fatture = converti_py_in_json(fatture)
    aggiunta_importo_scontato(fatture)
    crea_nuova_fattura_e_aggiorna_json(fatture)

def crea_json(fatture):
    
    with open("dati_es_33.json", "w") as file_json:
        json.dump(obj=fatture, fp=file_json, indent=4)  #trasferito il dizionario 
                                                        #"fatture" ---> dati_es_33.json


def converti_py_in_json(fatture):
    with open("dati_es_33.json","r") as file_json:
        try:
            fatture = json.load(file_json)
            for persona in fatture:
                nome = persona["id"]
                importo = persona["importo"]
                sconto_fattura = persona["sconto_fattura"]
                print(f"la {nome} ha un importo di {importo}, con uno sconto della fattura del {sconto_fattura}%")  #stampa delle fatture in ordine

        except:
            fatture = []
            print("non ci sono fatture presenti")
        

    return fatture



def aggiungi_importo(persona):

    importo = persona["importo"]

    sconto_fattura = persona["sconto_fattura"]
    scontato = (importo * sconto_fattura)/100 #calcolo della percentuale
    tot = importo - scontato
    persona["importo_scontato"] = tot



def aggiunta_importo_scontato(fatture):
    scelta = str(input("\ninserire l'id (il cognome) della persona che gli si vuole calcolare l'importo scontato\n\n"))
    for persona in fatture:
        cognome = persona["id"]
        if cognome == scelta:
            aggiungi_importo(persona)
            print(persona)
            break        


def crea_nuova_fattura_e_aggiorna_json(fatture):
    id = str(input("inserire l'id (il cognome) della persona che si vuole aggiumgere\n\n"))
    importo = str(input("inserire l'importo\n\n"))
    sconto_fattura = str(input("inserire o sconto fattura\n\n"))
    persona = {
        "id":id,
        "importo":importo,
        "sconto_fattura":sconto_fattura
    }
    fatture.append(persona)
    crea_json(fatture)

main(fatture)