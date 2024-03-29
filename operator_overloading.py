#sometimes can't able to add 
class Line:
    def __init__(self,l):
        self.length=l
    def show_length(self):
        print("length=",self.length)
    def __add__(self,other):
        return Line(self.length+other.length)
l1=Line(10)
l2=Line(20)
l3=l1+l2 #without operator overloading concept through error 
# meaning is l3=l1.__add(l2) --> __add__(l1,l2)
l3.show_length()
