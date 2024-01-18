"""
#FOCUS
liste di dizionari: imparare a combinare il precedente argomento (le liste) con i dizionari.
Realizzare un applicativo che permetta, mediante l'uso di dizionari e liste, la gestione del catalogo di un museo.
In particolare, l'applicativo dovrà permettere di:
#1) Creare una nuova stanza (id, denominazione, metratura) 
#2) Aggiungere un opera ad una stanza(titolo, artista, anno)
#3) Consultare le opere presenti in una stanza
#4) Consultare le stanze presenti
#5) Cercare le informazioni su un opera
#6) Cancellare un opera
7) Cancellare una stanza solo se vuota
 
NB 
- Progettare la struttura dati a priori in modo da garantire le funzionalità richieste.
- Fare in modo che il museo sia inizialmente vuoto e popolabile da applicativo.
- Realizzare un menù numerato con le varie funzionalità elencate in precedenza.
- Controllare la presenza della stanza e/o dell'opera prima di aggiungerla.
"""

"""
#opere = [opera1,opera2,opera3,]
contenitore_di_stanze = {}
    stanza{}
        lista_opere = []
"""
museo = []
lista_opere = []

while True:
    scelta = input("\npremere un numero il quale corrisponde al comando per proseguire\n\n1) Creare una nuova stanza (id, denominazione, metratura)\n2) Aggiungere un opera ad una stanza(titolo, artista, anno)\n3) Consultare le opere presenti in una stanza\n4) Consultare le stanze presenti\n5) Cercare le informazioni su un opera\n6) Cancellare un opera\n7) Cancellare una stanza solo se vuota\n")
    match scelta:
        case "1":
            
            denom = str(input("mettere denominazione della stanza   "))
            metratura = float(input("mettere metratura  "))
            id_stanza = int(input("mettere l'id della stanza  "))
            stanza = {
                "id_":id_stanza,
                "denominazione":denom,
                "metratura":metratura,
                "opere":lista_opere,
            }
            museo.append(stanza)    

            titolo_opera = str(input("mettere titolo opera   "))
            nome_artista = str(input("mettere nome artista  "))
            anno_data = int(input("mettere l'anno pubblicazione  "))
            id_opera = int(input("inserire l'id per identificare l'opera in questione  "))
            opera = {
                 "titolo":titolo_opera,
                 "artista":nome_artista,
                 "anno":anno_data,
                 "id_opera":id_opera,
            }
            lista_opere.append(opera)
            
        case "3":
            tracker_stanza = str(input("inserire in che stanza mettere l'opera  "))
            id_inser = str(input("inserire che opera prendere(dal suo id)   "))
            if id_opera in opera == id_inser:
                if traker_stanza == id_stanza:
                    stanza.append(opera) 
                else:
                    print("dato non corrisponde")                       
            else:
                print("opera non trovata")
        case "4":
            cercastanza = str(input("inserire che stanza consultare (dal suo id)    "))
            if id_stanza in stanza == cercastanza:
                print(stanza)
                
            else:
                print("stanza non trovata")
        case "5":
            cerca_opere = ("inserisci titolo dell'opera che si sta cercando ")
            if cerca_opere in titolo_opera:
                print("opera")
        case "6":
            cerca_opere = ("inserisci titolo dell'opera che si sta cercando ")
            if cerca_opere in titolo_opera:
                opera.remove()                      
        case "7":
            break 
