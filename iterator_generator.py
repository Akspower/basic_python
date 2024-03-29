#iterator = use to access alement one by one using iter(),use on any iterable
r1=range(1,11,1)
obj=iter(r1)
print(next(obj)) #next use to access always give one element
print(next(obj))
print(next(obj))


print("generator") #one type of function

def f1():
    yield 10  #yield is keyword to generate data 
    yield 20
    yield 30 
g=f1()
print(next(g))
print(next(g))