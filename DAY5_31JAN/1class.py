# #CLASS, METHOD, OBJECT
# class Student:

#     #CONSTRUCTOR
#     def __init__(self, name, age):
#         self.name= name 
#         self.age = age

#     #METHOD
#     def display(self):
#         print(f"Name: {self.name}, Age: {self.age}")

# name=input("Enter Name:")
# age=input("Enter Age:")

# #OBJECT
# s1=Student(name,age)
# s1.display()



#Create employee details using: class, object, constructor, mthods
class Employee:

    def __init__(self,name,age,dept,salary):
        self.name=name
        self.dept=dept 
        self.age=age
        self.salary=salary
    
    def display(self):
        print(f"Employee Name:{self.name} \nEmployee Age:{self.age} \nEmployee Department: {self.dept} \nEmployee Salary: {self.salary} ")

for i in range(3):
    name=input("Enter Employee Name:")
    age=input("Enter Employee Age:")
    dept=input("Enter Employee Department:")
    salary=input("Enter Employee Salary:")

    e=Employee(name,age,dept,salary)
    e.display()
