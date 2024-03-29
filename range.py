# range(start,end,step)

r=range(1,11,2) # in this start from 1 go upto 10 (ignore last number ) and difference is 2
# range are immutable means we cant change , start from zero index
print(r[0])
print(r[4])


# if we pass only one value in range means give only end value
# range(end) by default beg=0 and step=1 means difference
print("one pass one value ")
y=range(3)
print(y[0])
# i pass two value
# range(beg.end)  step=1 by default
print("only pass two value")
z=range(5,10)
print(z[4])

print ("using for")
a=range(10,80,8)
for e in a:
    print(e,end=' ')

print("print natural number square")
n=int(input("enter a natural number \n"))
b=range(1,n+1,1)
for e in b:
    print(e**2,end=' ')

print("print even number in reverse")
n=int(input("enter number\n"))
c=range(n*2,1,-2)
for e in c:
    print(e,end=' ')


    # calculate sum of first n multiple of x 
    x=int(input("enter a number"))
    n=int(input("number of multiple"))
    s=0
    for e in range(1,n+1,1):
        s=s+x*e
    print("sum is ",s)    



#range is hashable 