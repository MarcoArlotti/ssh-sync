"""
Esercizio 3 – Validazione data
Chiesta all’utente una data in input nel formato giorno, mese e anno, memorizzate in
tre variabili separate, dire in output se la data è valida o meno.
Al fine di implementare il programma si ricorda che:
• Gennaio, marzo, maggio, luglio, agosto, ottobre e dicembre hanno 31 giorni
• Aprile, giugno, settembre e novembre hanno 30 giorni
• Febbraio ha 29 giorni se l’anno è bisestile, 28 altrimenti
Usare l’algoritmo sviluppato all’esercizio 2 per verificare se l’anno è bisestile o meno.
"""
giorno = int(imput("mettere giono   "))
mese = int(imput("mettere mese  "))
anno = int(imput("mettere anno  "))
if  giorno > 31 and giorno < 1:
    print(ERRORE NEL GIORNO!)
elif  mese > 12 and mese < 1:
    print(ERRORE NEL MESE!)
elif  anno > 2100 and anno < 1:
    print(ERRORE NEL ANNO!)
gennaio =31
febbraio =29
marzo =31
aprile =30
maggio =31
giugno =30
luglio =31
agosto =31
settembre =30
ottobre =31
novembre =30
dicembre =31

if mese == 1: 
    giorno < 32 and giorno < 1

    else:
        print("mese corretto")
