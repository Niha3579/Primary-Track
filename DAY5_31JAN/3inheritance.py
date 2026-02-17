#SINGLE INHERITANCE
# class Father():
#     def drive(self):
#         print("Father can drive!")

# class Son(Father):
#     def play(self):
#         print("Son can play")

# s=Son()
# s.drive()
# s.play()



#MULTI-LEVEL INHERITANCE
# print("Multi Level Inheritance")
# class Grandfather:
#     def wisdom(self):
#         print("Grandfather shares wisdom")

# class Father(Grandfather):
#     def drive(self):
#         print("Father can drive")

# class Son(Father):
#     def play(self):
#         print("Son can play")

# s=Son()
# s.wisdom()
# s.drive()
# s.play()


#HIERARCHIAL INHERITANCE
# class Mother:
#     def cook(self):
#         print("Mother cooks well")

# class Daughter:
#     def dance(self):
#         print("Daughter can dance")

# class Son(Mother):
#     def play(self):
#         print("Son can play")

# m=Mother()
# d=Daughter()
# s=Son()
# s.cook()
# d.cook()



#MULTIPLE INHERITANCE
# class Father:
#     def drive(self):
#         print("Father Drive")

# class Mother:
#     def cook(self):
#         print("Mother cooks!")

# class Child(Father, Mother):
#     def play(self):
#         print("Child Plays")

# c=Child()
# c.drive()
# c.cook()
# c.play()


#HYBRID INHERITANCE
# class A:
#     def method_a(self):
#         print("A")

# class B:
#     def method_b(self):
#         print("B")

# class C:
#     def method_c(self):
#         print("C")

# class D(B,C):
#     def method_d(self):
#         print("D")


class A:
    def display(self):
        print("Hello A")

class B:
    def display(self):
        print("Hello B")
    def hi(self):
        print("Hello B")

class C(A,B):
    def display(self):
        A.display(self)
        B.display(self)
        super(A,self).display()

ci=C()
ci.display()
# ci.hi()

