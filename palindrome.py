print("="*10 +" Palindrome Checker   "+"="*10)

user_input=input("Enter word or number : ")

original_input=user_input

reversed_input=""

for char in user_input:
    reversed_input=char+reversed_input

print("Original Input is ",original_input)
print("Reverse of the input is :  ",reversed_input)

#palindrome check
if original_input.lower()==reversed_input.lower():
    print(original_input," is a palindrome")
else:
    print(original_input," is not a palindrome")