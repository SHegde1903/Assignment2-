print("="*10 +" Multiplication Table "+"="*10)

number=int(input("Enter number to generate the multiplication table: "))
end_range=int(input("Enter end range: "))

print("="*10 +" Multiplication Table of ",number,"="*10)
for i in range(1,end_range+1):
    print("     " ,number,"x",i,"=",number*i)



print("="*10 +" Multiplication Table (1-10)"+"="*10)
for i in range(1,11):
    for j in range(1,11):
        print(f"{i*j:5}",end=" ")
    print()