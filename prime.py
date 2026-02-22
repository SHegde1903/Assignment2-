print("="*10 +" Prime Number Program  "+"="*10)

while True:
    print("\n 3Select your option ")
    print("1. Check a number for prime")
    print("2. Generate prime numbers between a range ")
    print("3. Exit ")
    choice=int(input(" Eenter your choice ( select between 1 and 3): "))

    if choice==1:
        #part 1 : check for a single number

        number=int(input(" Enter a number: "))

        if number<=1:
            print(number," is not a prime number ")
        elif number==2:
            print("2 is a prime number ")
        else:
            count=0

            for i in range(1,number+1):
                if number%i==0:
                    count=count+1
            
            if count==2:
                print(number, " is a prime number ")
            else:
                print(number," is not prime number ")


    elif choice==2:

        # generate primr number in given range

        start_number=int(input("Enter starting number : "))
        end_number=int(input("Enter end number: "))

        print("Prime numbers between ",start_number," and ", end_number ," are: ")
        for prime_number in range(start_number,end_number+1):
            
            
            if prime_number>1:
                count=0

                for i in range(1,prime_number+1):
                    if prime_number%i==0:
                        count=count+1
                
                if count==2:
                    print(prime_number,end=" ")
    elif choice==3:
        print("Exiting.....")
        break
    else:
        print("Invalid choice !, please enter options between 1 and 3 only .")
        
        





        