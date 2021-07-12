class Students(object):
    def __init__(self,name,age,grade):
        self.name=name
        self.age=age
        self.grade=grade
    
    def setGrade (self,grade):
        self.grade=grade
    
    def getGrade (self):
        return self.grade
    

vidhi=Students("vidhi",13,"9th")
vidhi.setGrade("10")
print(vidhi.getGrade())
