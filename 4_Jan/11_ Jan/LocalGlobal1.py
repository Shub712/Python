No = 11     # Global

def fun():
    No = 21  # Local
    print("Value of No from fun is : ", No) # Local  21

print("Value of No is :", No) # Global 11
fun()
