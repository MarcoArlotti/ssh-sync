# File in Python
## Apertura di un file
### `open()`
#### Parametri
##### `file` - Il percorso del file come stringa. Può essere un percorso assoluto o relativo.
##### `mode` - Il modo in cui il file deve essere aperto. Può essere una combinazione dei seguenti:
###### 'r' - Apre il file in modalità lettura. Questa è l'impostazione predefinita.
###### 'w' - Apre il file in modalità scrittura. Crea un nuovo file se non esiste o tronca il file se esiste.
###### 'a' - Apre il file in modalità append. Crea un nuovo file se non esiste.
###### 'b' - Apre il file in modalità binaria.
###### '+' - Apre il file per aggiornamento (lettura e scrittura).
### `with` - Usato per gestire automaticamente la chiusura del file. Questo garantisce che il file venga chiuso quando il blocco di codice viene lasciato.
## Lettura di un file
### `read(size)` - Legge l'intero file se size non è specificato. Se size è specificato, legge al massimo size caratteri.
### `readline(size)` - Legge una linea del file se size non è specificato. Se size è specificato, legge al massimo size caratteri.
### `readlines()` - Legge tutte le linee del file e le restituisce come una lista di stringhe.
## Scrittura in un file
### `write(str)` - Scrive la stringa str nel file e restituisce il numero di caratteri scritti.
### `writelines(list)` - Scrive una lista di stringhe nel file. Le stringhe vengono scritte nell'ordine in cui appaiono nella lista.
## Chiusura di un file
### `close()` - Chiude il file. Un file chiuso non può essere letto o scritto.
## Altre operazioni sui file
### `seek(offset)` - Cambia la posizione del cursore nel file.
### `tell()` - Restituisce la posizione attuale del cursore nel file.
### `flush()` - Svuota il buffer di scrittura del file.
### `fileno()` - Restituisce un intero che rappresenta il descrittore del file.
### `isatty()` - Restituisce True se il file è collegato a un dispositivo tty.
### `truncate(size)` - Ridimensiona il file alla dimensione specificata.