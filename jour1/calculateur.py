# -*- coding: utf-8 -*-
"""
Created on Sat Nov 17 20:47:46 2018

@author: sayhan ibrahim
"""


def addition(num1, num2):
    return(num1 + num2)


def soustraction(num1, num2):
    return(num1 - num2)


def multuplication(num1, num2):
    return(num1 * num2)


def division(num1, num2):
    return(num1 / num2)


print("Pour addition enter: '+'")
print("Pour soustraction enter: '-'")
print("Pour multuplication enter: '*'")
print("Pour division enter: '/'")

while True:
    op = input("Enter un choix :(+, -, *, /,): ")
    if op in ("+", "-", "*", "/"):
        while True:
            try:
                num1 = float(input("Entrer le 1er nombre: "))
                num2 = float(input("Entrer le 2eme nombre: "))
                break

            except ValueError:
                print("Invalid input")
                continue

        if op == "+":
            print(num1, "+", num2, "=", addition(num1, num2))
        elif op == "-":
            print(num1, "-", num2, "=", soustraction(num1, num2))
        elif op == "*":
            print(num1, "*", num2, "=", multuplication(num1, num2))
        elif op == "/":
            print(num1, "/", num2, "=", division(num1, num2))
        break

    else:
        print("invalid input")
