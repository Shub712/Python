
############################################################################
#   SINGLY LINEAR LINKEDLIST 
############################################################################

class SinglyLLNode:
    
    def __init__(self,value):
        self.data = value
        self.next = None

class SinglyLL:  
    
    def __init__(self):
        self.first = None
        self.iCount = 0
        
#////////////////////////////////////////////////////////////////////
#//
#//  Function Name : InsertFirst
#//  Input :         Data of Node  
#//  Output :        Nothing
#//  Description :   Used to insert node at the first position
#//  Author :        Shubham Kiran Pawar
#//  Date :          28/03/2026
#//
#////////////////////////////////////////////////////////////////////
    
    
    def InsertFirst(self,no):
        newn = SinglyLLNode(no)
        
        if self.first == None:
            self.first = newn
        
        
        else:
            newn.next = self.first
            self.first = newn
        
        self.iCount = self.iCount+1
        
    #////////////////////////////////////////////////////////////////////
    #//
    #//  Function Name : InsertLast
    #//  Input :         Data of Node  
    #//  Output :        Nothing
    #//  Description :   Used to insert node at the last position
    #//  Author :        Shubham Kiran Pawar
    #//  Date :          28/03/2026
    #//
    #////////////////////////////////////////////////////////////////////
    
    def InsertLast(self,no):
        newn = SinglyLLNode(no)
        
        if self.first == None:
            self.first = newn
    
        else:
           
            temp = self.first
           
            while(temp.next != None):
               temp = temp.next
        
            temp.next = newn
            
        self.iCount = self.iCount+1    
    
    #////////////////////////////////////////////////////////////////////
    #//
    #//  Function Name : InsertAtPos
    #//  Input :         Data of Node and position 
    #//  Output :        Nothing
    #//  Description :   Used to insert node at the gioven position
    #//  Author :        Shubham Kiran Pawar
    #//  Date :          28/03/2026
    #//
    #////////////////////////////////////////////////////////////////////
    
    def InsertAtPos(self,no,pos):
        
        if pos < 1 or pos > self.iCount + 1:
            print("Invalid Postion")
            return
        
        if (pos == 1):
            self.InsertFirst(no)
            return
        
        elif pos == (self.iCount + 1):
            self.InsertLast(no)
            return
        
        else:
            
            newn = SinglyLLNode(no)
            
            temp = self.first
            
            for i in range(1,pos-1):
                temp = temp.next

            newn.next = temp.next
            temp.next = newn
            
            self.iCount = self.iCount + 1
     
    #////////////////////////////////////////////////////////////////////
    #//
    #//  Function Name : DeleteFirst
    #//  Input :         None  
    #//  Output :        None
    #//  Description :   Used to delete node at the first position
    #//  Author :        Shubham Kiran Pawar
    #//  Date :          28/03/2026
    #//
    #////////////////////////////////////////////////////////////////////      
    
    def DeleteFirst(self):
        
        if self.first == None:
            return
        
        temp = self.first
        
        self.first = self.first.next
        self.iCount = self.iCount - 1
         
    
    #////////////////////////////////////////////////////////////////////
    #//
    #//  Function Name : DeleteLast
    #//  Input :         None 
    #//  Output :        None
    #//  Description :   Used to delete node at the last position
    #//  Author :        Shubham Kiran Pawar
    #//  Date :          28/03/2026
    #//
    #////////////////////////////////////////////////////////////////////
    
    def DeleteLast(self):
        
        if self.first == None:
            return
        
        if(self.first.next == None):
            del self.first
            
            self.first = None
            self.iCount = 0 
        
        else:
            
            temp = self.first
    
            while(temp.next.next != None):
                temp = temp.next
            
            del temp.next
            temp.next = None
            
            self.iCount = self.iCount - 1
    
    #////////////////////////////////////////////////////////////////////
    #//
    #//  Function Name : DeleteAtPos
    #//  Input :         None
    #//  Output :        None
    #//  Description :   Used to delete node at from the given  position
    #//  Author :        Shubham Kiran Pawar
    #//  Date :          28/03/2026
    #//
    #////////////////////////////////////////////////////////////////////
    
    def DeleteAtPos(self,pos):
        
        if pos < 1 or pos > self.iCount:
            print("Invalid Postion")
            return
        
        if (pos == 1):
            self.DeleteFirst()
            return
        
        elif pos == (self.iCount):
            self.DeleteLast()
            return
        
        else:
            
            temp = self.first
            
            for i in range(1,pos-1):
                temp = temp.next

            temp.next = temp.next.next
            self.iCount = self.iCount - 1
    
    #////////////////////////////////////////////////////////////////////
    #//
    #//  Function Name : Count
    #//  Input :         None 
    #//  Output :        None
    #//  Description :   Used to return count of the nodes
    #//  Author :        Shubham Kiran Pawar
    #//  Date :          28/03/2026
    #//
    #////////////////////////////////////////////////////////////////////
    
    def Count(self):
        return self.iCount
    
    #////////////////////////////////////////////////////////////////////
    #//
    #//  Function Name : Display
    #//  Input :         None  
    #//  Output :        None
    #//  Description :   Used to display the nodes of the linked list
    #//  Author :        Shubham Kiran Pawar
    #//  Date :          28/03/2026
    #//
    #////////////////////////////////////////////////////////////////////
    
    def Display(self):
        
        temp = self.first
        
        while(temp != None):
            print("| ",temp.data,"| ->",end=" ")
            temp = temp.next 
               
        print("None")
    
    #////////////////////////////////////////////////////////////////////
    #//
    #//  Function Name : SearchByPos
    #//  Input :         Position
    #//  Output :        Nothing
    #//  Description :   Used to return the node from the given position
    #//  Author :        Shubham Kiran Pawar
    #//  Date :          28/03/2026
    #//
    #////////////////////////////////////////////////////////////////////
    
    def SearchByPos(self,pos):
        
        if(pos<1 or pos>self.iCount + 1):
            print("Invalid Position")
            return
        
        temp  = self.first
        
        for i in range(1,pos):
            temp = temp.next
        
        print(f"The data at the {pos} position is :")
        print(temp.data)
        
def main():
    
    sobj = SinglyLL()
    
    sobj.InsertFirst(101)    
    sobj.InsertFirst(51)
    sobj.InsertFirst(21)
    sobj.InsertFirst(11)
    
    print("Elements of LinkedList Are : ")
    sobj.Display()
    
    print("Number of elements are : ",sobj.Count())
    
    sobj.InsertLast(111)
    sobj.InsertLast(121)

    
    print("Elements of LinkedList Are : ")
    sobj.Display()
    
    print("Number of elements are : ",sobj.Count())
    
    sobj.InsertAtPos(75,4)
    
    print("Elements of LinkedList Are : ")
    sobj.Display()
    
    print("Number of elements are : ",sobj.Count())
    
    sobj.DeleteFirst()
    
    print("Elements of LinkedList Are : ")
    sobj.Display()
    
    print("Number of elements are : ",sobj.Count())
    
    sobj.DeleteFirst()
    
    print("Elements of LinkedList Are : ")
    sobj.Display()
    
    print("Number of elements are : ",sobj.Count())
    
    sobj.DeleteLast()
    
    print("Elements of LinkedList Are : ")
    sobj.Display()
    
    print("Number of elements are : ",sobj.Count())
    
    sobj.DeleteAtPos(3)
    
    print("Elements of LinkedList Are : ")
    sobj.Display()
    
    print("Number of elements are : ",sobj.Count())
    
    sobj.SearchByPos(3)
    
if __name__ == "__main__":
    main()