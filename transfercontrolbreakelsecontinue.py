
# break
i=1
while i<=3:
   a=int(input("enter even number"))
   if a%2==0:
       break
   i+=1    
if i==4:
    print("you lost the game")
else:
    print("yow won")



    # continnue
    # take 10 odd number as input and skip the even number
i=1
while i<=10:
    x=int(input("enter a odd number"))
    if x%2==0:
     continue
    print(i,"x=",x)
    i+=1

# pass keyword is used to create empty block
if i<5:
 pass    #use to refer next no any block to run

print("hello")