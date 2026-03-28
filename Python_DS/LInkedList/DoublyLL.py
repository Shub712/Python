############################################################################
#   DOUBLY LINEAR LINKED LIST
############################################################################

class DoublyLLNode:
    def __init__(self, Value):
        self.data = Value
        self.next = None
        self.prev = None


class DoublyLL:
    
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
    def InsertFirst(self, no):
        newn = DoublyLLNode(no)
        
        if(self.first == None):
            self.first = newn 
        else:
            newn.next = self.first
            self.first.prev = newn
            self.first = newn
        
        self.iCount = self.iCount + 1
    

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
    def InsertLast(self, no):
        
        newn = DoublyLLNode(no)
        
        if(self.first == None):
            self.first = newn
        else:
            temp = self.first
            while(temp.next != None):
                temp = temp.next
                
            newn.prev = temp
            temp.next = newn
        
        self.iCount = self.iCount + 1
            

    #////////////////////////////////////////////////////////////////////
    #//
    #//  Function Name : InsertAtPos
    #//  Input :         Data of Node, Position  
    #//  Output :        Nothing
    #//  Description :   Used to insert node at specific position
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
            newn = DoublyLLNode(no)
            temp = self.first
            
            for i in range(1, pos-1):
                temp = temp.next
            
            newn.next = temp.next
            temp.next.prev = newn
            
            temp.next = newn
            newn.prev = temp
            
            self.iCount = self.iCount + 1
    

    #////////////////////////////////////////////////////////////////////
    #//
    #//  Function Name : DeleteFirst
    #//  Input :         Nothing  
    #//  Output :        Nothing
    #//  Description :   Used to delete first node of linked list
    #//  Author :        Shubham Kiran Pawar
    #//  Date :          28/03/2026
    #//
    #////////////////////////////////////////////////////////////////////
    def DeleteFirst(self):
         
        if(self.first == None):
            print("LinkedList is Empty")
            return
        
        if(self.first.next == None):
            del self.first
            self.first = None
            self.iCount = 0
        
        else:
            self.first = self.first.next
            self.first.prev = None
            self.iCount = self.iCount - 1
    

    #////////////////////////////////////////////////////////////////////
    #//
    #//  Function Name : DeleteLast
    #//  Input :         Nothing  
    #//  Output :        Nothing
    #//  Description :   Used to delete last node of linked list
    #//  Author :        Shubham Kiran Pawar
    #//  Date :          28/03/2026
    #//
    #////////////////////////////////////////////////////////////////////
    def DeleteLast(self):
        if(self.first == None):
            print("LinkedList is Empty")
            return
        
        elif(self.first.next == None):
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
    #//  Input :         Position  
    #//  Output :        Nothing
    #//  Description :   Used to delete node at specific position
    #//  Author :        Shubham Kiran Pawar
    #//  Date :          28/03/2026
    #//
    #////////////////////////////////////////////////////////////////////
    def DeleteAtPos(self, pos):
        
        if(pos < 1 or pos > self.iCount):
            print("Invalid Position")
            return
        
        if (pos == 1):
            self.DeleteFirst()
            return
        
        elif(pos == self.iCount):
            self.DeleteLast()
        
        else:
            temp = self.first
            
            for i in range(1, pos-1):
                temp = temp.next
            
            target = temp.next
            
            temp.next = target.next
            target.next.prev = temp
            
            del target  
            self.iCount = self.iCount - 1
            

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
    #//  Function Name : Display
    #//  Input :         Nothing  
    #//  Output :        Nothing
    #//  Description :   Displays all elements of linked list
    #//  Author :        Shubham Kiran Pawar
    #//  Date :          28/03/2026
    #//
    #////////////////////////////////////////////////////////////////////
    def Display(self):
        
        temp = self.first
        
        print("\nNone <=>", end=" ")
        while(temp != None):
            print("| ", temp.data, "| <=>", end=" ")
            temp = temp.next

        print("None")
        

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
#//  Function Name : main
#//  Input :         Nothing  
#//  Output :        Nothing
#//  Description :   Entry point of the program, demonstrates all operations
#//  Author :        Shubham Kiran Pawar
#//  Date :          28/03/2026
#//
#////////////////////////////////////////////////////////////////////

def main():
    
    dobj = DoublyLL()
    
    dobj.InsertFirst(101)
    dobj.InsertFirst(51)
    dobj.InsertFirst(21)
    dobj.InsertFirst(11)
    
    print("Number of elements are in the linkedlist : ", dobj.Count())
    dobj.Display()
    
    dobj.InsertLast(70)
    dobj.InsertLast(75)
    dobj.InsertLast(80)

    print("Number of elements are in the linkedlist : ", dobj.Count())
    dobj.Display()
    
    dobj.InsertAtPos(65,3)
    dobj.InsertAtPos(95,6)
    
    print("Number of elements are in the linkedlist : ", dobj.Count())
    dobj.Display()
    
    dobj.DeleteFirst()
    
    print("Number of elements are in the linkedlist : ", dobj.Count())
    dobj.Display()
    
    dobj.DeleteLast()
    
    print("Number of elements are in the linkedlist : ", dobj.Count())
    dobj.Display()
    
    dobj.DeleteAtPos(3)
    
    print("Number of elements are in the linkedlist : ", dobj.Count())
    dobj.Display()


# Entry point check
if __name__ == "__main__":
    main()