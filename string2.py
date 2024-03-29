print( "{} How are you ? ".format("Aditya"))
s1="first= {},{},{}"
x="aks"
y=3
z=1.5
print(s1.format(x,y,z))

s1="aditya kumar sharma"
print(s1.split(' '))

s1=input("Enter a integer separated by comma ")
l1=s1.split(',')
mylist=[int(e) for e in l1]
print(mylist)
#split=change str to list of str

#join= change list of str into str
l1=["01","01","2023"]
print("-". join(l1))