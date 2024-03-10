# Mappa contenente le funzioni e le procedure in Python

## FUNZIONI

### Definizione di una funzione

```python
def nome_funzione (parametri):
    # corpo della funzione
    ...
    return valore

risultato = nome_funzione (argomenti)
```


- def: Parola chiave usata per iniziare la definizione di una funzione.
- nome_funzione: Il nome che si sceglie per la funzione. Deve essere unico e descrittivo.
- parametri: Variabili che vengono passate alla funzione. Possono essere di qualsiasi tipo e numero.
- valore: Il valore che la funzione restituisce.
- argomenti: I valori che vengono passati alla funzione quando viene chiamata.
- risultato: La variabile a cui viene assegnato il valore restituito dalla funzione.

## PROCEDURE

### Definizione di una procedura

```python
def nome_procedura (parametri):
    # corpo della procedura
    ...

nome_procedura (argomenti)
```


- def: Parola chiave usata per iniziare la definizione di una procedura.
- nome_procedura: Il nome che si sceglie per la procedura. Deve essere unico e descrittivo.
- parametri: Variabili che vengono passate alla procedura. Possono essere di qualsiasi tipo e numero.
- argomenti: I valori che vengono passati alla procedura quando viene chiamata.


## Differenza tra funzioni e procedure

### Funzioni

- Le funzioni in Python restituiscono un valore.
- Questo valore di ritorno viene specificato usando la parola chiave `return`.
- Quando si chiama una funzione, si assegna il suo valore di ritorno a una variabile.

```python
#Esempio di funzione

def somma (a, b):
    return a + b

risultato = somma (1, 2)  #Assegna il valore di ritorno a una variabile
print (risultato)  #Stampa: 3
```

### Procedure

- Una procedura è una funzione che non restituisce un valore.
- Questo tipo di funzioni sono spesso utilizzate per le loro operazioni, come stampare a schermo, scrivere su un file, ecc.

```python
#Esempio di procedura

def stampa_saluto ():
    print ("Ciao!")  #Esegue un'operazione ma non restituisce un valore

stampa_saluto ()  #Stampa: Ciao!
```

# L'istruzione `return` in Python

## Uscita dalla funzione

- L'istruzione `return` permette di uscire da una funzione.
- Quando il programma viene eseguito ed incontra l'istruzione `return`, la funzione si interrompe immediatamente.

```python
#Utilizzo dell’istruzione return per terminare anticipatamente una funzione in Python

def saluta (nome):
    if nome == "":
        return "Il nome non può essere vuoto."  #Esce dalla funzione se il nome è vuoto
    else:
        return f"Ciao, {nome}!"  #Restituisce un saluto se il nome non è vuoto

risultato = saluta ("Mario")
print (risultato)  #Stampa: Ciao, Mario!

risultato = saluta ("")
print (risultato)  #Stampa: Il nome non può essere vuoto.
```

## Restituzione di un valore
- L'istruzione `return` può essere seguita da un valore o da una espressione.
- Questo valore (o il risultato dell'espressione) viene restituito al codice che ha chiamato la funzione.

```python
#Esempio di funzione che restituisce un valore

def raddoppia (n):
    return n * 2  #Restituisce il doppio del valore in input

risultato = raddoppia (5)
print (risultato)  #Stampa: 10
```

## Restituzione di più valori
- In Python, l'istruzione `return` può restituire più valori se questi sono separati da virgole.
- In questo caso, i valori restituiti vengono impacchettati in una tupla.

```python
#Esempio di funzione che restituisce più valori

def somma_e_sottrazione (a, b):
    return a + b, a - b  #Restituisce la somma e la differenza

somma, differenza = somma_e_sottrazione (7, 3)
print (somma)  #Stampa: 10
print (differenza)  #Stampa: 4
```

## Funzioni senza `return`
- Se una funzione non ha un'istruzione `return`, o se l'istruzione `return` non è seguita da un valore, la funzione restituisce `None`.
- Questo è spesso il caso per le procedure, che eseguono un'azione ma non restituiscono un risultato.

```python
#Esempio di funzione senza 'return'
def stampa_saluto ():
    print ("Ciao!")  #Esegue un'operazione ma non restituisce un valore

risultato = stampa_saluto ()  #Stampa: Ciao!
print (risultato)  #Stampa: None
```

# None in Python

## Definizione

- `None` è un valore speciale in Python che rappresenta l'assenza di un valore o un valore nullo.

## Immutabilità

- `None` è immutabile, il che significa che non può essere cambiato una volta assegnato.

## Utilizzo come valore predefinito

- `None` è spesso utilizzato come valore predefinito per gli argomenti di funzione.

```python
#Esempio con il valore None

#Se 'arg' non viene fornito quando la funzione viene chiamata, il suo valore predefinito sarà 'None'

def funzione_esempio (arg= None):
    
    if arg is None:
        print ("Nessun argomento fornito") #Se 'arg' è 'None', la funzione stampa "Nessun argomento fornito"

    else: print (f"Argomento fornito: {arg}") #Se 'arg' non è 'None', la funzione stampa "Argomento fornito: " seguito dal valore di 'arg'
```