#higher order function takes function as a parameter and return a function
#map(function,iterables)
def square(a):
    return a*a

x=map(square,[1,2,3,4,5])
for e in x:
    print(e,end=' ')




