l1=[2,3,4]
(a,b,c)=l1
print(a,b,c)

l2=[c,b,a] # all these possible
print(l2)

print("Built in method")
print(len(l1))
print(min(l1))
print(max(l1))
print(sum(l1)) #not work when differnt type of datatypes
print(sorted(l1))  #only give sorted order not change the l1
print(l1==l2) #compare one to one ,equal index and same value at same index
print(l1>l2)   #compare only first index if equal then compare next

l3=l1+l2
print(l3)
print(l1*5)  #repeat 5 times


# slicing
print(l1[0:2])  #start from zero index go upto n-1
print(l1[::-1]) # start from last

print("list of list")
l5=[[1,2,3],[4,6],[7,8,9]]
print(l5[0])
print(l5[1])
print(l5[0][0])
print(l5[0][2])

l1=[5,6,7,8,9,10]
l1.remove(8) # value required to remove,no nned of index , if two place 8 in list only remove first 8
print(l1)
del l1[1]
print(l1)
l1.pop() # pop last value
print(l1)
l1.clear() # clear all the list but empty list present

l1=[122,5,651,74,98,100]
l1.sort()  #Also change the l1 
print(l1) 
l1=[23,54,12,5,100,5]
print(l1.index(100)) # give index
print(l1.count(5))  # count how many times 5 in list

print("taking input")
print("how many number you want to enter")
n=int(input())
l1=[]
i=0
while i<n:
    l1.append(int(input("Enter a Number ")))
    i+=1
    print(" The list is \n ")
    print(l1)
l3=[1,5,2]


