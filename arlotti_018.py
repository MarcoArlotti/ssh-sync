"""
Esercizio 18
Scrivere un programma che passati in input n valori popoli una lista.
In seguito scorre lista con un for e ne calcola il valore medio, il massimo e il minimo.
"""
list_popol = []
somma = 0
cicli = int(input("inserisci numero di cicli  "))
for i in range(cicli):
    dato = int(input("inserire dato da aggiungere alla lista    "))
    list_popol.append(dato)
    somma = dato + somma
tot = somma / cicli
print(f"la media è {tot}")
min_ = min(list_popol)
max_ver = max(list_popol)
print(f"il min è {min_}, il max è {max_ver}")