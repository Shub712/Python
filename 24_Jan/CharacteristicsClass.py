import gc

class Demo:
    No1 = 11        # Class Variable
    No2 = 10        # Class Variable

    def __init__(self):
        print("Inside Constructor")
    
    def __del__(self):
        print("Inside Destructor")

print(Demo.No1)
print(Demo.No2)

