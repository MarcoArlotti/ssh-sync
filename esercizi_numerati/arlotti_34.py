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


with open("dati_es_34.json","r") as file_input:

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
def riordina(fatture):
    return fatture["sconto_fattura"]


aggiungi_importo(persona)
lista_ordinata = fatture.sort(key=riordina)
print(lista_ordinata)
"""
def myFunc(e):
  return e['year']

cars = [
  {'car': 'Ford', 'year': 2005},
  {'car': 'Mitsubishi', 'year': 2000},
  {'car': 'BMW', 'year': 2019},
  {'car': 'VW', 'year': 2011}
]

cars.sort(key=myFunc)
"""
#with open("file_output_es34.json","w") as file_output:
#    file_output = json.dump(fatture)
#    