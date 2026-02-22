# Map

def CheckEven(No):
    return (No % 2 == 0)

def Increment(No):
    return No + 1

def main():
    Data = [11,10,15,20,22,27,30]
    print("Actual Data is : ", Data)

    FData = list (filter(CheckEven,Data))   # Return value of filter is boolean
    print("Data After filter : ", FData)

    MData = list(map(Increment,FData))      # return value of map is ID
    print("Data After map : ",MData)
    
if __name__ == "__main__":
    main()