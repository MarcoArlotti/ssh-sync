"""
1) Leggi il file in input
2) Calcola il prezzo scontato e aggiungetelo al dizionario come nel precedente esercizio
3) Ordina le fatture in ordine decrescente con il prezzo scontato come criterio di ordinamento
4) Salva la lista nel file output_json.json
"""
import json
def aggiungi_importo(persona):

    importo = persona["importo"]

    sconto_fattura = persona["sconto_fattura"]
    scontato = (importo * sconto_fattura)/100 #calcolo della percentuale
    tot = importo - scontato
    persona["importo_scontato"] = tot


with open("es_34_dati_input.json","r") as file_input:

    try:
        fatture = json.load(file_input)
        for persona in fatture:
            nome = persona["id"]
            importo = persona["importo"]
            sconto_fattura = persona["sconto_fattura"]
            print(f"la {nome} ha un importo di {importo}, con uno sconto della fattura del {sconto_fattura}%")  #stampa delle fatture in ordine

    except:
        fatture = []
        print("non ci sono fatture presenti")
for persona in fatture:
    aggiungi_importo(persona)
for persona in fatture:
    importo_scontato = persona["importo_scontato"]
    #lista_ordinata = riordinamento(importo_scontato)
with open("file_output_es34.json","w") as file_output:
#    file_output = json.dumps(lista_ordinata)