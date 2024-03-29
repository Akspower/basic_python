#same as access specifer but not too much secure



class Test:
    x=5
    __y=10 #hide data
    def __init__(self):
        self.__a=100
# print(Test.__y) not possible due to name mangling
print(Test._Test__y)
t1=Test()
print(t1.__dict__)