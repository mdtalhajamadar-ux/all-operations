# Taking input from user
a = 10
b = 20

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
