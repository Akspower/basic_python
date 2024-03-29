# tuple is immutable means we can't change
t1=(1,2,3)
print(type(t1))
t2=(5) #this is int ,so when only element pass apply comma after element then it is tuple
print(type(t2))
t2=(4,)
print(type(t2))
t3=1,2,3  #this is also tuple
print(type(t3))

# in tuple also a indexing and slicing concept
print(t3[-1])

t4=1,2,34,5,7,4,3,23,45,100
print(t4[0:5:1]) #slicing
for e in t4:
    print(e , end=" ")

print("builtin method")
print(len(t4))
print(max(t4))
print(sum(t4))
print(sorted(t4))
print(sorted(t4,reverse=True)) # print in reverse sorted

#concatenation and comparision same as str
print(t4.index(34))  # also use count

