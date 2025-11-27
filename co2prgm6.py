square_area=lambda side:side*side
rectangle_area=lambda length,width:length*width
triangle_area=lambda base,height:0.5*base*height
side=float(input("enter side of square:"))
length=float(input("enter length of rectangle:"))
width=float(input("enter width of reactangle:"))
base=float(input("enter base of triangle:"))
height=float(input("enter height of triangle:"))
print("area of square:",square_area(side))
print("area of recctangle:",rectangle_area(length,width))
print("area of triangle:",triangle_area(base,height))