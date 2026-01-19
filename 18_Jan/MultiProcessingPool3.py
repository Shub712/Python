import time
import os

def SumCube(No):
    print("Process is running with PID : ", os.getpid())
    Sum = 0 

    for i in range(1,No+1):
        Sum = Sum + (i ** 3)
    
    return Sum

def main():
    Data = [1000000,2000000,3000000,4000000,5000000,6000000,7000000,8000000,9000000,1000000]
    Result = []

    Start_Time = time.time()

    for i in range(len(Data)):
        Ret = SumCube(Data[i])
        Result.append(Ret)

    End_time = time.time()
    
    print(Result)
    print("Total time of execution :" , End_time - Start_Time)

if __name__ == "__main__":
    main()