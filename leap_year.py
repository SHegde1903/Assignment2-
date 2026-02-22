print("="*10 +"Leap year checker "+"="*10)

year=int(input("enter Year: "))
if(year%4==0 and year %100!=0) or (year%400==0):
    print(f"{year} is leap year")
    print("the entered year is divisible by 400 and 4 but not by 100 ")
else:
    print(f"{year} is not a leap year")
    print("the entered year is divisible by 100, but not by 400 and 4")