"""
Esercizio 1 – Voti sufficienti
Chiesti all’utente 5 voti in input dire quanti di questi sono sufficienti su quelli
considerati validi. I voti sono considerati validi se compresi tra 1 e 10.
"""
v1 = int(input("mettere il primo voto:  "))
v2 = int(input("mettere il secondo voto:  "))
v3 = int(input("mettere il terzo voto:  "))
v4 = int(input("mettere il quarto voto:  "))
v5 = int(input("mettere il quinto voto:  "))
insuff = 0

suffic = 0

if 10 < v1 < 1 and 10 < v2 < 1 and 10 < v3 < 1 and 10 < v4 < 1 and 10 < v5 < 1:
    print ("INSERIRE VOTI TRA 1 E 10!")

if v1 <= 5:
    insuff = insuff + 1
else:
    suffic = suffic + 1

if v2 <= 5:
    insuff = insuff + 1
else:
    suffic = suffic + 1

if v3 <= 5:
    insuff = insuff + 1
else:
    suffic = suffic + 1

if v4 <= 5:
    insuff = insuff + 1
else:
    suffic = suffic + 1

if v5 <= 5:
    insuff = insuff + 1
else:
    suffic = suffic + 1

print(f"ci sono {insuff} insufficenze")
print(f"ci sono {suffic} sufficenze")