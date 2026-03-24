print("="*10 +" ATM Simulator "+"="*10)
Initial_balance=10000
Deposit_amount=0
Witdraw_amount=0
print("Welcome to ATM SIMULATOR")
while True:
    print("Select options below ")
    print("1.Check Balance \n 2. Deposit amount \n 3. Withdraw amount \n 4. Exit ")
    Choice=int(input("Enter your Choice (Select between 1 and 4): "))

    if Choice==1:
        print("Your account Balance is : Rs. ",Initial_balance)

    elif Choice==2:
        Deposit_amount=int(input("Enter amount to be deposit : Rs."))
        Initial_balance=Initial_balance+Deposit_amount
        print("Deposit succesfull...!")
        print("Total amount after deposit of Rs.",Deposit_amount,"is Rs.",Initial_balance)
    elif Choice==3:
        Witdraw_amount=int(input("Enter Aount to withdraw: Rs."))
        if Initial_balance-Witdraw_amount<500:
            print("minimum balance Rs. 500 must remain. ")
        else:
            Initial_balance=Initial_balance-Witdraw_amount
            print("Withdraw Successfull ...!")
            print("Balance after withdraw of Rs.",Witdraw_amount,"is Rs.",Initial_balance)
    elif Choice==4:
        print("Exiting........ \n Thank you *-* ")
        break
    else:
        print("Invald choice ! please enter a valid option between 1 and 4. ")

