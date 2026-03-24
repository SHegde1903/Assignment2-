print("="*20 +"Grade Calculator "+"="*20)
Student_name=input("Enter name of student: ")
Total_marks=0
Pass=True
Grade=""
Result=""
print("Enter marks of Student in 5 subjects (out of 100 each) : ")
for i in range(5):
    marks=int(input(f"Enter marks of subject{i+1}: "))
    #if any subject scores below 40 marks
    if marks<40:
        Pass=False 
        
    Total_marks=Total_marks+marks

Percentage=(Total_marks/500)*100
#grade calculation
if not Pass:
    Grade="F"
    Result="Fail ( scored less than 40 in one or more subject )"
else:
    if Percentage>=90 and Percentage<=100:
        Grade="A+ "
        Result="Outstanding"
    elif Percentage>=80 and Percentage<=89:
        Grade="A"
        Result="Excellent"
    elif Percentage>=70 and Percentage<=79:
        Grade="B"
        Result="Good"
    elif Percentage>=60 and Percentage<=69:
        Grade="C"
        Result="Average"
    elif Percentage>=50 and Percentage<=59:
        Grade="D "
        Result="Pass"
    elif Percentage<50:
        Grade="F "
        Result="Fail"
    else:
        print("Invalid percentage !")





#grade display

print("="*20 +"Grade Scale pf Student "+"="*20)
print("\n")
print("     Student name:   ",Student_name)
print("     Total marks obtained (out of 500):   ",Total_marks)
print("     Percentage Scored:   ",Percentage)
print("     Grade:   ",Grade)
print("     result of the student:   ",Result)



