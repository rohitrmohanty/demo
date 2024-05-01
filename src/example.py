# This function adds two numbers
def addition(x, y):
    return x + y

# This function subtracts two numbers
def subtraction(x, y):
    return x - y

# This function multiplies two numbers
def multiplication(x, y):
    return x * y

# This function divides two numbers
def division(x, y):
    return x / y

# This function the exponentiation operator uses right-sided binding to calculate two numbers
def exponentiation(x, y):
    return x ** y


print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")
print("5.Exponent")


while True:
    # accept input from the user
    selection = int(input("Enter operation to compute(1/2/3/4/5): "))
    print(type(selection))
    # check if the input is one of the options
    if selection in (1, 2, 3, 4, 5):
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        if selection == 1:
            print(num1, "+", num2, "=", addition(num1, num2))

        elif selection == 2:
            print(num1, "-", num2, "=", subtraction(num1, num2))

        elif selection == 3:
            print(num1, "*", num2, "=", multiplication(num1, num2))

        elif selection == 4:
            print(num1, "/", num2, "=", division(num1, num2))

        elif selection == 5:
            print(num1, "**", num2, "=", exponentiation(num1, num2))
        
        # check if user wants another calculation
        # break the while loop if answer is N
        next_calculation = input("Calculate again? (Y/N): ")
        if next_calculation == "N":
          break
    else:
        print("Invalid Input")
