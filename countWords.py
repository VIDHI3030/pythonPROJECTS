myscreen=input("enter astring: ")
charCount=0
wordCount=1
for i in myscreen:
    charCount+=1
    if (i== ' '):
        wordCount+=1
    
print(wordCount)
print(charCount)