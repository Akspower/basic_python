class Person:
    def __init__(self,n,a):
        self.name=n
        self.age=a
    def showname(self):
        print(self.name)
    def showage(self):
        print(self.age)

class student(Person):
    def setrollno(self,r):
        self.rollno=r
    def showrollno(self):
        print(self.rollno)


s1=student("aditya",21)
s2=student("rahul",20)
s1.setrollno(123)
s1.showname()
s1.showage()
s1.showrollno()


s2.setrollno(124)
s2.showname()
s2.showage()
s2.showrollno()


# p1=Person("aks",21)
# p1.showname()
# p1.showage()

