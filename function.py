def countWords():
    fname=input("please enter your file name ")
    wordCount=0
    lineCount=0
    file=open (fname,'r')
    for line in file:
        words=line.split()
        wordCount+=len(words)
        lineCount+=1
    print("number of words ",wordCount)
    print("number of lines ",lineCount)
countWords()