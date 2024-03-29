# arithmetic operator
a=2**2
print(a)

b=(-2)**2    #without () it gives -4 as answer
print(b)

c=5/2 #allways gives float value
print(c)

d=5//2    # it gives you floor value like normal division in other language
print(d)
e=18%5  # gives remainder
print(e)

# x=int(input())
# print(5*x)

f="ab"+"cd"  #gives you concandiate
print(f)

g=4*"aks"  #repeat 4 times aks
print(g)


#relational operator

h=5>3
print(h)
h="a">"A"    # follow unicode like ASCII
print(h)




# logical (not,or,and)
i=not True
print(i)
i=5>2 and 5>3
print(i)
i=7>3 or 5<3
print(i)



# bitwise
j=25&37
print(j)

j=44|71
print(j)

j=35>>2
print(j)

j=12<<3
print(j)

# assignment
# x++ error
k=0
k+=1
print(k)

l,m,n=1,2,3 #l=5,y=6 error
print(l,m,n)


# identity operator


a=5
b=5
print (a is b)

a=3.3
b=3.3
print(a is not b)   #is used for match the id



# membership operator (not work on int,float.cmplex)
x="jai shree ram"
print('j' in x)
print('E' in x)
print('shree' not in x)