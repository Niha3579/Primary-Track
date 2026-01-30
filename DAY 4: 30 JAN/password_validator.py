import re


def pass_check(password):
    if len(password)<7:
        print("small")
    elif not re.search(r'[A-Z]',password):
        print("need one uppercase")
    elif not re.search(r'\d',password):
        print("need digit")
    elif not re.search(r'[a-z]',password):
        print("need lowercase")
    else:
        print("strong password")
password=input("enter the password  ")
pass_check(password)