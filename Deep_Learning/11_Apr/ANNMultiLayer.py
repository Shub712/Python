#-------------------------------------------------------
# Network Structure :
#   Input Layer : 2 Inputs
#   Hidden Layer : 2 neurons with ReLU activation
#   Output Layer : 1 neuron with sigmoid activation
#
# Purpose : 
#   To understand how data moves from input layer
#   To hidden layer and finally to output layer 
#-------------------------------------------------------

import math

#-------------------------------------------------------
# Function name : Marvellous_ReLU
# Description : Applies ReLU activation function
# Formula : ReLU(x) = max(0,x)
# Use : Commonly used in hidden layers
#-------------------------------------------------------

def Marvellous_ReLU(value):
    return max(0,value)

#-------------------------------------------------------
# Function name : Marvellous_Sigmoid
# Description : Applies Sigmoid activation function
# Formula : 1 /(1 + e ^ (-x))
# Use : commonly used in output layer for binary classification
# Output Range : 0 to 1
#-------------------------------------------------------

def Marvellous_Sigmoid(value):
    return 1 / (1 + math.exp(-value))

#-------------------------------------------------------
# Function name : Marvellous_Calculated_Weighted_Sum
# Description : Displays step-by-step multiplication of
#               inputs and weights for 1 neuron
# Parameters :
#   inputs : list of inputs
#   weights : List of weights
#-------------------------------------------------------

def Marvellous_Calculated_Weighted_Sum(inputs,weights,bias):
    weighted_sum = sum(weight * input_value for weight,input_value in zip(weights,inputs)) + bias
    
    return weighted_sum

def Marvellous_Display_Multiplication_Details(inputs,weights):
    print(" Step 1 : Multiply Inputs by corresponding weights")
    
    for index in range(len(inputs)):
        print(
            f" ({weights[index]} * {inputs[index]}) = {weights[index] * inputs[index]:.3f}"
        )
        
#-------------------------------------------------------
# Function name : Marvellous_Process_Hidden_Layer
# Description : Process All neurons of hidden layer
#               using ReLU Activation function
# Parameters :
#   inputs : Input values from input layer
#   hidden_weights : weight matrix for hidden layer
#   hidden_biases : bias list of hidden neurons
# returns  : List of hidden layer outputs
#-------------------------------------------------------

def Marvellous_Process_Hidden_Layer(inputs,hidden_weights,hidden_biases):
    hidden_outputs = []
    
    print("\n==================== HIDDEN LAYER ======================")
    
    for neuron_index in range(len(hidden_weights)):
        print(f"Hidden Neuron {neuron_index + 1}:")
        
        current_weights = hidden_weights[neuron_index]
        curren_bias = hidden_biases[neuron_index]
        
        # Display Multiplication Details
        Marvellous_Display_Multiplication_Details(inputs,current_weights)
        
        # Calculated Weighted Sum
        z_value = Marvellous_Calculated_Weighted_Sum(inputs,current_weights,curren_bias)
        print(f" Step 2 : Add all multiplication results and bias {curren_bias}")
        print(f" z = {z_value:.3f}")
        
        # Apply ReLU Activation
        
        activated_output = Marvellous_ReLU(z_value)
        print(f" Step 3 : Apply ReLU activation")
        print(f" ReLU({z_value:.3f}) = {activated_output:.3f}\n")
        
        hidden_outputs.append(activated_output)
        
    return hidden_outputs

#-------------------------------------------------------
# Function name : Marvellous_Process_Output_Layer
# Description : Processes output layer neuron using
#               sigmoid activation function
# Parameters :
#   hidden_outputs : Output from hidden layer
#   output_weights : weight of output neuron
#   output_bias : bias of output neuron
# returns  : final weighted sum and final output
#-----------------------------------------------------

def Marvellous_Process_Output_Layer(hidden_outputs,output_weights,output_bias):
    print("\n ========================= OUTPUT LAYER =======================")
    print("Output Neuron :")
    print("Step 1 : Multiply hidden layer outputs by output weights")
    
    for index in range(len(hidden_outputs)):
        print(
            f" ({output_weights[index]} * {hidden_outputs[index]:.3f}) ="
            f"{output_weights[index] * hidden_outputs[index]:.3f}"
        )
        
        # calculate weighted sum of output layer
        z_output = Marvellous_Calculated_Weighted_Sum(hidden_outputs,output_weights,output_bias)
    
    print(f" Step 2 : Add all multiplication results and bias {output_bias}")
    print(f"  z = {z_output:.3f}")
    
    # Apply sigmoid activation
    
    final_ouput = Marvellous_Sigmoid(z_output)
    print(f"Step 3: Apply sigmoid activation")
    print(f" Sigmoid({z_output:.3f}) = {final_ouput:.3f}")
    
    return z_output,final_ouput

#-------------------------------------------------------
# Function name : Marvellous_Display_Network_Summary
# Description : Dsiplays Final output of network
# Parameters :
#   hidden_outputs : Hidden layer output
#   final_output :  Output layer final output
#-----------------------------------------------------

def Marvellous_Display_Network_Summary(hidden_outputs,final_output):
    print("\n================= FINAL SUMMARY ==================")
    print(f"Hidden Layer Outputs : {hidden_outputs}")
    print(f" Final Network Output : {final_output:.3f}")
    print(f"Confidence Percentage : {final_output * 100:.2f}%")
    
    if final_output>0.5:
        print("Prediction   : Positive Class")
    else:
        print("Prediction    : Negative Class")


#-------------------------------------------------------
# Function name : Marvellous_ANN_Forward_Pass
# Description : Complete Forward pass of ANN
# Parameters :
#   inputs : List of input values
# Flow:
#       Input Layer -> Hidden Layer -> Output Layer
#-------------------------------------------------------

def Marvellous_ANN_Forward_Pass(inputs):
    print("====================== INPUT LAYER ======================")
    print(f"input x1 = {inputs[0]}")
    print(f"input x2 = {inputs[1]}")
    
    #-------------------------------------------
    # Hidden layer weights and biases
    # Two neurons in hidden layer
    #-------------------------------------------
    
    hidden_weights = [
        [0.5,-0.2], # Weights for hidden neuron 1
        [0.8,0.4]   # Weights for hidden neuron 2
    ]
    
    hidden_biases = [
        0.1, # bias for hidden neuron 1
        -0.1 # Bias for hidden neuron 2
    ]
    
    #--------------------------------------------
    # Output layer weights and bias
    # One neuron in output layer 
    #--------------------------------------------
    output_weights = [1.0,-1.5]
    output_bias = 0.2
    
    # Process Hidden layer
    
    Hidden_outputs = Marvellous_Process_Hidden_Layer(
        inputs,
        hidden_weights,
        hidden_biases
    )
    
    # Process output layer
    
    z_output,final_output = Marvellous_Process_Output_Layer(
        Hidden_outputs,
        output_weights,
        output_bias
        
    )
    
    # Display Summary
    Marvellous_Display_Network_Summary(Hidden_outputs,final_output)
    
def main():
     # Example input values 
     # You can change these values and test different outputs  
     
     inputs = [2.0,3.0]
     
     # Start ANN Forward Pass
     Marvellous_ANN_Forward_Pass(inputs)

if __name__ == "__main__":
    main()  