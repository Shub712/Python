
#-------------------------------------------------------
# Program : Sigmoid vs ReLU Neuron Comparison
# Author : Shubham Kiran Pawar
#-------------------------------------------------------

import math
import matplotlib.pyplot as plt
import numpy as np

#------------------------------------------------------
# STEP 1 : Activation Functions
#------------------------------------------------------

def Sigmoid(z):
    """
    Sigmoid Activation Function
    Output range : (0,1)
    Used For probablity-based outputs
    
    """
    
    return 1 / (1 + math.exp(-z))

def ReLU(z):
    """
    ReLU Activation Function
    output : max(0,z)
    Used in hidden layers of deep networks  
    
    """
    
    return max(0,z)

#-------------------------------------------------------
# STEP 2 : Neuron Forward Pass
#-------------------------------------------------------
# Generic neuron -> works with any activation function

def Marvellous_neuron_forward(inputs,weights,bias):
    
    print("\n------- NEURON CALCULATION ------\n")
    
    # Display input details
    
    print("Inputs (x) : ",inputs)
    print("Weights (w) : ",weights)
    print("Bias (b) : ",bias)
    
    #---------------------------------------------------
    # Weighted Sum Calculation
    # z = w.x + b   
    #---------------------------------------------------
    
    z = sum(w * x for w,x in zip(weights,inputs)) + bias
    
    print("\nStep 1 : Weighted Sum")
    print("z = ",z)
    
    #--------------------------------------------------
    # Apply sigmoid
    #--------------------------------------------------
    y_hat = Sigmoid(z)
    
    print("\nStep 2 : Activation Function")
    print("Activation Function : ",Sigmoid)
    print("Output(y) : ",y_hat)
    
    print("\n-------------- NEURON CALCULATION END -------------------\n")
    
    return z,y_hat

#---------------------------------------------------
# STEP 3 : Plot Sigmoid Function
#---------------------------------------------------

def plot_sigmoid():
    
    # Generate input range
    z_values = np.linspace(-10,10,200)
    
    # Apply sigmoid on range
    sigmoid_values = 1 / (1 + np.exp(-z_values))
    
    #plot graph
    plt.figure(figsize=(8,5))
    plt.plot(z_values,sigmoid_values,label = "Sigmoid Function",linewidth=2,color="blue")
    
    # Reference Lines 
    
    plt.axhline(y=0,color="black",linewidth=0.5)
    plt.axhline(y=1,color="black",linewidth=0.5)
    
    plt.axvline(x=0,color="grey",linestyle="--")
    
    # Labels and title
    plt.title("Sigmoid Activation Function",fontsize=16)
    plt.xlabel("Input(z)",fontsize = 14)
    plt.ylabel("Output (Probablity)",fontsize=14)
    
    # Grid and legend
    plt.grid(True,linestyle="--",alpha=0.6)
    plt.legend
    
    plt.show()
    
#-------------------------------------------
# STEP 4 : Main Function
#-------------------------------------------

def main():
    
    print("\n================= MARVELLOUS SIGMOID FUNCTION ==================")
    
    # Example inputs
    inputs = [1.0,2.0,3.0]
    
    # Weights
    weights = [0.6,0.4,-0.2]
    
    # Bias
    bias = 0.5

    # Forward Pass
    z,y_hat=Marvellous_neuron_forward(inputs,weights,bias)
    
    print("Final z : ", z)
    print("Final y_hat : ",y_hat)
    
    plot_sigmoid()


if __name__ == "__main__":
    main()    
    