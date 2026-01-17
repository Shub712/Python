from MarvellousFMR import filterX,mapX,reduceX

CheckEven = lambda No : (No % 2 == 0)
Increment = lambda No : No + 1
Add = lambda A,B : A + B

def main():
    Data = [11,10,15,20,22,27,30]
    print("Actual Data is : ", Data)

    FData = list (filterX(CheckEven,Data))  
    print("Data After filter : ", FData)

    MData = list(mapX(Increment,FData))    
    print("Data After map : ",MData)

    RData = reduceX(Add,MData)
    print("Data After Reduce is : ", RData)
    
if __name__ == "__main__":
    main()

#   OUTPUT :
#
#   Actual Data is :  [11, 10, 15, 20, 22, 27, 30]
#   Data After filter :  [10, 20, 22, 30]
#   Data After map :  [11, 21, 23, 31]
#   Data After Reduce is :  86
