############################################################################
#   DOUBLY CIRCULAR LINKED LIST 
############################################################################

class DoublyCLLNode:
    
    def __init__(self, value):
        self.data = value
        self.next = None
        self.prev = None


class DoublyCLL:
    
    def __init__(self):
        self.first = None
        self.last  = None
        self.iCount = 0
    

    #////////////////////////////////////////////////////////////////////
    #//
    #//  Function Name : InsertFirst
    #//  Input :         Data of Node  
    #//  Output :        Nothing
    #//  Description :   Inserts node at beginning of doubly circular list
    #//  Author :        Shubham Kiran Pawar
    #//  Date :          28/03/2026
    #//
    #////////////////////////////////////////////////////////////////////
    def InsertFirst(self, no):
        
        newn = DoublyCLLNode(no)
        
        if(self.first == None and self.last == None):
            self.first = newn
            self.last = newn

        else:
            newn.next = self.first
            self.first.prev = newn
            self.first = newn
            
        # Maintain circular links
        self.last.next = self.first
        self.first.prev = self.last
            
        self.iCount = self.iCount + 1
            

    #////////////////////////////////////////////////////////////////////
    #//
    #//  Function Name : InsertLast
    #//  Input :         Data of Node  
    #//  Output :        Nothing
    #//  Description :   Inserts node at end of doubly circular list
    #//  Author :        Shubham Kiran Pawar
    #//  Date :          28/03/2026
    #//
    #////////////////////////////////////////////////////////////////////
    def InsertLast(self, no):
         
        newn = DoublyCLLNode(no)
        
        if(self.first == None or self.last == None):
            self.first = newn
            self.last = newn
        
        else:
            self.last.next = newn
            newn.prev = self.last
            self.last = newn
        
        # Maintain circular links
        self.last.next = self.first
        self.first.prev = self.last
        
        self.iCount = self.iCount + 1
    

    #////////////////////////////////////////////////////////////////////
    #//
    #//  Function Name : InsertAtPos
    #//  Input :         Data of Node, Position  
    #//  Output :        Nothing
    #//  Description :   Inserts node at specific position
    #//  Author :        Shubham Kiran Pawar
    #//  Date :          28/03/2026
    #//
    #////////////////////////////////////////////////////////////////////
    def InsertAtPos(self, no, pos):
        
        if(pos < 1 or pos > self.iCount + 1):
            print("Invalid Position")
            return
        
        if(pos == 1):
            self.InsertFirst(no)
            return
        
        elif(pos == self.iCount + 1):
            self.InsertLast(no)
            return
        
        else:
            newn = DoublyCLLNode(no)
            temp = self.first 
            
            for i in range(1, pos-1):
                temp = temp.next
            
            newn.next = temp.next
            newn.prev = temp
            
            temp.next.prev = newn
            temp.next = newn
            
            self.iCount = self.iCount + 1
    

    #////////////////////////////////////////////////////////////////////
    #//
    #//  Function Name : DeleteFirst
    #//  Input :         Nothing  
    #//  Output :        Nothing
    #//  Description :   Deletes first node of doubly circular list
    #//  Author :        Shubham Kiran Pawar
    #//  Date :          28/03/2026
    #//
    #////////////////////////////////////////////////////////////////////
    def DeleteFirst(self):
        
        if(self.first == None and self.last == None):
            print("Linked List is empty")
            return
        
        elif(self.first == self.last):
            del self.first
            del self.last
            self.first = None
            self.last = None
        
        else:
            self.first = self.first.next
            
            # Maintain circular links
            self.last.next = self.first
            self.first.prev = self.last
        
        self.iCount = self.iCount - 1
        

    #////////////////////////////////////////////////////////////////////
    #//
    #//  Function Name : DeleteLast
    #//  Input :         Nothing  
    #//  Output :        Nothing
    #//  Description :   Deletes last node of doubly circular list
    #//  Author :        Shubham Kiran Pawar
    #//  Date :          28/03/2026
    #//
    #////////////////////////////////////////////////////////////////////
    def DeleteLast(self):
        
        if(self.first == None and self.last == None):
            print("Linked List is empty")
            return
        
        elif(self.first == self.last):
            del self.first
            del self.last
            self.first = None
            self.last = None
        
        else:
            self.last = self.last.prev
            
            # Maintain circular links
            self.last.next = self.first
            self.first.prev = self.last
        
        self.iCount = self.iCount - 1
                

    #////////////////////////////////////////////////////////////////////
    #//
    #//  Function Name : DeleteAtPos
    #//  Input :         Position  
    #//  Output :        Nothing
    #//  Description :   Deletes node at specific position
    #//  Author :        Shubham Kiran Pawar
    #//  Date :          28/03/2026
    #//
    #////////////////////////////////////////////////////////////////////
    def DeleteAtPos(self, pos):
        
        if(pos < 1 or pos > self.iCount):
            print("Invalid Position")
            return
        
        if(pos == 1):
            self.DeleteFirst()
            return
        
        elif(pos == self.iCount):
            self.DeleteLast()
            return
        
        else:
            temp = self.first
            
            for i in range(1, pos-1):
                temp = temp.next
            
            temp.next = temp.next.next
            temp.next.prev = temp
            
            self.iCount = self.iCount - 1
            

    #////////////////////////////////////////////////////////////////////
    #//
    #//  Function Name : Display
    #//  Input :         Nothing  
    #//  Output :        Nothing
    #//  Description :   Displays all elements of doubly circular list
    #//  Author :        Shubham Kiran Pawar
    #//  Date :          28/03/2026
    #//
    #////////////////////////////////////////////////////////////////////
    def Display(self):
        
        if(self.first == None):
            print("Linked list is empty")
            return
        
        temp = self.first
        
        print("<=>", end=" ")
        while True:
            print("|", temp.data, "| <=>", end=" ")
            temp = temp.next
            
            if temp == self.first:
                break
            
        print()
        

    #////////////////////////////////////////////////////////////////////
    #//
    #//  Function Name : SearchByPos
    #//  Input :         Position  
    #//  Output :        Nothing
    #//  Description :   Displays data at given position
    #//  Author :        Shubham Kiran Pawar
    #//  Date :          28/03/2026
    #//
    #////////////////////////////////////////////////////////////////////
    def SearchByPos(self, pos):
        
        if(pos < 1 or pos > self.iCount):
            print("Invalid Position")
            return
        
        temp = self.first
        
        for i in range(1, pos):
            temp = temp.next
        
        print(f"The data at the {pos} position is :")
        print(temp.data)
        

    #////////////////////////////////////////////////////////////////////
    #//
    #//  Function Name : Count
    #//  Input :         Nothing  
    #//  Output :        Integer
    #//  Description :   Returns total number of nodes
    #//  Author :        Shubham Kiran Pawar
    #//  Date :          28/03/2026
    #//
    #////////////////////////////////////////////////////////////////////
    def Count(self):
        return self.iCount


