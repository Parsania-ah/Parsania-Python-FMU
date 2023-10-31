a=float(input("Edge1=?:"))
b=float(input("Edge2=?:"))
c=float(input("Edge3=?:"))
if (a+b>c):
    if (b+c>a):
        if (a+c>b):
            print("Edges make triangle")        
        else:
             print("Edges is not of triangle")
    else:
             print("Edges is not of triangle")
else:
             print("Edges is not of triangle")