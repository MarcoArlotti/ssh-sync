"""
Exercise 1: Write to a File
Create a new file named exercise1.txt and write the following lines to it:
"Hello, World!"
"Welcome to file handling in Python."
Exercise 2: Read from a File
Read the contents of the file exercise1.txt and print them to the console.
Exercise 3: Append to a File
Append the following line to the file exercise1.txt:
"This line was appended."
Exercise 4: Read Lines from a File
Read the file exercise1.txt line by line and print each line to the console.
Exercise 5: Copy a File
Create a copy of the file exercise1.txt and name it exercise1_copy.txt.
"""
import os
f = open("exercise1.txt","w")
f.write("Hello, World!\nWelcome to file handling in python.\n") #creazione del file python
f.close()

f = open("exercise1.txt","r") #print del file intero
print(f.read())
f.close()

f = open("exercise1.txt","a")
f.write("this line was appended.\n") #aggiungi una riga
f.close()

f = open("exercise1.txt", "r") #riga per riga
for i in f:
  print(i)
f.close

f = open("exercise1.txt","r")
os.