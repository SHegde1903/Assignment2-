print("="*10 +" Number Pattern printing "+"="*10)
while True:
    print("Select pattern Type ")
    print(" 1. Pattern 1: Increasing numbers")
    print(" 2. Pattern 2: Repeated Row numbers")
    print(" 3. Pattern 3: Decreading numbers")
    print(" 4. Pattern 4: Pyramid pattern")
    print(" 5. Exit")

    Choice=int(input("Enter your choice ( between 1 and 5): "))
    
    if Choice==5:
        print("Exiting..... ")
        break


    height=int(input("Enter hight of the patter( number of rows)  : "))

    print("="*10 +" Generated Pattern "+"="*10)
    #pattern 1
    if Choice==1:
        print(" Pattern 1: Increasing numbers")
        for i in range(1,height+1):
            for j in range(1,i+1):
                print(j,end=" ")
            print()
    #Pattern 2
    elif Choice==2:
        print(" Pattern 2: Repeated Row numbers")
        for i in range(1,height+1):
            for j in range(i):
                print(i,end=" ")
            print()
    #pattern 3
    elif Choice==3:
        print(" 3. Pattern 3: Decreading numbers")
        for i in range(height,0,-1):
            for j in range(i,0,-1):
                print(j,end=" ")
            print()
    #Pattern 4
    elif Choice==4:
        for i in range(1,height+1):
            # spaces
            for space in range(height - i):
                print(" ", end="")
            for j in range(1,i+1):
                print(j,end="")
            for j in range(i-1,0,-1):
                print(j,end="")
            print()

    

    else:
        print("Invalid Choice !, please enter choice between 1 and 5")


        