#Dati in input tre numeri, mostrare a video il maggiore
num1 = int(input("numero 1: "))
num2 = int(input("numero 2: "))
num3 = int(input("numero 3: "))
if num1 > num2 and num3:
    print("il primo numero è maggiore")
elif num2 > num1 and num3:
    print("il secono numero è maggiore")
elif num3 > num2 and num1:
    print("il terzo numero è maggiore")