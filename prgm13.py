colors=input("enter coma-seperated color names:")
color_list=colors.split(",")
color_list=[color.strip()for color in color_list]
print("first color:",color_list[0])
print("last color:",color_list[-1])