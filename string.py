# str is immutable and hashable , immutable means cant change after create

# "adi" """adi""" 'adi' '''adi'''   all are string

s1="aditya"
print(type(s1))
print(s1[-1])
print(s1[1])

for e in s1:
    print(e ,end=' ' )

    # slicing concept
print(s1[0:4:1] )     #start from zero index go upto 4-1 and taking step of 1

# builtin same as list ,len(),max(),min(),sum(),sorted()

s1="ABC"
s2="DEF"
s3=s1+s2
print(s3)
print(s3*3)  #print 3 times s3
print(s1>s2)  #firstly compare first element



print("object method")
s5="Aditya Kumar Sharma"
print(s5.index("i"))
print(s5.count("a"))
print(s5.startswith("A"))
print(s5.endswith("a"))
print(s5.isdigit())
print(s5.islower())   # return true if all are lower 
print(s5.isupper())
print(s5.upper())   #convert but not change s5
print(s5.replace('A','Z'))