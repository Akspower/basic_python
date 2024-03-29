#dict is mutable
d1={}
print(type(d1))
d1={1:"aditya",2:"kumar",3:"sharma",4:100}
print(d1)
print(d1[2])
for e in d1:
    print(e,d1[e])
d2={
 'a':1,
   'k':2,
 "2k":"section"
  }
print("d2 element",d2)

d1[1]="adi"  # edit ,update the value at 1
print(d1)
del d1[1]
print(d1)
print("methods")
print(d1.items())
print(d1.keys())
print(d1.values())

# builtin method apply on keys
print("dictionary")
d2={
    "fast":"in a quick manner",
    "slow":" no response",
    "marks": [1,2,3],
    "anotherdict":{
        "cricket":"outdoor game",
        "ludo":"indoor game"
    }
}
print(d2["fast"])
print(d2["anotherdict"]["cricket"]) #nested dictionary
