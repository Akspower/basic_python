# init , automatic call like constructor 
# declare like this __init__(),it is one type of function
class Test:
    def __init__(self) : # one argument required
        print("Namaste")
t1=Test() #auto call when object created
t2=Test()  #due to self t1 is directly passed init   function     



class number :
    def __init__(self,a,b) :
        self.a=a
        self.b=b
        print(a,b)
n1=number(5,6)
n2=number(4,8)