#lancia una moneta
#from termcolor import colored
import random

flip = ["you go first","you go as second"]
while True:
    print(random.choices(flip,weights=[0.1,99]))
#print("-"*50)
#print(f"è uscito {print(random.choices(flip))}")
#print("-"*50)