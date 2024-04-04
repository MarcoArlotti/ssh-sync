"""
1) Leggi il file in input
2) Calcola il prezzo scontato e aggiungetelo al dizionario come nel precedente esercizio
3) Ordina le fatture in ordine decrescente con il prezzo scontato come criterio di ordinamento
4) Salva la lista nel file output_json.json
"""
import json
def aggiungi_importo(fatture):
  for persona in fatture:
      importo = persona["importo"]

      sconto_fattura = persona["sconto_fattura"]
      scontato = (importo * sconto_fattura)/100 #calcolo della percentuale
      tot = importo - scontato
      persona["importo_scontato"] = tot

def riordina(fatture):
    return fatture["sconto_fattura"]

def calcolo_prezzo():
  with open("dati_es_34.json","r") as file_input:
    fatture = json.load(file_input)
    aggiungi_importo(fatture)
    for persona in fatture:
        nome = persona["id"]
        importo = persona["importo"]
        sconto_fattura = persona["sconto_fattura"]
        print(f"la {nome} ha un importo di {importo}, con uno sconto della fattura del {sconto_fattura}%")  #stampa delle fatture in ordine

  return fatture
  




fatture = calcolo_prezzo()
moment =  []
with open("file_output_es34.json","w") as file_json:
  json.dump(moment,file_json,indent=4)
  open("file_output_es34.json")
for persona in fatture:
   persona["importo_scontato"]
 
    #json.dump(fatture,file_json,indent=4)
