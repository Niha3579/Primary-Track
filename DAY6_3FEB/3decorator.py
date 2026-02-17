
#decorators main usage 

# def my_decorator(func):
#     def wrapper():
#         print("Before the function call")
#         func()
#         print("After the function call")
#     return wrapper

# @my_decorator
# def say_hello():
#     print("Hello!")


#second
# def decorator(func):
#     def wrapper(*args,**kwargs):
#         print("Before the function call!")
#         result=func(*args,**kwargs)
#         print("After the function call")
#         return result
#     return wrapper

# @decorator
# def add(a,b):
#     return a+b

# print(add(3,5))




#decorator with parameter

# def repeat(n):
#     def decorator(func):
#         def wrapper(*args, **kwargs):
#             for _ in range(n):
#                 func(*args,**kwargs)
#         return wrapper
#     return decorator


# @repeat(3)
# def greet():
#     print("Hello")

# greet()



#
# class Mathutils:
#     @staticmethod
#     def add(a,b):
#         return a+b

# print(Mathutils.add(5,7))


#
# class student:
#     school_name="ABC"

#     def __init__(self,name,age):
#         self.name=name
#         self.age=age

#     @classmethod
#     def change_school_name(cls,new_name):
#         cls.school_name=new_name

# print("Before Change:",student.school_name)
# student.change_school_name("XYZ")
# print("After change:",student.school_name)




# def print_details(func):
#     def wrapper(employee):
#         print(f"Salary: {employee['salary']}")
#         print(f"Designation: {employee['designation']}")
#         return func(employee)
#     return wrapper

# @print_details
# def call_employee(employee):
#     print(f"Calling employee: {employee['name']}")

# employee1 = {
#     "name": "Rahul",
#     "salary": 50000,
#     "designation": "Software Engineer"
# }

# call_employee(employee1)


# def salary(func):
#     def wrapper():
#         print("Salary: 20000 ")
#         func()
#         return wrapper

# def designation(func):
#     def wrapper():
#         print("Designation: lawyer")
#         func()
#         return wrapper

# @salary
# @designation
# def employee():
#     print("Employee record displayed")

# employee()


# def login_required(func):
#     def wrapper():
#         user_authenticated=True
#         if user_authenticated:
#             return func()
#         else:
#             print("User not authenticated, Please log in")
#     return wrapper

# @login_required
# def view_dashboard():
#     print("Registration Successful! welcome to your dashboard")

# view_dashboard



#REGISTRATION FORM:


# three topics: module,package,decorators, create employee management system, 
# organize packages and modules, control decorators, login and registration
# main folder: init.py to create package, folder decorators: access.py, employee: details.py, main.py





numbers=[1,2,3,4,5]
it=iter(numbers)

print(next(it))
print(next(it))
print(next(it))

for i in range(5):
    print(i)