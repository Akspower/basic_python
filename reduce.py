from functools import reduce
# import is necessary
# return a single value
# reduce(function,iterables)
def add (a,b):
    return a+b
l1=[1,2,3,4,5]
x=reduce(add,l1)
print(x)