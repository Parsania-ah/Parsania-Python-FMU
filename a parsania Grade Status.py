na=input("name=?:")
fa=input("Family=?:")

a=float(input("grade1=?:"))
b=float(input("grade2=?:"))
c=float(input("grade=?:"))
avr=(a+b+c)/3
if (avr>=17):
    print(na, fa,"is Grate")
elif (12<=avr<17):
    print(na, fa, "is normal")
else:    
   print(na, fa,"is Failed")