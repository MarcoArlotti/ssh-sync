# Python

## Esecuzione di file
- **Script Python**: Esegui un file Python come script.
- **Python interattivo**: Usa Python in una shell interattiva.

## Indentazione
- **Blocchi di codice**: I blocchi di codice sono denotati dall'indentazione.
- **Coerenza**: L'indentazione coerente è fondamentale in Python.

## I/O
- **print()**: Emette dati sulla console.
    - **strings**: Stampa dati di testo.
    - **numbers**: Stampa dati numerici.
    - **variables**: Stampa il valore delle variabili.
- **input()**: Legge i dati dalla console.
    - **strings**: Legge i dati di testo.
    - **conversione del tipo di dati**: Converte i dati di input nel tipo di dati richiesto.

## Variabili
- **assegnazione (=)**: Assegna un valore a una variabile.
- **nomi delle variabili**: Nomi dati alle variabili per l'identificazione.
- **variabili globali e locali**: Variabili definite nell'ambito globale e all'interno di una funzione rispettivamente.

## Commenti
- **commenti su una sola linea**: Commenti che coprono solo una linea.
- **commenti su più linee**: Commenti che coprono più linee.

## Tipi di dati
- **type()**: Ottieni il tipo di dati di una variabile.
- **Casting**:
    - **str()**: Converte una variabile in una stringa.
    - **int()**: Converte una variabile in un intero.
    - **float()**: Converte una variabile in un float.
- **str**:
    - **slicing**: Estrae parti di una stringa.
    - **len()**: Ottieni la lunghezza di una stringa.
    - **concatenazione**: Combina due stringhe.
    - **f-strings**: Formatta le stringhe in Python.
    - **caratteri di escape**: Caratteri speciali nelle stringhe.
- **bool**:
    - **True**: Valore booleano True.
    - **False**: Valore booleano False.
- **int**:
    - **operazioni aritmetiche**: Esegui calcoli con interi.
    - **confronto**: Confronta gli interi.
- **float**:
    - **operazioni aritmetiche**: Esegui calcoli con float.
    - **confronto**: Confronta i float.
- **list**:
    - **len()**: Ottieni il numero di elementi in una lista.
    - **append()**: Aggiungi un elemento alla fine di una lista.
    - **remove()**: Rimuovi un elemento da una lista.
    - **insert()**: Aggiungi un elemento in una posizione specifica in una lista.
    - **pop()**: Rimuovi un elemento da una posizione specifica in una lista.
    - **index()**: Trova l'indice di un elemento in una lista.
    - **count()**: Conta il numero di volte che un elemento appare in una lista.
    - **sort()**: Ordina gli elementi in una lista.
        - **reverse=True**: Ordina gli elementi in ordine decrescente.
        - **reverse=False**: Ordina gli elementi in ordine crescente (default).
        - **key**: Specifica una funzione di un argomento per estrarre una chiave di confronto da ciascun elemento della lista (es. `key=len` ordina una lista di stringhe per lunghezza).
    - **reverse()**: Inverti l'ordine degli elementi in una lista.
- **dict**:
    - **values()**: Ottieni tutti i valori in un dizionario.
    - **keys()**: Ottieni tutte le chiavi in un dizionario.
    - **items()**: Ottieni tutte le coppie chiave-valore in un dizionario.
    - **get()**: Ottieni il valore di una chiave specifica in un dizionario.
    - **update()**: Aggiorna il valore di una chiave specifica in un dizionario.
    - **pop()**: Rimuovi un elemento da un dizionario.
    - **clear()**: Rimuovi tutti gli elementi da un dizionario.

## Operatori
- **aritmetici**:
    - **addizione (+)**: Aggiungi due numeri.
    - **sottrazione (-)**: Sottrai un numero da un altro.
    - **moltiplicazione (*)**: Moltiplica due numeri.
    - **divisione (/)**: Divide un numero per un altro.
    - **modulo (%)**: Ottieni il resto di una divisione.
    - **esponente (**)**: Eleva un numero alla potenza di un altro.
- **di assegnazione**:
    - **assegnazione semplice (=)**: Assegna un valore a una variabile.
    - **assegnazione con operatore (+=, -=, *=, /=)**: Esegui un'operazione e assegna il risultato a una variabile.
- **di confronto**:
    - **uguale a (==)**: Controlla se due valori sono uguali.
    - **diverso da (!=)**: Controlla se due valori non sono uguali.
    - **minore di (<)**: Controlla se un valore è minore di un altro.
    - **maggiore di (>)**: Controlla se un valore è maggiore di un altro.
    - **minore o uguale a (<=)**: Controlla se un valore è minore o uguale a un altro.
    - **maggiore o uguale a (>=)**: Controlla se un valore è maggiore o uguale a un altro.
- **logici (and, or, not)**: Operatori logici.

## if...else
- **if**: Esegui un blocco di codice se una condizione è vera.
- **else**: Esegui un blocco di codice se la condizione nell'istruzione if è falsa.
- **elif**: Esegui un blocco di codice se le condizioni precedenti non erano vere.

## Cicli
- **for**: Esegui un blocco di codice per ogni elemento in una sequenza.
    - **for .. in []**: Scorri ogni elemento in una lista.
    - **for .. in {}**: Scorri ogni coppia chiave-valore in un dizionario.
    - **for .. in range()**: Scorri una sequenza di numeri.
- **while**: Esegui un blocco di codice mentre una condizione è vera.
    - **while con condizione**: Esegui un blocco di codice mentre una condizione è vera.
    - **break**: Esci prematuramente dal ciclo.
    - **continue**: Salta l'iterazione corrente e continua con la successiva.

## Funzioni
- **def**: Definisce una nuova funzione.
    - **Nome della funzione**: Identifica univocamente la funzione.
    - **Parametri**: Specifica gli input per la funzione.
    - **Corpo della funzione**: Il codice che viene eseguito quando la funzione viene chiamata.
    - **Return**: Restituisce un valore dalla funzione. Se non specificato, la funzione restituirà `None`.
    - **Docstring**: Fornisce una descrizione della funzione.

## Importazione di moduli
- **import**: Importa un modulo intero.
- **from ... import ...**: Importa specifiche funzioni o variabili da un modulo.
- **import ... as ...**: Importa un modulo con un alias.
- **from ... import ... as ...**: Importa specifiche funzioni o variabili da un modulo con un alias.

# File
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