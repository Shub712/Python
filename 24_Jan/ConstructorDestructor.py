import gc

class Demo:
    def __init__(self):
        print("Inside Constructor")
    
    def __del__(self):
        print("Inside Destructor")

# Allocate
obj = Demo()    # Memory gets allocated to the object

# Use

# Deallocate the memory
del obj         # Its like free() and delete()

gc.collect()    # Request to the garbage collector 

print("End of application")