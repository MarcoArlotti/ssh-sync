"""
Scrivere un programma che permetta la gestione di una lista della spesa. Esso deve prevedere un menu così formato:


Scegliere l'opzione desiderata:
1) Visualizza lista
2) Aggiungi item e quantità
3) Modifica quantità di un item
4) Rimuovi item
5) Esci
Scelta:_
"""
lista = []
quantità = []
print("INSERIRE UN NUMERO IN BASE ALLA SCELTA\n1) Visualizza lista\n2) Aggiungi item e quantità\n3) Modifica quantità di un item\n4) Rimuovi item\n5) Esci)")
command = str(input(""))
i = 0

while i == 0:
   match command:
      case '1':
         print(lista)
         print(quantità)
         print("INSERIRE UN NUMERO IN BASE ALLA SCELTA\n1) Visualizza lista\n2) Aggiungi item e quantità\n3) Modifica quantità di un item\n4) Rimuovi item\n5) Esci)")
         command = str(input(""))
      case '2':
         coso = input("inserisci prodotto da aggiungere  ")
         lista.append(coso)
         quant = int(input("inserisci numero di prodotti "))
         quantità.append(quant)
         print("INSERIRE UN NUMERO IN BASE ALLA SCELTA\n1) Visualizza lista\n2) Aggiungi item e quantità\n3) Modifica quantità di un item\n4) Rimuovi item\n5) Esci)")
         command = str(input(""))
      case '3':
         che_item = int(input("mettere il numero della posizione da cambiare della lista  "))
         lista.pop(che_item)
         cambio = int(input("mettere quantità nuova   "))
         lista.insert(che_item,cambio)
         print("INSERIRE UN NUMERO IN BASE ALLA SCELTA\n1) Visualizza lista\n2) Aggiungi item e quantità\n3) Modifica quantità di un item\n4) Rimuovi item\n5) Esci)")
         command = str(input(""))
      case '4':
         che_item2 = int(input("mettere il numero della posizione da cancellare della lista  "))
         lista.pop(che_item)
         print("INSERIRE UN NUMERO IN BASE ALLA SCELTA\n1) Visualizza lista\n2) Aggiungi item e quantità\n3) Modifica quantità di un item\n4) Rimuovi item\n5) Esci)")
         command = str(input(""))
      case '5':
         break