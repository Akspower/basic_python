
def f1(a,b=0):  # so assign b=0 now we call with single argument and code run
    print("a=",a,"b=",b)
    c=a+b
    print(" add is " ,c)
    return c  #return value always back 


s=f1(1,2)
print("return value in s is ",s)
f1(5) #with single argument
