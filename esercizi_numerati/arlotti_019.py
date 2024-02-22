"""
Esercizio 19
Dato in input un numero scritto con sistema di numerazione decimale (intero), 
calcolare la sua conversione in binario. Dato che la stampa a video del numero deve avvenire 
in ordine inverso da quello del calcolo, usare una lista per stampare il valore corretto.
"""
numeri_bin = []
decimale = int(input("inserire numero decimale  "))
resto = 0
binario = 0
while resto != 1:
    resto = decimale % 2
    if resto == 0:
        binario = 0
    else:
        binario = 1
    numeri_bin.append(binario)
    passaggio2 = decimale // 2
numeri_bin.reverse()
print(numeri_bin)