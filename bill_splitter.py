print("="*10 +" BILL SPLITTER "+"="*10)
# User Inputs
Total_bill_amount=float(input("Enter total bill amount ( in rupees): "))
Number_of_people=int(input("Enter Number of People: "))
Tax_percentage=float(input("Enter tax (in percentage): "))
Tip_percentage=float(input("Enter Tip (in Percentge): "))
# calculations
Sub_total=Total_bill_amount
Tax_amount=Total_bill_amount*Tax_percentage/100
Bill_after_tax=Sub_total+Tax_amount
Tip_amount=Bill_after_tax*Tip_percentage/100
Total_bill=Bill_after_tax+Tip_amount
Amount_per_person=Total_bill/Number_of_people

print("\n")
print("="*20 +" BILL BREAKDOWN "+"="*20)
print("     "+"Initial Total amount: "+"    "+"Rs.",Total_bill_amount)
print("     "+"Subtotal Amount: "+"    "+"Rs.",Sub_total)
print("     "+"Tax Percentage (",Tax_percentage,"% ): "+"    "+"Rs.",Tax_amount)
print("     "+"Total Amount after Tax : "+"    "+"Rs.",Bill_after_tax)
print("     "+"Tip Percentage (",Tip_percentage,"% ): "+"    "+"Rs.",Tip_amount)
print("     "+"Final Total Amount: "+"    "+"Rs.",Total_bill)
print("     "+"Amount per person Rs. "+"    "+"Rs.",Amount_per_person)



