# set is mutable and set is not in sequence,no index concept and no slicing concept
# no duplicate value allow
s1={10,20,30,40,50,10} #discard second 10 because it repeat
print(s1) # print in random order
s2=set([1,2,3])
print(s2)
# buildin method same as list and tuple
# concatenation not possible
# comparision possible

s5={1,2,3,4,5,6,7}
s5.add(8)
print(s5) #add element at random position
# list cant add because it is not hashable
s5.update([9,0]) #one by one value will update in set
print(s5)
# s5.clear() clear complete set
# print(s5)

s5.discard(100) #if there is no element in set do not through error but s5.remove() theough the error

print(s1.union(s5)) # give unique value in both
print(s1.intersection(s5)) #common in both


# frozenset is immutable