# ESERCIZIO 6
# 1. Ask the user for two numbers
# 2. Convert the user's input to integers
# 3. Use if-else statements and logical operators to determine whether the numbers are both even, both odd, or one even and one odd
# 4. Print out the result
num1 = int(input("insert fist number"))
num2 = int(input("insert second number"))
if num1 % 2 == 0 and num2 % 2 == 0:
    print("all number are even")