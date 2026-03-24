print("="*10 +" Text Analysis Functions   "+"="*10)



#1. count words
def CountWords(text_input):
    words=text_input.split()
    return len(words)

#2. Count vowels
def CountVowels(text_input):
    vowels="AEIOUaeiou"
    count=0
    for char in text_input:
        if char in vowels:
            count=count+1
        
    return count

#3. count consonents
def CountConsonents(text_input):
    vowels="AEIOUaeiou"
    count=0
    for char in text_input:
        if char.isalpha() and char not in vowels:
            count=count+1
    return count

#4. reverse text
def ReverseText(text_input):
    return text_input[::-1]

#5. check palidrome
def Palindrome(text_input):
    text=text_input.lower()
    reverse_text=text[::-1]
    print("     original text: ",text)
    print("     reversed text: ",reverse_text)
    if text==reverse_text:
        print("     text is palindrome")
    else:
        print("     text is not palidrome")


    
#6.remove vowels
def RemoveVowels(text_input):
    vowels="AEIOUaeiou"
    result=""
    for char in text_input:
        if char not in vowels:
            result=result+char
    return result

#7.word frequency
def WordFrequency(text_input):
    words=text_input.lower().split()
    frequency={}
    for word in words:
        frequency[word]=frequency.get(word,0)+1
    return frequency

#8. longest word
def LongestWord(text_input):
    words=text_input.split()
    longest_word=""
    for word in words:
        if len(word)>len(longest_word):
            longest_word=word
    return longest_word


# main function Anlyse text 
def AnalyseText(text_input):
    print("="*20 +" Text Analysis Result   "+"="*20)
    print("     Words count: ",CountWords(text_input))
    print("     Vowels count: ",CountVowels(text_input))
    print("     Consonents counts: ",CountConsonents(text_input))
    print("     Reversed text: ",ReverseText(text_input))
    print("     Palindrome check: ",Palindrome(text_input))
    print("     Vowels Removed: ",RemoveVowels(text_input))

    longest=LongestWord(text_input)
    len_longest=len(longest)
    print(" longest word: ",longest, "with ",len_longest,"letters")

    word_frequency=WordFrequency(text_input)
    print("Word Frequency: ",end=" ")
    for word, count in word_frequency.items():
        print(f" {word}: {count} ",end=" ")
    print()

# main function calling
text_input=input("Enter Text: ")
AnalyseText(text_input)
   
