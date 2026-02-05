class Circle:
    PI = 3.14

    def __init__(self):
        self.Radius = 0.0
        self.Area = 0.0
        self.CircumferenceX = 0.0

    def Accept(self,A):
        self.Radius = A

    def CalculateArea(self):
        self.Area = Circle.PI * self.Radius * self.Radius

    def Circumference(self):
        self.CircumferenceX = 2 * Circle.PI * self.Radius

    def Display(self):
        print("Circumference :",self.CircumferenceX)
        print("Radius is : ",self.Radius)
        print("Area is : ",self.Area)

def main():

    obj1 = Circle()
    obj1.Accept(4.0)
    obj1.CalculateArea()
    obj1.Circumference()
    obj1.Display()

    print("---------------------------------")

    obj2 = Circle()
    obj2.Accept(5.0)
    obj2.CalculateArea()
    obj2.Circumference()
    obj2.Display()

if __name__ == "__main__":
    main()