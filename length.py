a=[1,2,3,4]
b=[4,5,6,7]
c=len(a)
d=len(b)
print(c)
print(d)
if c==d:
    print("list are in same length")
else:
    print("not same length")
    s1=sum(a)
    s2=sum(b)
    print(s1,s2)
    if s1==s2:
        print("both sums are equal")
    else:
        print("not same sum")