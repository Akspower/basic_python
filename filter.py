
# filter(function,iterables)
def f(x):
    if x%2==0:
        return x
t=(1,2,3,4,13,17,10)
y=filter(f,t)
for e in y:
    print(e,end=' ')