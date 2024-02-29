"""
creare un programma simulativo di sette e mezzo

usando

#1) def crea_mazzo(semi:list,valori:list)->list[dict]:

#1.2) def mischia():

#2) def estrai_carta(mazzo:list[dict])->dict:

3) def turno_del_giocatore(mazzo:list[dict])->float

4) simula_banco(mazzo:list[dict],punteggio_giocatore:float)->float

istruzioni;
si chiede il nome dell'utente
si genera il mazzo
si decide la bet (euro)
si avvia la estrazione del banco
"""
import random
segni = ["bastoni","coppe","denari","spade"]
valori = [1,2,3,4,5,6,7,8,9,10]
mano = []
#ogni carta è un dizionario

def crea_mazzo(segni,valori)->list[dict]:
    mazzo = {}
    #40 carte totali
    carta = {}
    for i in range(len(segni)):
        if i == 0:
            segno = "bastoni"
        elif i == 1:
            segno = "coppe"
        elif i == 2:
            segno = "denari"
        elif i == 3:
            segno = "spade"

        for j in range(len(valori)):
            x = j+1
            mazzo["segno"] = 1
            mazzo["valori"] = valori

    return mazzo
mazzo = crea_mazzo(segni,valori)



def mischia(mazzo):
    for i in range(random.randint(5,10)):
        random.shuffle(mazzo)
    return mazzo





def estrai_carta(mazzo) -> dict:
    #mano = [carta,carta....]
    carta_estratta = mazzo[0]
    mazzo.pop(0)
    return carta_estratta


def turno_del_giocatore(mazzo)->float:
    mano = []

    while True:
        somma_mano = 0
        scelta = input(str("si vuole pescare una carta?\n\nsi\n\nno\n"))

        if scelta == "si":
            carta_estratta = estrai_carta(mazzo)
            mano.append(carta_estratta)
            print(mano)

            for carta in mano:
                print(carta)
                print(type(carta))
                valore_effettivo = carta["valore"]
                if valore_effettivo >= 8:
                    moment = 0.5
                somma_mano = moment + somma_mano

            if somma_mano > 7.5:
                print("hai sforato\ndando i soldi al banco...\n")
                break#TO DO dare i soldi al banco

            else:
                pass

        else:
            print("hai passato")
            break
    
    return mazzo,mano
        

            


#partita()
mazzo = crea_mazzo(segni,valori)
mazzo = mischia(mazzo)
mazzo,mano = turno_del_giocatore(mazzo)


