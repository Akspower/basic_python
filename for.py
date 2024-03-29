

# cheak how many times any letter repeat in string  
s=input("enter a string \n")
count=0
for e in s:
    if e=='a':
        count+=1
print(count)      



# stop print if r appeaered
x=input("enter a string")
for i in x:
  if i=='r':
   break
  print(i)   
else:
      print("\n All chracter printed , r not found")  # this else run when only break is not used if used then else statement not run
