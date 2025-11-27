start=int(input("enter the starting number of the range:"))
end=int(input("enter the ending number of the range:"))
print("four-digit numbers with all even digits and perfect squares:")
for num in range(start,end+1):
    root=int(num**0.5)
    if root*root==num:
        digits=str(num)
        if all(int(d)%2==0 for d in digits):
            print(num)