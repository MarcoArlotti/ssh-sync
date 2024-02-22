# ESERCIZIO 8
#Dato in input un numero n di pasticcini, dire quante scatole da 5 pezzi, da 3 pezzi e da 1 pezzo servono a contenerli. 
#Nota bene:
#- Utilizzare il minor numero di scatole possibili, non lasciando nessuna scatola parzialmente vuota.
pasticcini = int(input("quanti pasticcini?:"))

pasticcini

scatola5 = pasticcini / 5
scatola3 = pasticcini % 5

scatola3 = pasticcini / 3
scatola1 = pasticcini % 3

scatola1 = pasticcini / 1
print("scatola da 5"scatola5+"scatola da 3"scatola3+"scatola3+scatole da 1"scatola1)