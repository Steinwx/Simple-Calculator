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

def get_numbers():
    while True:
        try:
            num1 = int(input("Enter the first number: "))
            num2 = int(input("Enter the second number: "))
            return num1, num2
        except ValueError:
            print("Invalid input. Please enter valid numbers.")

def calculator_app():
    while True:
        operation = get_math_operation()
        num1, num2 = get_numbers()

        if operation == 1:
            result = add(num1, num2)
        elif operation == 2:
            result = subtract(num1, num2)
        elif operation == 3:
            result = multiply(num1, num2)
        elif operation == 4:
            try:
                result = divide(num1, num2)
            except ValueError as e:
                print(f"Error: {e}")
                continue

        print(f"Result: {result}")

        choice = input("Do you want to try again? (yes/no): ").lower()
        if choice != "yes":
            print("Thank you!")
            break

if __name__ == "__main__":
    calculator_app()
