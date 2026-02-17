#FEBRUARY 3TH, 2026


# package -all information of employers in object
# data id salary designatio exp
# main file
# Alice:
# name

import calcfunc

a=int(input("Enter number a:"))
op=str(input("Enter Operator:"))
b=int(input("Enter number b:"))

if(op== '+'):
    print(calcfunc.add(a,b))
elif(op=='-'):
    print(calcfunc.sub(a,b))
elif(op=='*'):
    print(calcfunc.mul(a,b))
elif(op=='/'):
    print(calcfunc.div(a,b))
elif(op=='%'):
    print(calcfunc.mod(a,b))
elif(op=='^'):
    print(calcfunc.pow(a,b))