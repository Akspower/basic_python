y=20 #global
def f1():
    x=10 #local
    print(x)
f1()
# print(x) through error because x is local
print(y)

# local varible priority is more than global