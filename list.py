n = [-5,0,5,-19,19]
p_l = [x for x in n if x>0]
print("positive number:",p_l)

n = 5
square = [x**2 for x in range(1,n+1)]
print("square",square)

word="programming"
v = [ch for ch in word if ch in 'aeiou']
print("vowels:",v)


words="abc"
o = [ord(ch) for ch in words ]
print("vowels:",o)


