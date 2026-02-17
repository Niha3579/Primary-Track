def add(a,b):
    return a+b

def sub(a,b):
    return a-b

def mul(a,b):
    return a*b

def div(a,b):
    return a/b

def mod(a,b):
    return a%b

def pow(a,b):
    ans=1
    for i in range(b):
        ans*=a
    return ans