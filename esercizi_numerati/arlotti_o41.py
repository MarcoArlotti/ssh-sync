def inserisci_numeri():
    rifai = True
    while rifai == True:
        rifai = False
        numero1 = input("inserisci un numero\n")
        try:
            int(numero1)
        except:
            rifai = True
            print("inserire un numero valido\n")
    rifai = True

    while rifai == True:
        rifai = False
        numero2 = input("inserisci un numero\n")
        try:
            int(numero2)
        except:
            rifai = True
            print("inserire un numero valido\n")

    return numero1,numero2


def scegli_operazione():
    segno = str(input("|+|-|/|*|\n"))
    return segno



def calcola(segno,numero1,numero2):
    if segno == "*":
       ris = numero1 * numero2
    elif segno == "+":
        ris = numero1 + numero2
    elif segno == "-":
        ris = numero1 + numero2
    elif segno == "/":
        ris = numero1 + numero2
    print(ris)

def main():
    numero1,numero2 = inserisci_numeri()
    segno = scegli_operazione()
    calcola(segno,numero1,numero2)

main()