print("="*10 +" Factoril Calculator  "+"="*10)

number=int(input("Enter a number: "))

if number<0:
    print("No factorial for negetive number ")

elif number==0:
    print("0!(Zero factorial)= 1")
else:
    factorial=1
    result=""

    for i in range(number,0,-1):
        factorial=factorial*i
        result=result+str(i)

        if i!=1:
            result=result+"x"
    print(f"{number}!={result}={factorial}")