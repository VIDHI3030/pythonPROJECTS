def swap():
    file1=input("please enter the first file ")
    file2=input("please enter the second file ")
    a=open(file1,'r')
    dataA=a.read()
    b=open(file2,'r')
    dataB=b.read()
    a=open(file1,'w')
    a.write(dataB)
    b=open(file2,'w')
    b.write(dataA)

swap()