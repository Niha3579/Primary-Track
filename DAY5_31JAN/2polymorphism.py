#METHOD OVERLOADING: methods with same name and different parameters

# class Employee:
#     def display(self,*args):
#         if len(args)==1:
#             print(f"Employee Name:{name}")
#         elif len(args)==2:
#             print(f"Employee Name:{name} \nEmployee Age:{age}")
#         elif len(args)==3:
#             print(f"Employee Name:{name} \nEmployee Age:{age} \nEmployee Department: {dept}")
#         else:
#             print(f"Employee Name:{name} \nEmployee Age:{age} \nEmployee Department: {dept} \nEmployee Salary: {salary} ")

# for i in range(1):
#     name=input("Enter Employee Name:")
#     age=input("Enter Employee Age:")
#     dept=input("Enter Employee Department:")
#     salary=input("Enter Employee Salary:")

#     e=Employee()
#     e.display(name,age)
#     e.display(name,age,dept,salary)



# #
# class Display:
#     def show(self, *args):
#         if len(args)==1:
#             if isinstance(args[0],str):
#                 print("Name:",args[0])
#             elif isinstance(args[0], int):
#                 print("Age:",args[0])
#             print("One value:",name)
            



#METHOD OVERRIDING: child class overrides the functionality of the parent class
#RUNTIME POLYMORPHISM

# class Animal:
#     def sound(self):
#         print("Some generic sound")

# class Dog(Animal):
#     def sound(self):
#         print("Bark")

# class Cat(Animal):
#     def sound(self):
#         print("Meow")

# for creatures in [Dog(),Cat()]:
#     creatures.sound()


#DUCK TYPING
class Pycharm:
    def execute(self):
        print("Compiling + Running!")

class VSCode:
    def execute(self):
        print("Running + Linting")

def code(editor):
    editor.execute()

code(Pycharm())
code(VSCode())