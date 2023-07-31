def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

def get_math_operation():
    while True:
        print("Choose a math operation:")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        choice = input("Enter the corresponding number (1/2/3/4): ")
        if choice in ["1", "2", "3", "4"]:
            return int(choice)
        print("Invalid choice. Please try again.")
