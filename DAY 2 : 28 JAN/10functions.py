# def greet(name):
#     print(f"Welcome to {name}")
# greet("uber")


# def add(a,b):
#     return a+b
# a,b=5,7
# result=add(a,b)
# print(result)


# def add_all(*args):
#     sum=0
#     for num in args:
#         sum+=num
#     return sum

# print(add_all(1,2,3,4,5))


# def print_data(**kwargs):
#     for key,value in kwargs.items():
#         print(f"{key}:{value}")

# print_data(Name="Niha", Age=25)


def profileGen(**kwargs):
    for key,value in kwargs.items():
        print(f"{key}:{value}")


name=input("Enter Full Name:")
email=input("Enter Email:")
number=input("Enter Phone Number:")
age=int(input("Enter Age:"))
gender=input("Enter Gender:")
city=input("Enter City:")
print()

profileGen(Name=name.title().strip(),Email=email.strip(),Number=number,Age=age,Gender=gender,City=city)

