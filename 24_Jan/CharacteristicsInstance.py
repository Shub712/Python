import gc

class Demo:
    No1 = 11        # Class Variable
    No2 = 10        # Class Variable

    def __init__(self):

        self.A = 101        # Instance Variable
        self.B = 201        # Instance Variable
        print("Inside Constructor")
    
    def __del__(self):
        print("Inside Destructor")

print(Demo.No1)
print(Demo.No2)

obj = Demo()

print(obj.A)
print(obj.B)


