import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


def MarvellousPredictor():
    # Load The data
    
    X = [1,2,3,4,5]
    Y = [3,4,2,4,5]
     
    print("Values Of Independant Variable : X - ", X)   
    print("Values Of Dependant Variable : Y - ", Y)   

    mean_X = np.mean(X)
    mean_Y = np.mean(Y)
    
    print("X_Mean is : ", mean_X)
    print("Y_Mean is : ", mean_Y)
    
def main():
    MarvellousPredictor()
    
if __name__ == "__main__":
    main()