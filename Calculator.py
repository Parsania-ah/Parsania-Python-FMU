
import math
p=math.pi
while True:
    
    op=input("enter op (+ - * / sin cos tan cot sqrt fact ) or exit    ")
    if op=="exit":
        break
    if (op=="sin"):
        x=float(input("Enter_x(deg for angle) x:"))
        print("sin",x,"=",math.sin(x*p/180))
    if (op=="cos"):
        x=float(input("Enter_Angle(deg) x:"))
        print("cos",x,"=",math.cos(x*p/180))
    if (op=="tan"):
        x=float(input("Enter_Angle(deg) x:"))
        print("tan",x,"=",math.tan(x*p/180))
    if (op=="cot"):
        x=float(input("Enter_x x:"))
        print("cot",x,"=",math.cot(x*p/180))
    if (op=="sqrt"):
        x=float(input("Enter_x x:"))
        print("sqrt",x,"=",math.sqrt(x))
    if (op=="fact"):
        x=int(input("Enter_ x:"))
        fact=1
        for j in range(x):
            fact=fact*(j+1)
        print("fact",x,"=",fact)
    if (op=="+" or op=="-" or op=="*" or op=="/"):
        a=float(input("enter a:"))    
        b=float(input("enter b:"))
    if op=="+":
        print(float(a+b))
    if op=="-":
        print(float(a-b))
    if op=="*":
        print(float(a*b))
    if op=="/":
        
        #if b==0:
            #print("ERROR_b should not be zero")
        print(float(a/b))

    
    