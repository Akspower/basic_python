#types of method in class
# 1 instance method
# 2 static method
# 3 class method 
    

print ("instance method ")#(compulsory one argument)
class A:
    def f1(self):
        self.a=5
obj1=A()
A.f1(obj1)
print(obj1.a)



print(" static method") #(no need of argument)
class B:
    @staticmethod
    def f1():
        print("Namaste")
    @staticmethod
    def f2(a,b):
        print(a,b)
obj2=B()
B.f1()
B.f2(5,10)
obj2.f2(20,40)


print ("class method")# (argument required)
class C:
    @classmethod
    def f1(cls):
        cls.x=100

obj3=C()
obj3.f1()
print(C.x)
