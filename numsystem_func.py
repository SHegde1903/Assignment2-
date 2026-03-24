print("="*10 +" Number System Functions   "+"="*10)

#1. Factorial function
def Fctorial(num):
    if num<0:
        return "no factorial for negertive numbers"
    fact=1
    for i in range(1,num+1):
        fact=fact*i
    return fact

#2. primechecker
def PrimeCheck(num):
    if num<=1:
            print(num," is not a prime number ")
    elif num==2:
            print("2 is a prime number ")
    else:
            count=0

            for i in range(1,num+1):
                if num%i==0:
                    count=count+1
            
            if count==2:
                print(num, " is a prime number ")
            else:
                print(num," is not prime number ")

#3. fibonacci function
def Fibonacci(num):
     if num<=0:
          return "invalid "
     elif num==1:
          return 0
     elif num==2:
          return 1
     else:
          return Fibonacci(num-1)+Fibonacci(num-2)
     
#4.Sum of digits
def DigitSum(num):
     sum=0
     n=num
     while n>0:
        rem=n%10
        sum=sum+rem
        n=n//10
     return sum

#5. reverse number
def NumberReverse(num):
    reversed_num=0
    n=num
    while n>0:
        rem=n%10
        reversed_num=reversed_num*10+rem
        n=n//10
    return reversed_num

#6.Armstrong number
def Armstrong(num):
    original_number=num
    sum=0
    digits=len(str(num))

    while num>0:
        rem=num%10
        sum=sum+rem**digits
        num=num//10

    return sum==original_number

#7. GCD  function
def GCD(num1,num2):
    while(num2!=0):
        num1,num2=num2,num1%num2
    return num1

#8. LCM Function
def LCM(num1,num2):
    greater=max(num1,num2)
    while True:
        if greater % num1==0 and greater %num2==0:
             return greater
        greater=greater+1


#9.is_perfect_number(n) - sum of divisors equals n (e.g., 6 = 1+2+3)

def IsPerfectNumber(num):
     if num<1:
          return False
     sum=0
     for i in range(1,num+1):
          if num%i==0:
               sum=sum+i

     return sum==num
 
#10 main function MathFunction()
def MathFunction():
     while True:
        print("select Function ")
        print("1. Factorial")
        print("2. Check Prime")
        print("3. Fibonacci")
        print("4. Sum of Digits")
        print("5. Reverse Number")
        print("6. Armstrong Number")
        print("7. GCD")
        print("8. LCM")
        print("9. Perfect Number")
        print("10. Exit")

        choice=int(input("Enter your choice (bewtween 1 and 10): "))

        if choice==1:
            num=int(input("enter number: "))
            print("Factorial result: ",Fctorial(num))
        elif choice==2:
            num = int(input("Enter number: "))
            PrimeCheck(num)
        elif choice==3:
            num = int(input("Enter number: "))
            print("Fibonacci numbers:", Fibonacci(num))
        elif choice==4:
            num = int(input("Enter number: "))
            print("Sum of digits:", DigitSum(num))
        elif choice==5:
            num = int(input("Enter number: "))
            print("Reversed number:", NumberReverse(num))
        elif choice==6:
            num = int(input("Enter number: "))
            print(" Armstrong Result:", Armstrong(num))
        elif choice==7:
            num1=int(input("Enter number: "))
            num2=int(input("Enter number: "))
            print("GCD Result:", GCD(num1,num2))
        elif choice==8:
            num1=int(input("Enter number: "))
            num2=int(input("Enter number: "))
            print("LCM Result:", LCM(num1,num2))
        elif choice==9:
            num = int(input("Enter number: "))
            print("Perfect Number Result:",IsPerfectNumber(num))
        elif choice==10:
            print("Exiting.....")
            break
        else:
             print("Invalid choice!, please enter valid choice between 1 and 10")
    

# calling main function
MathFunction()
             



             
             
     