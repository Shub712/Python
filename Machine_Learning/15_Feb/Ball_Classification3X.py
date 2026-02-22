from sklearn import tree

# Rough = 1 
# Smooth = 0

# Tennis = 1
# Cricket = 2

def main():
    print("Ball Classsification case study")


    # Independent Variables : [Weight, Surface]
    Features = [[35,1],[47,1],[90,0],[48,1],[90,0],[35,1],[92,0],[35,1],[35,1],[35,1],[96,0],[43,1],[110,0],[35,1],[95,0]]

    # Depenedent Variables
    Labels = [1,1,2,1,2,1,2,1,1,1,2,1,2,1,2]
    
    modelobj = tree.DecisionTreeClassifier()   # Model Selection
    
    trainedmodel = modelobj.fit(Features,Labels)    # Training Model
    
    Result = trainedmodel.predict([[37,1],[94,0]])  # 1  2
    
    print("Model Predicts the object as : ",Result) #[1 2]
    


if __name__ =="__main__":
    main()