#////////////////////////////////////////////////////////////////////
#//
#//  Function Name : main
#//  Input :         Nothing  
#//  Output :        Nothing
#//  Description :   Entry point of the program, demonstrates all operations
#//  Author :        Shubham Kiran Pawar
#//  Date :          28/03/2026
#//
#////////////////////////////////////////////////////////////////////
def main():
    
    dobj = DoublyCLL()
    
    dobj.InsertFirst(101)
    dobj.InsertFirst(51)
    dobj.InsertFirst(21)
    dobj.InsertFirst(11)
    
    dobj.Display()
    print("The Number of nodes in the linked list : ", dobj.Count())
    
    dobj.InsertLast(10)
    dobj.InsertLast(20)
    dobj.InsertLast(30)
    dobj.InsertLast(40)
    
    dobj.Display()
    print("The Number of nodes in the linked list : ", dobj.Count())
    
    dobj.InsertAtPos(58,4)
    
    dobj.Display()
    print("The Number of nodes in the linked list : ", dobj.Count())
    
    dobj.DeleteFirst()

    dobj.Display()
    print("The Number of nodes in the linked list : ", dobj.Count())
    
    dobj.DeleteLast()
    
    dobj.Display()
    print("The Number of nodes in the linked list : ", dobj.Count())
    
    dobj.DeleteAtPos(4)
    
    dobj.Display()
    print("The Number of nodes in the linked list : ", dobj.Count())
    
    dobj.SearchByPos(5)


if __name__ == "__main__":
    main()