print("="*10 +"Ticket Pricing System "+"="*10)
#user input
Ticket_price=0
Child_ticket=150
Adult_ticket=300
Senior_ticket=200
Ticket_type=""
Base_price=0
Total_amount=0
Day_of_week=input("Enter Day of week(name of the day SUN,MON,TUE,WED,THUR,FRI,SAT): ")
Number_of_tickets=int(input("Enter number of tickets: "))
for i in range(Number_of_tickets):
    Age=int(input(f"Enter Age of person{i+1} :"))

    if Age>=3 and Age<=12:
        
        Ticket_type=" Child Ticket "
        Base_price=Child_ticket
        print(f"Person {i+1}: Child Ticket - Rs.{Base_price}")
    elif Age>=13 and Age<=59:
        
        Ticket_type=" Adult Ticket "
        Base_price=Adult_ticket
        print(f"Person {i+1}: Adult Ticket - Rs.{Base_price}")
    elif Age>=60:
        
        Ticket_type=" Senior Ticket "
        Base_price=Senior_ticket
        print(f"Person {i+1}: Senior Ticket - Rs.{Base_price}")
    else:
        print("Please enter a valid age ")

    Ticket_price=Ticket_price+Base_price

#display Ticket Prices
print("="*10 +" Ticket Prices "+"="*10)

if Day_of_week in["MON","TUE" ,"WED" ,"THURS"]:
    Discount_amount=Ticket_price*20/100
    Total_amount=Ticket_price-Discount_amount
    print("Total amount befor discount :Rs. ",Ticket_price)
    print("Discont 20 percent on total amount Rs. ",Ticket_price, "is Rs. ",Discount_amount)
    print("Amount after Discount is : Rs.",Total_amount)
else:
    print("Total amount to be pay is:  Rs.",Ticket_price)


