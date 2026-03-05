#   [A,B,C,D]
# X [1,2,3,5]
# Y [2,3,1,6]
#   [R,R,B,B]

# R = RED
# B = BLUE

# Predict = (3,3) -> ?

import numpy as np
import math


def EucDistance(P1,P2):
    Ans = math.sqrt((P1['X'] - P2 ['X'])**2 + (P1['Y'] - P2['Y'])**2)
    return Ans

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
    
    new_point = {'X': 3 , 'Y': 3} # testing
    
    for d in Data:
        d['distance'] = EucDistance(d,new_point) 
    
    print(Border)
    print("Calculated Distances are:")
    print(Border)
    
    for d in Data:
        print(d)
    
    sorted_data = sorted(Data,key=lambda item: item['distance'])
    
    print(Border)
    print("sorted data is :")
    print(Border)
    
    for d in sorted_data:
        print(d)
    
    k = 3
    nearest = sorted_data[:k]
    
    print(Border)
    print("Nearest 3 elements are :")
    print(Border)
    
    for d in nearest:
        print(d)
    
    # voting
    
    votes = {}
    
    for neighbour in nearest:
        label = neighbour['label']
        votes[label] = votes.get(label,0)+1
        
    print(Border)
    print("Voting Result :")
    print(Border)
    
    for d in votes:
        print("Name : ",d,"Number of votes : ",votes[d])
        
    print(Border)

def main():
    MarvellousKNeighborsClassifier()
    
if __name__ == "__main__":
    main()