cy=int(input("enter the current year:"))
fy=int(input("enter the final year"))
print(f"leap year from{cy}to{fy}are:")
for year in range(cy,fy+1):
    if(year%4==0 and year%100!=0)or(year%400==0):
        print(year)
