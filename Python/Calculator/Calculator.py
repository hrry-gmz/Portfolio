# Calculator | October 31, 2025

def Calculator(): # Function - Input First, Operator, Second, Round
    FirstNumber = float(input("What's your first number? ")) # Input - First Number
    print(" 1 - Addition \n 2 - Subrataction \n 3 - Multiplication \n 4 - Division \n 5 - Exponentiation ") # Print - Operator
    Operator = str(input("What's your operation? ")) # Input - Operator
    SecondNumber = float(input("What's your second number? ")) # Input - Second Number
    Round = int(input("What's the number of decimal places to round to? ")) # Input - Round
    
    Calculate(FirstNumber, Operator, SecondNumber, Round)
    
def Calculate(x, y, z, a): # Function - Output Result
    match y:
        case "1":
            print(format(x, "g"), "+", format(z, "g"), "=", format(round(x + z, a), "g"))
        case "2":
            print(format(x, "g"), "-", format(z, "g"), "=", format(round(x - z, a), "g"))
        case "3":
            print(format(x, "g"), "*", format(z, "g"), "=", format(round(x * z, a), "g"))
        case "4":
            print(format(x, "g"), "/", format(z, "g"), "=", format(round(x / z, a), "g"))
        case "5":
            print(format(x, "g"), "^", format(z, "g"), "=", format(round(x ** z, a), "g"))

Calculator()