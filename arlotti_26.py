from math import sqrt

a = float(input("mettere la a\n"))
b = float(input("mettere la b\n"))
c = float(input("mettere la c\n"))

def delta(a: float,b: float,c: float) -> list[float] | None:
    delta = b*b-4*a*c
    if delta < 0:
        return [None,None]
    elif delta == 0:
        risX1 = -b / (2*a)
        risX2 = -b / (2*a)
    else:
        risX1 = (-b + sqrt(delta) / (2 *a))
        risX2 = (-b - sqrt(delta) / (2 *a))
    return [risX1,risX2]

def print_ris(soluz: list[float] | None) -> None:
    
    if lista_soluzioni == None:
        print("il delta è negativo, perciò ERROR")   

    else:
        risX1, risX2  = soluz 
        print(f"x1 corrisponde a {risX1}\nx2 corisponde a {risX2}")    

lista_soluzioni = delta(a,b,c)
print_ris(soluz)