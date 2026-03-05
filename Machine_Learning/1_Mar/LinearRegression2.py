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
    
    print("X_Mean is : ", mean_X)   # 3.0
    print("Y_Mean is : ", mean_Y)   # 3.6
    
    n = len(X)  # 5
    
    # Y = mX + C  
    
    # m = (Summ (x-X_bar) * (y-Y_bar)) / (Sum (X - X_bar)**2)
    
    numerator = 0
    denominator = 0
    
    for i in range(n):
        numerator = numerator + ((X[i] - mean_X) * (Y[i] - mean_Y))
        denominator = denominator + ((X[i] - mean_X)**2)
    
    m = numerator / denominator
    
    print("Slope of line that is m : ", m)  # 0.4
    
    c = mean_Y - (m * mean_X)
    
    print("Y intercept line that is C : ", c)
    
def main():
    MarvellousPredictor()
    
if __name__ == "__main__":
    main()