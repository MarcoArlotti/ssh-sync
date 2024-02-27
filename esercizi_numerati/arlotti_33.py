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
fabio = [
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
x = json.dumps(fabio)
with open("file_json.json","w") as file_json:
    try:
        mylist = json.load(file_json)
    except:
        mylist = []
mylist.append(fabio)
with open("file_json.json","w") as file_json:
    json.dump(mylist,file_json,indent = 4)