def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y

print("Select operation:")
print("Add")
print("Subtract")
print("Multiply")
print("Divide")

while True:
    choice = input("Enter (Add/Subtract/Multiply/Divide): ")

    if choice in ('Add', 'Subtract', 'Multiply', 'Divide'):
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        if choice == 'Add':
            print(num1, "+", num2, "=", add(num1, num2))

        elif choice == 'Subtract':
            print(num1, "-", num2, "=", subtract(num1, num2))

        elif choice == 'Multiply':
            print(num1, "*", num2, "=", multiply(num1, num2))

        elif choice == 'Divide':
            print(num1, "/", num2, "=", divide(num1, num2))
        
        next_calculation = input("For next calculation type(Yes/No): ")
        if next_calculation == "No":
          break
    else:
        print("Invalid Input")