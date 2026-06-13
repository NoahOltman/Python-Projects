# Clear function
import os
import sympy as sp
os.system('cls' if os.name == 'nt' else 'clear')


def numerical_calculator(x, y, op):
    op = op.lower()
    if op in ["+", "add", "addition", "plus"]:
        return x + y
    elif op in ["-", "subtract", "subtraction", "minus"]:
        return x - y
    elif op in ["*", "multiply", "multiplication"]:
        return x * y
    elif op in ["/", "divide", "division"]:
        if y == 0:
            return "Division by zero error"
        else:
            return x / y
    elif op in ["**", "^", "exponent", "exponentiation"]:
        return x ** y
    elif op in ["rt", "root"]:
        return x ** (1/y)
    else:
        return "That is not a valid operation."
    
def Value_Eror_Correction(variable):
    while True:
        try:
            return float(variable)
        except ValueError:
            print("That is not a valid number.")
            variable = input("Input valid number: ")

def symbolic_calculator():
    x, y = sp.symbols("x y")
    eq = input("Input equation: ")
    solutions = sp.solve(eq, x)
    print(solutions)
symbolic_calculator()

# Calculator loop
while False:
    x = input("Input x: ")
    x = Value_Eror_Correction(x)

    y = input("Input y: ")
    y = Value_Eror_Correction(y)

    op = (input("Input Operation: "))

    result = numerical_calculator(x, y, op)
    print(result)

    again = input("Do you want to continue?: ")
    if again.lower() != "yes":
        break







        
