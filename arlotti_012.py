"""
Dati in input n valori, calcolarne la somma.
Suggerimenti....
Si chieda quanti valori si vogliono inserire quando inizia il programma, si inizializzi la variabile di somma a zero prima che inizi il ciclo.
"""
numeri_scelti = int(input("inserire quanti numeri "))
# calcoli = 0
totale = 0
for i in range(numeri_scelti):
    numero = int(input("inserire valore "))
    totale = totale + numero    
print(f"la tua somma totale è di {totale}")
