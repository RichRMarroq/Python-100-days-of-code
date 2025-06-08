from art import logo
import os
def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}

use_result = False
first_num = 0
while True:
    if not use_result:
        print(logo)
        first_num = int(input("What's the first number: "))
    operation = input("'+'\n'-'\n'*'\n'/'\nSelect an operation: ")
    second_num = int(input("What's the next number"))
    result = operations[operation](first_num, second_num)
    print(f"{first_num} {operation} {second_num} = {result}\n")
    use_result = input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation: ").lower() == 'y'
    first_num = result if use_result else 0

