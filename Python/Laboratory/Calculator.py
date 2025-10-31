# Calculator | October 31, 2025

def Calculator(): # Function - Input Operator, First, Second, Round

    while True:    
        print("Calculator")
        print("1 - Addition")
        print("2 - Subtraction")
        print("3 - Multiplication")
        print("4 - Division")
        print("5 - Exponentiation")
        print("6 - Exit")    

        Operator = int(input("What's your operation? ")) # Input - Operator
        FirstNumber = float(input("What's your first number? ")) # Input - First Number
        SecondNumber = float(input("What's your second number? ")) # Input - Second Number
        Round = int(input("What's the number of decimal places to round to? ")) # Input - Round
        Calculate(Operator, FirstNumber, SecondNumber, Round)
        
        Again = str(input("Would you like to calculate again? (Y/N): ")).strip().upper()
        if Again != "Y":
            exit()
        print("")
    
def Calculate(Operation, First, Second, Decimal): # Function - Output Result
    match Operation:
        case 1:
            print(format(First, "g"), "+", format(Second, "g"), "=", format(round(First + Second, Decimal), "g"))
        case 2:
            print(format(First, "g"), "-", format(Second, "g"), "=", format(round(First - Second, Decimal), "g"))
        case 3:
            print(format(First, "g"), "*", format(Second, "g"), "=", format(round(First * Second, Decimal), "g"))
        case 4:
            print(format(First, "g"), "/", format(Second, "g"), "=", format(round(First / Second, Decimal), "g"))
        case 5:
            print(format(First, "g"), "^", format(Second, "g"), "=", format(round(First ** Second, Decimal), "g"))
        case 6:
            exit()

Calculator()