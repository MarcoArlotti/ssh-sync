#ESERCIZIO 9
#Dato in input il numero di secondi dire a quanti anni, mesi, giorni, ore, minuti e secondi corrispondono
secondi = int(input("INSERIRE IL TEMPO; "))
secondi_anni = int(secondi // 365)
resto_anni = int(secondi % 365)

secondi_MESI = int(resto_anni // 30)
resto_MESI = int(resto_anni % 30)

secondi_ore = int(resto_MESI // 60)
resto_ore = int(resto_MESI % 60)

secondi_minuti = int(resto_ore // 60)
resto_minuti = int(resto_ore % 60)

secondi_secondi = resto_minuti

print(f"anni:"{secondi_anni}"mesi:"{secondi_MESI}"ore:"{secondi_ore}"minuti:"{secondi_minuti}"secondi:"{secondi_secondi})