#   [A,B,C,D]
# X [1,2,3,5]
# Y [2,3,1,6]
#   [R,R,B,B]

# R = RED
# B = BLUE

# Predict = (3,3)

def MarvellousKNeighborsClassifier():
    Border = "-"*40
    Data =[
                {'Point' : 'A', 'X' : 1, 'Y' : 2, 'label' : 'Red'},
                {'Point' : 'B', 'X' : 2, 'Y' : 3, 'label' : 'Red'},
                {'Point' : 'C', 'X' : 3, 'Y' : 1, 'label' : 'Blue'},
                {'Point' : 'D', 'X' : 5, 'Y' : 6, 'label' : 'Blue'}
          ]
    
    print(Border)
    print("Marvellous UserDefined KNN")
    print(Border)
    
    print(Border)
    print("Training Dataset")
    print(Border)
    
    for i in Data:
        print(i)
    
    print(Border)

def main():
    MarvellousKNeighborsClassifier()
    
if __name__ == "__main__":
    main()