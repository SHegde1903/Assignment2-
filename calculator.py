print("*"*5+" Simple Calculator "+"*"*5)
print("Enter 2 numbers for calculation : \n")
Number_1=int(input("Enter Number 1: "))
Number_2=int(input("Enter number 2: "))
print("Select Your choice of operation to be performe: ")
print(" \n 1. Addition \n 2. Subtraction \n 3. Multiplication \n 4. Division \n 5. Modulas \n 6. Exponentiation ")
Choice=int(input("Enter your choice number ( between 1 and 6):  "))

if Choice==1:
    print("Selected operation is Addition: ")
    print(" result is:  ",  Number_1 + Number_2)
elif Choice==2:
    print("Selected operation is Subtraction: ")
    print(" result is:  ",  Number_1 - Number_2)
elif Choice==3:
    print("Selected operation is Multiplication: ")
    print(" result is:  ",  Number_1 * Number_2)
elif Choice==4:
    if Number_2!=0:
        print("Selected operation is Division: ")
        print(" result is:  ",  Number_1 / Number_2)
    else:
        print("NUmber not Divisible by Zero !")
elif Choice==5:
    print("Selected operation is Modulus: ")
    print(" result is:  ",  Number_1 % Number_2)
elif Choice==6:
    print("Selected operation is Exponention: ")
    print(" result is:  ",  Number_1 ** Number_2)
else:
    print("Invalid Choice ! . Please select between 1 and 6 only. \n")

print("*"*5 + "THANK YOU "+ "*"*5)
        