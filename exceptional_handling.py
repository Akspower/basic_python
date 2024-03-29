#unexpected error like define take input in int but give input in string it through error
#  print y before declaration through error

try:
    a=int(input("Enter a number"))
    print("a")
except ValueError as e: # more than 1 except will  be able to defined
# except ZeroDivisionError as e: it handle error when denominator is zero
    print("not a number")

finally:  #run in any situation
    print("Thank You")
#also use else when exception not match
print("Hello")
