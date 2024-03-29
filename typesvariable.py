# local,global


# instance object variables
#  class object variables



print("instance object and class object")
class A:
    x1=5 #class object
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def f1(self):
        self.c=30

    @classmethod
    def f2(cls):
     cls.x2=15
obj1=A(10,20) #instance
print(A.a,obj1.b)
obj1.f1()
print(obj1.c)
A.f2() #class object
A.x3=5
print(A.x2)


# print("class object")
# class B:
#     x1=5
# @classmethod
# def f2(cls):
#     cls.x2=15

