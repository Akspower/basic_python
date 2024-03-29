#decision.match,iterative all are control statement
x= int(input("enter  number for cheak \n"))
#if x>0:   
#    print("positive number")  #equal space required 
#else:      # also used again if x<=0;
 #print("negative number")   # equal indentation required every statement


 #if elif else


if x>60 and x<=99:
    print("first division")
elif x>45 and x<=60:
    print("second division") 
elif  x<30:
    print("third division")
else:
    print("enter valid number")    


    #single line if else
z=int(input("enter your lucky number"))
print("lucky") if z>20 and z<=50 else print("unlucky")    