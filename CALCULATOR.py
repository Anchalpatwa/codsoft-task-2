# Calculator------------task2-------------------------
def add(m, n):
    return m + n
def subtract(m, n):
    return m - n
def multiply(m, n):
    return m * n
def divide(m, n):
    if n == 0:
        return "Error!! Division by zero."
    return m / n
print("Select any one operation:")
print("1. Addition")
print("2. Subtract")
print("3. Multiply")
print("4. Division")
choice = input("Enter choice (1/2/3/4): ")
num1 = float(input("Enter First Number: "))
num2 = float(input("Enter Second Number: "))

if choice == '1':
    print(num1, "+", num2, "=", add(num1, num2))

elif choice == '2':
    print(num1, "-", num2, "=", subtract(num1, num2))

elif choice == '3':
    print(num1, "*", num2, "=", multiply(num1, num2))

elif choice == '4':
    print(num1, "/", num2, "=", divide(num1, num2))

else:
    print("Invalid input")    