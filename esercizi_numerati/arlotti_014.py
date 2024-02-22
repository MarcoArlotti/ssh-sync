"""
Scrivi un programma che calcoli il valore della circonferenza e quello dell'area di 
tutti i cerchi con raggio compreso tra 1 e 20.
"""
for raggio in range(0,21):
    circonferenza = (raggio + raggio)* 3.14
    print("///////////////////////////////////////////////////////////////")
    print(f"la tua circonferenza è {circonferenza}")

for raggio2 in range(0,21):
    area = (raggio2 + raggio2)* 3.14
    print("---------------------------------------------------------------")
    print(f"la tua area è {area}")