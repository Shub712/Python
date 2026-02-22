from sklearn.datasets import load_iris

def main():
    
    print("Iris Classification case study")
    
    # Metadata of dataset
    DataSet = load_iris()
    print("Independant Variable Are : ")
    print(DataSet.feature_names)
    print("Length of independant variables is : ",len(DataSet.feature_names))
    
    print("Dependant variables are :")
    print(DataSet.target_names)
    print("Length of dependant variables is : ",len(DataSet.target_names))
    
    
if __name__ == "__main__":
    main()