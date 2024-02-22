from math import sqrt

a = float(input("mettere la a\n"))
b = float(input("mettere la b\n"))
c = float(input("mettere la c\n"))

def delta(a: float,b: float,c: float) -> list[float] | None:
    delta = b*b-4*a*c
    if delta < 0:
        risX1 = None
        risX2 = None
    elif delta == 0:
        risX1 = -b / (2*a)
        risX2 = -b / (2*a)
    else:
        risX1 = (-b + sqrt(delta) / (2 *a))
        risX2 = (-b - sqrt(delta) / (2 *a))
    return risX1,risX2

def print_ris(risX1,risX2) -> None:
    
    if  risX1== None and risX2 == None:
        print("il delta è negativo, perciò ERROR")   

    else:
        print(f"x1 corrisponde a {risX1}\nx2 corisponde a {risX2}")    

risX1,risX2 = delta(a,b,c)
print_ris(risX1,risX2)