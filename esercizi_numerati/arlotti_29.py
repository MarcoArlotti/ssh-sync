"""
Scrivere una funzione che ricevuta in ingresso una lista di dizionari contenenti le fatture di n utenti così formate:
{"id":"id_utente",
"importo":128.54,
"sconto_fattura":15}
svolga le seguenti funzioni:
1) Aggiunga ad ogni dizionario una nuova chiave "importo_scontato" al quale associa il valore dell'importo scontato in base alla percentuale
    indicata alla chiave "sconto_fattura";
2) Restituisca una lista di float dove il primo elemento è il totale degli importi e il secondo il totale degli importi scontati;
3) Restituisca None se la lista delle fatture è vuota.

La funzione ha la seguente signature:
def calcola_importo(fatture:list[dict])->list[float]|None: ...... 

Si provi la funzione in un programma dove le si dia in ingresso la seguente lista:
"""
fatture=[
{"id":"Monticelli",
"importo":245.78,
"sconto_fattura":10
},
{"id":"Kola",
"importo":325.71,
"sconto_fattura":12
},
{"id":"Romagna",
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
def aggiungi_importo():
    for persone in fatture:
        importo = persone["importo"]

        sconto_fattura = persone["sconto_fattura"]
        scontato = (importo / sconto_fattura)*100 #? non sembra calcolare correttamente la percentuale BUG
        persone["importo_scontato"] = scontato

aggiungi_importo()
print(fatture)