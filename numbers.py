numbers=input("enter integers separated by space:")
numbers=[int(x) for x in numbers.split()]
result=["over" if n>100 else n for n in numbers]
print ("processed list:",result)