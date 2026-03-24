print("="*10 +"Ticket Pricing System "+"="*10)
#user input
Age=int(input("Enter Your Age: "))
Day_of_week=input("Enter Day of week(name of the day SUN,MON,TUE,WED,THUR,FRI,SAT): ")
Number_of_tickets=int(input("Enter number of tickets: "))
Ticket_price=0
Child_ticket=150
Adult_ticket=300
Senior_ticket=200
Ticket_type=""
Base_price=0

if Age>=3 and Age<=12:
    Ticket_type=" Child Ticket "
    Base_price=Child_ticket
elif Age>=13 and Age<=59:
    Ticket_type=" Adult Ticket "
    Base_price=Adult_ticket
elif Age>=60:
    Ticket_type=" Senior Ticket "
    Base_price=Senior_ticket
else:
    print("Please enter a valid age ")



#display Ticket Prices
print("="*10 +" Ticket Prices "+"="*10)
print(" You have booked a ",Ticket_type,"and its Base Price is : Rs.",Base_price)
if Day_of_week in["MON","TUE" ,"WED" ,"THURS"]:
    Discount_amount=Base_price*20/100
    Total_amount=Base_price-Discount_amount
    print("Discont 20 percent on base price Rs. ",Base_price, "is Rs. ",Discount_amount)
    print("Amount after Discount is : Rs.",Total_amount)
else:
    print("Total amount to be pay is:  Rs.",Base_price)

Total_amount = Total_amount * Number_of_tickets

print("Total amount to be paid is: Rs.",Total_amount)
