import time
import multiprocessing

def SumCube(No):
    Sum = 0 

    for i in range(1,No+1):
        Sum = Sum + (i ** 3)
    
    return Sum

def main():
    Data = [100000,200000,300000,400000,500000,600000,700000,800000,900000,100000]
    Result = []

    Start_Time = time.time()

    pobj = multiprocessing.Pool()
    Result = pobj.map(SumCube,Data)

    pobj.close()
    pobj.join()
    
    End_time = time.time()
    
    print(Result)
    print("Total time of execution :" , End_time - Start_Time)

if __name__ == "__main__":
    main()