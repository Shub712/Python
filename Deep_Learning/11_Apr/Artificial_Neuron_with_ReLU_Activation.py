#-----------------------------------------------------
# Program : Artificial Neuron with ReLU Activation
# Author : Shubham Kiran Pawar
#-----------------------------------------------------

import matplotlib.pyplot as plt
import numpy as np

#-------------------------------------------------------
# Step 1 : Activation Fuction (ReLU)
#-------------------------------------------------------
# ReLU = max(0,z)
# if z is postive -> output is z
# if z is negative -> output is 0

def Relu(z):
    return max(0,z)


#-------------------------------------------------------
# Step 2 : Neuron Forward Pass Function
#-------------------------------------------------------
# This function simulates a single artificial neuron
# ir performs 
# 1 . Input x Weights Multiplication
# 2 . Summation + Bias
# 3 . Activation(ReLU)

def Marvellous_neuron_forward(inputs,weights,bias):
    print("\n-------- NEURON CALCULATION START ---------\n")
    
    # Display inputs and weights 
    print("Inputs (x) : ", inputs)
    print("Weights (w) : ", weights)
    print("Bias (b) : ",bias)
    


    #-------------------------------------------------------
    # Step 2.1 : Weighted sum calculation
    # Formula : (x1*w1 + x2*w2 + ....+xn*wn) + bias
    #-------------------------------------------------------

    z = sum(w * x for w,x in zip(weights,inputs)) + bias

    print("\nStep 1 : Weighted Sum calculation")
    print("z = w*x + b =", z)
    
    #-------------------------------------------------------
    # Step 2.2 : Activation Function
    #-------------------------------------------------------

    y_hat = Relu(z)
    
    print("\nStep 2 : Activation Function Applied")
    print("Activation Function : ReLU")
    print("Output (y) = ", y_hat)
    
    print("\n------- NEURON CALCULATION END --------")
    
    return z,y_hat

#-------------------------------------------------------
# Step 3  : Plot ReLU Function
#-------------------------------------------------------
# This Helps to visualize how ReLU Behaves

def Plot_relu():
    
    # Generate range of values for z 
    z_values = np.linspace(-10,10,200)
    
    # Apply ReLU on all values 
    relu_values = np.maximum(0,z_values)
    
    # Plot graph
    plt.figure(figsize=(8,5))
    plt.plot(z_values,relu_values, label= "ReLU Function",linewidth=2,color = "green")
    
    # Axes Lines
    plt.axhline(y=0,color="black",linewidth=0.5)
    plt.axvline(x=0,color = "grey",linestyle = "--")
    
    # Labels and title
    plt.title("ReLU Activation Function",fontsize=16)
    plt.xlabel("Input (z)",fontsize = 14)
    plt.ylabel("Output",fontsize = 14)
    
    # Grid and Legend
    plt.grid(True,linestyle="--",alpha =0.6)
    plt.legend()
    
    # Show graph
    plt.show()
    
#-------------------------------------------------------
# Step 4 : Main Function
#-------------------------------------------------------

def main():
    
    print("\n============= MARVELLOUS NEURON DEMO ===========")
    
    # Example inputs(features)
    inputs = [1.0,2.0,3.0]
    
    # Corresponding Weights 
    weights = [0.6,0.4,-0.2]
    
    # Bias value
    bias = 0.5
    
    # Perform forward propagation
    z,y_hat = Marvellous_neuron_forward(inputs,weights,bias)
    
    Plot_relu()
    
if __name__ == "__main__":
    main()