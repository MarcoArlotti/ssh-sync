"""
ESERCIZIO 11
In una copisteria, il costo unitario delle fotocopie varia a seconda del numero da effettuare secondo la seguente tabella:
n.1-19 0,10 euro, n.20-100 0,08 euro, piu di 100 0,05 euro. 
Inoltre se le fotocopie sono da rilegare viene aggiunto un costo di 1,80 euro.
Dati in input il numero di fotocopie da effettuare, il nome del cliente e un indicazione che segnali se il plico è da rilegare, calcola il costo totale e stampa il seguente prospetto:
Gentile Sig. ___ il suo preventivo è di ___ euro compresa la rilegatura. L'ultima riga è da scrivere solo se è richiesta la rilegatura
"""
print("---------------------------------\nda 1-19 = 0,10 euro;\nda 20-100 = 0,08 euro;\npiu di 100 = 0,05 euro;\nin caso di fotocopie rilegate 1,80 euro;\n---------------------------------")
egregio_sign = input("buon dì gregio signore come si chaiama lei? ")
fotocopie = float(input("quante fotocopie? "))
rilegatura = str(input("rilegatura?\n\nsi o no  ?"))
prentivo = float(preventivo)

if rilegatura == si:
    prentivo = 1.80
else:
    prentivo = 0

if fotocopie <= 19:
    prentivo + 0.10
elif 20 <= fotocopie <= 100:
    prentivo + 0.08
elif 100 < fotocopie
    prentivo + 0.05

if rilegatura == si:
    print("Gentile Sig. {egregio_sign} il suo preventivo è di {prentivo} euro compresa la rilegatura")
else:
    print(f"fGentile Sig. {egregio_sign} il suo preventivo è di {prentivo}")