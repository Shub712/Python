class Parent:
    def __init__(self):
        print("Inside Parent Constructor")
     
    def fun(self):
        print("Inside fun method of parent")

class Child(Parent):
    def __init__(self):         
        super().__init__()          # Compulsory to call if there is an instance variable in parent class
        print("Inside Child Constructor")

    def fun(self):
        super().fun()
        print("Inside fun method of child")

cobj = Child()

cobj.fun()
