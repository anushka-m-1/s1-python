filename=input("enter the filename:")
parts=filename.split(".")
if len(parts)>1:
    print("the file extension is:",parts[-1])
else:
    print("no extension found.")