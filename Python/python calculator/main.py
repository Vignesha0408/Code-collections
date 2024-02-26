from math import *
print("type + for addition")
print("type - for substraction")
print("type * for multiplication")
print("type / for division")
print("type @ for square")
print("type % for remainder")
print("type ^ for cube")
print("type | for root")
type = str(input())

if type == "+":
    num1 = int(input("enter value of first number \n"))
    num2 = int(input("enter value of 2 number \n"))
    num3 = num1 + num2
    print(f"result {num3}")

if type == "-":
    num1 = int(input("enter value of first number \n"))
    num2 = int(input("enter value of 2 number \n"))
    num3 = num1 - num2
    print(f"result {num3}")


if type == "*":
    num1 = int(input("enter value of first number \n"))
    num2 = int(input("enter value of 2 number \n"))
    num3 = num1 * num2
    print(f"result {num3}")


if type == "/":
    num1 = int(input("enter value of first number \n"))
    num2 = int(input("enter value of 2 number \n"))
    num3 = num1 / num2
    print(f"result {num3}")


if type == "@":
    num1 = int(input("enter value of first number \n"))
    num2 = int(input("enter value of 2 number \n"))
    num3 = float(num1*num1 )   
    num4 = float(num2*num2 )
    print(f"result square of { num1 } is { num3 } & square of { num2 } is { num4 } ")


if type == "%":
    num1 = int(input("enter value of first number \n"))
    num2 = int(input("enter value of 2 number \n"))
    num3 = num1 % num2
    print(f"result  the remainder of {num1} & {num2} is {num3}")



if type == "^":
    num1 = int(input("enter value of first number \n"))
    num2 = int(input("enter value of 2 number \n"))
    num3 = float(num1*num1*num1 )   
    num4 = float(num2*num2*num2 )
    print(f"result cube of { num1 } is { num3 } & cube of { num2 } is { num4 } ")


if type == "|":
    num1 = int(input("enter value of first number \n"))
    num2 = int(input("enter value of 2 number \n"))
    num3 = float(sqrt(num1))   
    num4 = float(sqrt(num2))
    print(f"result root of { num1 } is { num3 } & root of { num2 } is { num4 } ")