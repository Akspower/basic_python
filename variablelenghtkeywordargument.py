#  it is different from keyword argument
def f2(**d):  #with two star it is a dict
       for k,v in d.items():
        print(k,'-',v)
f2(a=1,b=2,c=3)
f2(d=4,e=5)



d1={
    'f':6,'g':7
}
f2(**d1)   #we can't direct pass we need to pass with ** then run successfully