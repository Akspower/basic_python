l1=[2,3.4,'aditya',True]   
#list is same as array in other language but in this contain all type of data type also change the value of any element
print(type(l1))
print(l1)   # access full list
print(l1[2]) #access through index
print(l1[-1])  # using -1 access last element and also able to print -2 means second last element

print("access through for loop")
l2=[2,3,4,5,6]
for a in l2:
    print(a ,end=' ')

l3=[1,2,3,4,5,6]    
del l3[1]  # delete second index
print(l3)
l3[0]=0 #edit second index element
print(l3)

# append use to add any element in last l3.append(value)
# insert use to add at any position , in this give two values first is index second is value like this l3.insert(index,value)

l3.append(7)
print(l3)
l3.insert(1,0.1)
print(l3)
