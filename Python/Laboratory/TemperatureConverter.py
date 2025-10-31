# Temperature Converter | October 31, 2025

def Converter(): # Function - Input Conversion, Temperature

    while True:
        print("Temperature Converter")
        print("1 - Celsius to Fahrenheit")
        print("2 - Fahrenheit to Celsius")
        print("3 - Celsius to Kelvin")
        print("4 - Kelvin to Celsius")
        print("5 - Exit")

        Conversion = int(input("Enter your choice: "))
        match Conversion:
            case 1:
                Converting, Converted, Symbol = "Celsius: ", "Fahrenheit: ", "°F\n"
            case 2:
                Converting, Converted, Symbol = "Fahrenheit: ", "Celsius: ", "°C\n"
            case 3:
                Converting, Converted, Symbol = "Celsius: ", "Kelvin: ", "K\n"
            case 4:
                Converting, Converted, Symbol = "Kelvin: ", "Celsius: ", "°C\n"
            case 5:
                exit()

        Temperature = float(input("Enter " + Converting))
        print(Converted, format(round(Convert(Temperature, Conversion), 2), "g"), sep="", end=Symbol) # Round 2 Decimal Places - General Format (No Tracing Zeros)

        Again = str(input("Would you like to convert again? (Y/N): ")).strip().upper()
        if Again != "Y":
            exit()
        print("")

def Convert(Value, Formula): # Function - Output Result
    match Formula:
        case 1:
            return ((9/5)*Value) + 32
        case 2:
            return (Value - 32)*(5/9)
        case 3:
            return Value + 273.15
        case 4:
            return Value - 273.15
        
Converter()