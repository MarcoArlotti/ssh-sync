f = open("eserizio1.txt","w")
f.write("Hello, World!\nWelcome to file handling in python.")
f.close()
f = open("esercizio1.txt","r")
print(f.read())
f.close
f = open("esercizio1.txt","a")
f.#boh("\nthis line was appended")