from sklearn import tree

# Rough = 1 
# Smooth = 0

# Tennis = 1
# Cricket = 2

def main():
    
    print("Ball Classsification case study")

    # Original Encoded Data Set
    # Independent Variables : [Weight, Surface]
    X = [[35,1],[47,1],[90,0],[48,1],[90,0],[35,1],[92,0],[35,1],[35,1],[35,1],[96,0],[43,1],[110,0],[35,1],[95,0]]

    # Original Encoded Data Set
    # Depenedent Variables 1 - tennis 2 - cricket
    Y = [1,1,2,1,2,1,2,1,1,1,2,1,2,1,2]
    
    # Independant Variables for training
    XTrain= [[35,1],[47,1],[90,0],[48,1],[90,0],[35,1],[92,0],[35,1],[35,1],[35,1],[96,0],[43,1],[110,0]]
    
    # Independant Variables for testing
    XTest = [[35,1],[95,0]]
    
    # Dependant Variables for training
    YTrain = [1,1,2,1,2,1,2,1,1,1,2,1,2]
    
    # Dependant Variables for testing
    YTest = [1,2]
    
    modelobj = tree.DecisionTreeClassifier()   # Model Selection
    
    trainedmodel = modelobj.fit(XTrain,YTrain)    # Training Model
    
    Result = trainedmodel.predict(XTest)  
    
    print("Model Predicts the object as : ",Result) # [1 2]
    
if __name__ =="__main__":
    main()

