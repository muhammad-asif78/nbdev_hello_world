# run_calculator.py
from nbdev_hello_world.calculator import calculator_logic

def calculator():
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))
    op = input("Enter operation (+, -, *, /): ")
    print("Result:", calculator_logic(a, b, op))

if __name__ == "__main__":
    calculator()
