text=input("enter a sentence:")
words=text.split()
w={}
for i in words:
    if i in w:
        w[i]+=1
    else:
        w[i]=1
print(w)
