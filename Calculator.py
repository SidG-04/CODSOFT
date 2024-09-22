def divide(x, y):
    if y == 0:
        return "Mathematrical Error (Division by zero)"
    return x / y
print("Simple Calculator")
print("Operations:")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")
while True:
    choice = input("Enter operation number (1/2/3/4): ")
    if choice in ('1', '2', '3', '4'):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        if choice == '1':
            print(f"{num1} + {num2} = ",num1+num2)
        elif choice == '2':
            print(f"{num1} - {num2} = ",num1-num2)
        elif choice == '3':
            print(f"{num1} * {num2} = ",num1*num2)
        elif choice == '4':
            print(f"{num1} / {num2} = {divide(num1, num2)}")
        another = input("Do another calculation? (yes/no): ")
        if another.lower() != 'yes':
            break
    else:
        print("Invalid choice. Please try again.")