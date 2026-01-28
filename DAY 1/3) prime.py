def prime(a,b):
    if(b<=1):
        return "false"
    elif (a%b==0):
        return "false"
    
    return prime(a,b-1)

a=5
print(prime(a,a))