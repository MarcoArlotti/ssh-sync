"""
Scrivere una programma che letto da file JSON una lista di dizionari contenenti le fatture di n utenti così formate:
{"id":"id_utente",
"importo":128.54,
"sconto_fattura":15}
svolga le seguenti funzioni:
1) Mostri tutte le fatture 
2) Permetta di aggiungere ad una fattura selezionata una nuova chiave "importo_scontato" al quale associa il valore dell'importo scontato in base alla percentuale indicata alla chiave "sconto_fattura";
3)Permetta di aggiungere una fattura alla lista (aggiornando il file JSON)

- Definire apposite funzioni di lettura e scrittura da/sul file JSON.
- Definire eventuali altre funzioni utili ai fini dell'esercizio.


"""
import json



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

    crea_file_json(fatture) #done




    aggiungi_fatture(fatture)#TODO
    #aggiungi_importo_scontato()

    

    #aggiungi_fattura()
    #mostra_fatture()



def crea_file_json(fatture):

   with open("dati_es_33.json", "w") as f:
    # usa json.dump per scrivere i dati nel file
    json.dump(fatture, f,indent=4) #crea e formatta per bene i dati
    
def aggiungi_fatture(fatture) -> None:  #mostri la lista "fabio"/"fatture" e aggiunga la key "importo_scontato" al quale associa il valore dell'importo scontato in base alla percentuale 
                                        #indicata alla chiave "sconto_fattura";
   print(fatture)
   choice = input(str("a chi si vuole aggiungere la chiave sconto fatture (id)?"))





def aggiungi_fattura(fatture: list, nome_file: str) -> list:
    pass
def aggiungi_importo_scontato(fatture: list, idx: int) -> list:
    pass
main(fatture)