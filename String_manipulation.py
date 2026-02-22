print("Enter a sentence to perform String manipulation")
Sentence=input("Enter Sentece (min 15 char with space included): ")
words=Sentence.split()
#1. Original Sentence.
print("\n Original Sentence entered by you :  ",Sentence)
#2. Total number of Characters with space.
print("Total Characters with space: ",len(Sentence))
#3. Total number of Character Without Space.
print("Total Chracters witout space: ",len(Sentence.replace(" ","")))
#4. Total count of words.
print("Total number of words: ",len(words))
#5.Convert to upper case.
print("Upper case Conversion: ",Sentence.upper())
#6. Convert to lower case.
print("Lower case Conversion : ",Sentence.lower())
#7. First  word of the sentence.
print("First word of the sentence: ",words[0])
#8. last word of the sentence.
print("Lastt word of the sentence: ",words[-1])
#9.Title case conversion
print("Title case conversion : ",Sentence.title())
#10. Reverse the sentence.
print("Reversed Sentence: ",Sentence[::-1])
