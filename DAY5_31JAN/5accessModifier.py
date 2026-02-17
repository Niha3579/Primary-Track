class Parent:
    def __init__(self):
        selfpublic_var="Public"
        self_protected_var="Protected"
        self__private_var="Private"

    def access_from_same_class(self):
        print("Inside Parent Class")
        print("Public",self.public_var)
        print("Protected",self.protected_var)
        print("Private",self.private_var)

class Child(Parent):
    def access_from_child_class(self):
        print("Inside child class(Student):")
        print("Public", self.public_var)
        print("Protected",self.protected_var)
        print("Private",self.private_var)
        try:
            print("Private:", self.__private_var)
        except AttributeError:
            print("Private: ❌ Cannot access (AttributeError)")

class Stranger:
    def access_from_other_class(self, obj):
        print("Inside Stranger class (Unrelated):")
        print("Public:", obj.public_var)
        print("Protected:", obj._protected_var)  # ⚠️ Not recommended
        try:
            print("Private:", obj.__private_var)
        except AttributeError:
            print("Private: ❌ Cannot access (AttributeError)")
