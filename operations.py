# Taking input from user
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

# Arithmetic operations
print("Addition =", a + b)
print("Subtraction =", a - b)
print("Multiplication =", a * b)

# Division (avoid division by zero)
if b != 0:
    print("Division =", a / b)
    print("Modulus =", a % b)
else:
    print("Division and Modulus not possible (division by zero)")
