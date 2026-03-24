print("="*10 +"Menu based Temperature Calculator "+"="*10)

#user input for temperature in celsius
Temperature=float(input("Enter Temperature in Celsius: "))
while True:
    print("*"*10+"Convertion options"+"*"*10)
    print(" 1. Celsius to Fahrenheit ")
    print(" 2. Fahrenheit to Celsius ")
    print(" 3. Celsius to Kelvin")
    print(" 4. Kelvin to Celsius ")
    print(" 5. Fahrenheit to Kelvin ")
    print(" 6. Kelvin to Fahrenheit ")
    print(" 7. Exit ")
    Choice=int(input("Select Convertion Choice (select between 1 and 7 ): "))

    #convertion calculation
    if Choice==1:
        #Celsius to Fahrenheit
        Fahrenheit=(Temperature*9/5)+32
        print("Conversion Result of Celsius to Fahrenheit : ",Fahrenheit)
    elif Choice==2:
        #Fahrenheit to Celsius 
        Fahrenheit_to_Celsius=(Fahrenheit-32)*5/9 
        print("Conversion Result of Fahrenheit to Celsius : ",Fahrenheit_to_Celsius)
    elif Choice==3:
        #Celsius to Kelvin
        Kelvin=Temperature+237.15
        print("Conversion Result of Celsius to Kelvin : ",Kelvin)
    elif Choice==4:
        #Kelvin to Celsius
        Kelvin_to_Celsius=Kelvin-273.15
        print("Conversion Result of Kelvin to Celsius : ",Kelvin_to_Celsius)
    elif Choice==5:
        #Fahrenheit to Kelvin
        Fahrenheit_to_Kelvin=(Fahrenheit - 32)*5/9 + 273.15
        print("Conversion Result of Fahrenheit to Kelvin : ",Fahrenheit_to_Kelvin)
    elif Choice==6:
        #Kelvin to Fahrenheit
        Kelvin_to_Fahrenheit=(Kelvin-237.15)*9/5+32
        print("Conversion Result of Kelvin to Fahrenheit : ",Kelvin_to_Fahrenheit)
    elif Choice==7:
        print("Exiting ........")
        break
    else:
        print("Invalid choice ! please enter options between 1 and 7 ")





