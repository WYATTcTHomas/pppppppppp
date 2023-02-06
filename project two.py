import math
print("Hello. enter a number and get started!")
print("1 Addition")
print("2 Subtraction")
print("3 Multiplacation")
print("4 Division")

choice = input ("Enter your choice : ")

number1 = float(input("Enter number 1 : "))
number2 = float(input("Enter number 2 : "))

if choice == "1":
    print(number1, "+", number2, "=", (number1+number2))
if choice == "2":
    print(number1, "-", number2, "=", (number1-number2))
if choice == "3":
    print(number1, "*", number2, "=", (number1*number2))
if choice == "4":
    print(number1, "/", number2, "=", (number1/number2))