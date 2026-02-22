print("="*10 +" Calculator function   "+"="*10)

#1.addition function
def add(a,b):
    return a+b

#2. Subtraction function
def subtract(a,b):
    return a-b

#3. multiplication function
def multiply(a,b):
    return a*b

#4. division function
def division(a,b):
    
    if b==0:
        return "Division by zero is not possible !"
    else:
        return a/b
    
#modulas function
def modulas(a,b):
    if b==0:
        return "Division by zero is not possible !"
    else:
        a%b
#6. Power function
def power(a,b):
    return a**b




def calculator():

    while True:
        

        print("select operation function to be perform")
        print(" 1. Add(a,b)")
        print(" 2. Subtract(a,b)")
        print(" 3. Multiply(a,b)")
        print(" 4. Divide(a,b)")
        print(" 5. Modulus(a,b)")
        print(" 6. Power(a,b)")
        print(" 7. Exit")

        choice=int(input("Enter your choice( select between 1 and 7): "))

        if choice==7:
            print("Exiting.....")
            break

        first_number=int(input("Enter First number: "))
        second_number=int(input("Enter Second number: "))

        if choice==1:
            print("Addition result: ",add(first_number,second_number))

        elif choice==2:
            print("Subtraction Result: ",subtract(first_number,second_number))

        elif choice==3:
            print("Multiplication Result: ",multiply(first_number,second_number))

        elif choice==4:
            print("Division result: ",division(first_number,second_number))

        elif choice==5:
            print("Modulas result: ",modulas(first_number,second_number))

        elif choice==6:
            print("Exponentiation Result: ",power(first_number,second_number))

        else:
            print("Invalid choice !, please enter valid choice between 1 and 7")


# call main function calculator()
calculator()


    
