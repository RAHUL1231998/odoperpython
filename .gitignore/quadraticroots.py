import math
global r1,r2,rpart,ipart
print("Enter the coefficients of x square,x and contant")
a = float(input("a ="))
b = float(input("b ="))
c = float(input("c ="))
d = (b*b)-(4*a*c)
T = math.sqrt(d)
if d==0:
    print("The roots are equal","\n")
    r1 = r2 = (-b)/(2*a)
    print("The root1 = ",r1,"root2 = ",r2,"\n")
elif d>0:
    print("The roots are real and distinct","\n")
    r1 = ((-b)+T)/(2*a)
    r2 = ((-b)-T)/(2*a) 
    print("The root1 = ",r1,"root2 = ",r2,"\n")
elif d<o:
    print("The roots are imaginary","\n")
    rpart = (-b)/(2*a);
    ipart = (math.sqrt(-d))/(2*a)
    print("The root1 = ",rpart,"+",ipart,"root 2 = ",rpart,"-",ipart)
