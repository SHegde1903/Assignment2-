print("="*10 +" Sum and Average Calculator "+"="*10)

number=int(input("How many number you want to include in the operation : "))

total=0
first=int(input("Enter element 1: "))
total=total+first
minimum=first
maximum=first

for i in range(2,number+1):
    element=int(input(f"Enter  element {i+1}:  "))

    total=total+element



    if element>maximum:
        maximum=element
    
    if element<minimum:
        minimum=element

average=total/number


print("="*10 +"  Results  "+"="*10)
print(" Sum:", total)
print(" Average:", average)
print(" Maximum:", maximum)
print(" Minimum:", minimum)






