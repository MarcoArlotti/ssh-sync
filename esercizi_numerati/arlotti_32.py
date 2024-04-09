
lista1 = [45,75,25,68,98,12,21,84,54,62]
lista2 = [42,78,23,74,95,16,27,88,51,66]
lista3 = [
    {"name":"Giovanni",
     "surname":"Di Santo",
     "age":42},
     {"name":"Giuseppe",
     "surname":"Mancini",
     "age":75},
     {"name":"Laura",
     "surname":"Accardi",
     "age":25},
     {"name":"Lalla",
     "surname":"Sallusti",
     "age":68},
     {"name":"Salvo",
     "surname":"Olivieri",
     "age":12},
    ]

"""
Date le seguenti liste:
1) ordinare la prima in ordine crescente
2) ordinare la seconda in ordine decrescente
3) ordinare la terza per age decrescente
4) ordinare la terza in base alla lunghezza del cognome
"""
lista1.sort()
print(lista1)

lista2.sort(reverse=True)
print(lista2)

lunghezza = {}

def myFunc(e):
  return e['age']

def riordina(lista3):
    lista3.sort(key=myFunc)

    return lista3
lista3_ordinata = riordina(lista3)
print(lista3_ordinata)





for persone in lista3:
    cognome = persone["surname"]
    num_lettere = len(cognome)
    
    persone["lunghezza_cognome"] = num_lettere
    lunghezza["cognome"] = cognome
    lunghezza["lunghezza_cognome"] = num_lettere
print(lista3)

def myFunc(e):
  return e['lunghezza_cognome']

def riordina(lista3):
    lista3.sort(key=myFunc)

    return lista3
lista3_ordinata = riordina(lista3)
print(lista3_ordinata)