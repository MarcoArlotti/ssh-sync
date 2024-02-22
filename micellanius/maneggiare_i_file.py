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

f = open("exercice1.txt","w")
f.write("Hello, World!\nWelcome to file handling in python.")
f.close()
f = open("exercice1.txt","r")
print(f.read())
f.close
f = open("exercice1.txt","a")
f.write("\nthis line was appended.")
f.close()