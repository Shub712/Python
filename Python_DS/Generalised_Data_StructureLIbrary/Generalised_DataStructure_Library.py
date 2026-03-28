#---------------------------------------------------------------------
#   GENERALISED DATASTRUCTURE LIBRARY IN PYTHON
#---------------------------------------------------------------------

#--------------------------------------------------------------------
#   Type                Name of class for Node          Name of a class       
#--------------------------------------------------------------------
#   Singly Linear       SinglyLLNode                    SinglyLL
#   Singly Circular     SinglyCLLNode                   SinglyCLL
#   Doubly Linear       DoublyLLNode                    DoublyLL
#   Doubly Circular     DoublyCLLNode                   DoublyCLL
#   Stack               StackNode                       Stack
#   Queue               QueueNode                       Queue
#
#---------------------------------------------------------------------\
    
#----------------------------------------------------------------------------
#   SINGLY LINEAR LINKEDLIST 
#----------------------------------------------------------------------------


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

#----------------------------------------------------------------------------
#   DOUBLY LINEAR LINKEDLIST 
#----------------------------------------------------------------------------

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

#----------------------------------------------------------------------------
#   SINGLY CIRCULAR LINKEDLIST 
#----------------------------------------------------------------------------

class SinglyCLLNode:
    def __init__(self, Value):
        self.data = Value
        self.next = None


class SinglyCLL:
    
    def __init__(self):
        self.first = None
        self.last = None
        self.iCount = 0


    #////////////////////////////////////////////////////////////////////
    #//
    #//  Function Name : InsertFirst
    #//  Input :         Data of Node  
    #//  Output :        Nothing
    #//  Description :   Inserts node at the beginning of circular linked list
    #//  Author :        Shubham Kiran Pawar
    #//  Date :          28/03/2026
    #//
    #////////////////////////////////////////////////////////////////////
    def InsertFirst(self, no):
        newn = SinglyCLLNode(no)
        
        if(self.first == None and self.last == None):
            self.first = newn
            self.last = newn
            self.last.next = self.first
            
        else:
            newn.next = self.first
            self.first = newn
            self.last.next = self.first
        
        self.iCount = self.iCount + 1
        

    #////////////////////////////////////////////////////////////////////
    #//
    #//  Function Name : InsertLast
    #//  Input :         Data of Node  
    #//  Output :        Nothing
    #//  Description :   Inserts node at the end of circular linked list
    #//  Author :        Shubham Kiran Pawar
    #//  Date :          28/03/2026
    #//
    #////////////////////////////////////////////////////////////////////
    def InsertLast(self, no):
        newn = SinglyCLLNode(no)
        
        if(self.first == None and self.last == None):
            self.first = newn
            self.last = newn
            self.last.next = self.first
        
        else:
            self.last.next = newn
            self.last = newn
            self.last.next = self.first
        
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
        
        if (pos == 1):
            self.InsertFirst(no)
            return
        
        elif(pos == self.iCount + 1):
            self.InsertLast(no)
            return

        else:
            newn = SinglyCLLNode(no)
            temp = self.first
            
            for i in range(1, pos-1):
                temp = temp.next
            
            newn.next = temp.next
            temp.next = newn
            
            self.iCount = self.iCount + 1
    

    #////////////////////////////////////////////////////////////////////
    #//
    #//  Function Name : DeleteFirst
    #//  Input :         Nothing  
    #//  Output :        Nothing
    #//  Description :   Deletes first node of circular linked list
    #//  Author :        Shubham Kiran Pawar
    #//  Date :          28/03/2026
    #//
    #////////////////////////////////////////////////////////////////////
    def DeleteFirst(self):
        
        if(self.first == None and self.last == None):
            print("Linked List is Empty")
            return
        
        elif(self.first == self.last):
            del self.first
            del self.last
            self.first = None
            self.last = None
        
        else:
            self.first = self.first.next
            self.last.next = self.first
        
        self.iCount = self.iCount - 1
    

    #////////////////////////////////////////////////////////////////////
    #//
    #//  Function Name : DeleteLast
    #//  Input :         Nothing  
    #//  Output :        Nothing
    #//  Description :   Deletes last node of circular linked list
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
            temp = self.first
            
            while(temp.next != self.last):
                temp = temp.next
            
            del self.last
            self.last = temp
            self.last.next = self.first
        
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
        
        if (pos == 1):
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
            
            self.iCount = self.iCount - 1
    

    #////////////////////////////////////////////////////////////////////
    #//
    #//  Function Name : Display
    #//  Input :         Nothing  
    #//  Output :        Nothing
    #//  Description :   Displays all elements of circular linked list
    #//  Author :        Shubham Kiran Pawar
    #//  Date :          28/03/2026
    #//
    #////////////////////////////////////////////////////////////////////
    
    def Display(self):
        
        temp = self.first
        
        while True:
            print("| ", temp.data, "| -> ", end=" ")
            temp = temp.next
            
            if(temp == self.first):
                print()
                break
            

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

#----------------------------------------------------------------------------
#   DOUBLY CIRCULAR LINKEDLIST 
#----------------------------------------------------------------------------

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


#----------------------------------------------------------------------------
#   STACK 
#----------------------------------------------------------------------------

class StackNode:
    
    def __init__(self, value):
        self.data = value
        self.next = None


class Stack:
    
    def __init__(self):
        self.first = None
        self.iCount = 0
    

    #////////////////////////////////////////////////////////////////////
    #//
    #//  Function Name : Push
    #//  Input :         Data of Node  
    #//  Output :        Nothing
    #//  Description :   Inserts element at top of stack
    #//  Author :        Shubham Kiran Pawar
    #//  Date :          28/03/2026
    #//
    #////////////////////////////////////////////////////////////////////
    def Push(self, no):
        
        newn = StackNode(no)
        
        # Insert at beginning (Top of stack)
        newn.next = self.first
        self.first = newn
        
        self.iCount = self.iCount + 1
    

    #////////////////////////////////////////////////////////////////////
    #//
    #//  Function Name : Display
    #//  Input :         Nothing  
    #//  Output :        Nothing
    #//  Description :   Displays all elements of stack
    #//  Author :        Shubham Kiran Pawar
    #//  Date :          28/03/2026
    #//
    #////////////////////////////////////////////////////////////////////
    def Display(self):
        
        temp = self.first
        
        while(temp != None):
            print("| ", temp.data, " |")
            temp = temp.next
    

    #////////////////////////////////////////////////////////////////////
    #//
    #//  Function Name : Pop
    #//  Input :         Nothing  
    #//  Output :        Data of deleted node
    #//  Description :   Removes and returns top element from stack
    #//  Author :        Shubham Kiran Pawar
    #//  Date :          28/03/2026
    #//
    #////////////////////////////////////////////////////////////////////
    def Pop(self):
        
        if self.first == None:
            print("Stack is Empty")
            return
        
        value = self.first.data
        
        # Remove first node (Top element)
        self.first = self.first.next
        
        self.iCount = self.iCount - 1
        
        return value
    

    #////////////////////////////////////////////////////////////////////
    #//
    #//  Function Name : Peep
    #//  Input :         Nothing  
    #//  Output :        Data of top node
    #//  Description :   Returns top element without removing it
    #//  Author :        Shubham Kiran Pawar
    #//  Date :          28/03/2026
    #//
    #////////////////////////////////////////////////////////////////////
    def Peep(self):
        
        if(self.first == None):
            print("Stack is Empty")
            return
        
        return self.first.data
    

    #////////////////////////////////////////////////////////////////////
    #//
    #//  Function Name : Count
    #//  Input :         Nothing  
    #//  Output :        Integer
    #//  Description :   Returns total number of elements in stack
    #//  Author :        Shubham Kiran Pawar
    #//  Date :          28/03/2026
    #//
    #////////////////////////////////////////////////////////////////////
    def Count(self):
        return self.iCount

#----------------------------------------------------------------------------
#   QUEUE 
#----------------------------------------------------------------------------

class QueueNode:
    
    def __init__(self, value):
        self.data = value
        self.next = None
    

class Queue:
    
    def __init__(self):
        self.first = None
        self.last = None
        self.iCount = 0
        

    #////////////////////////////////////////////////////////////////////
    #//
    #//  Function Name : Enqueue
    #//  Input :         Data of Node  
    #//  Output :        Nothing
    #//  Description :   Inserts element at the end of queue
    #//  Author :        Shubham Kiran Pawar
    #//  Date :          28/03/2026
    #//
    #////////////////////////////////////////////////////////////////////
    def Enqueue(self, no):
        
        newn = QueueNode(no)
        
        # If queue is empty
        if(self.first == None and self.last == None):
            self.first = newn
            self.last = newn
        
        else:
            # Insert at end
            self.last.next = newn
            self.last = newn
        
        self.iCount = self.iCount + 1
    

    #////////////////////////////////////////////////////////////////////
    #//
    #//  Function Name : Dequeue
    #//  Input :         Nothing  
    #//  Output :        Data of deleted node
    #//  Description :   Removes element from front of queue
    #//  Author :        Shubham Kiran Pawar
    #//  Date :          28/03/2026
    #//
    #////////////////////////////////////////////////////////////////////
    def Dequeue(self):
         
        # If queue is empty
        if(self.first == None):
            print("Queue is Empty")
            return
        
        value = self.first.data

        # If only one node
        if(self.first == self.last):
            del self.first
            self.first = None
            self.last = None  
        
        else:
            # Move first pointer
            self.first = self.first.next
    
        self.iCount = self.iCount - 1

        return value


    #////////////////////////////////////////////////////////////////////
    #//
    #//  Function Name : Display
    #//  Input :         Nothing  
    #//  Output :        Nothing
    #//  Description :   Displays all elements of queue
    #//  Author :        Shubham Kiran Pawar
    #//  Date :          28/03/2026
    #//
    #////////////////////////////////////////////////////////////////////
    def Display(self):
        
        if(self.first == None):
            print("Queue is Empty")
            return
        
        temp = self.first
        
        while(temp != None):
            print("| ", temp.data, "|", end=" ")
            temp = temp.next
        
        print()
    

    #////////////////////////////////////////////////////////////////////
    #//
    #//  Function Name : Count
    #//  Input :         Nothing  
    #//  Output :        Integer
    #//  Description :   Returns total number of elements in queue
    #//  Author :        Shubham Kiran Pawar
    #//  Date :          28/03/2026
    #//
    #////////////////////////////////////////////////////////////////////
    def Count(self):
        return self.iCount


def main(): 
    
#----------------------------------------------------------------------------
#   SINGLY LINEAR CALLS
#----------------------------------------------------------------------------

    sll = SinglyLL()
    
    sll.InsertFirst(101)    
    sll.InsertFirst(51)
    sll.InsertFirst(21)
    sll.InsertFirst(11)
    
    print("Elements of LinkedList Are : ")
    sll.Display()
    
    print("Number of elements are : ",sll.Count())
    
    sll.InsertLast(111)
    sll.InsertLast(121)

    
    print("Elements of LinkedList Are : ")
    sll.Display()
    
    print("Number of elements are : ",sll.Count())
    
    sll.InsertAtPos(75,4)
    
    print("Elements of LinkedList Are : ")
    sll.Display()
    
    print("Number of elements are : ",sll.Count())
    
    sll.DeleteFirst()
    
    print("Elements of LinkedList Are : ")
    sll.Display()
    
    print("Number of elements are : ",sll.Count())
    
    sll.DeleteFirst()
    
    print("Elements of LinkedList Are : ")
    sll.Display()
    
    print("Number of elements are : ",sll.Count())
    
    sll.DeleteLast()
    
    print("Elements of LinkedList Are : ")
    sll.Display()
    
    print("Number of elements are : ",sll.Count())
    
    sll.DeleteAtPos(3)
    
    print("Elements of LinkedList Are : ")
    sll.Display()
    
    print("Number of elements are : ",sll.Count())
    
    sll.SearchByPos(3)
    
#----------------------------------------------------------------------------
#   DOUBLY LINEAR CALLS
#----------------------------------------------------------------------------
    dllobj = DoublyLL()
    
    dllobj.InsertFirst(101)
    dllobj.InsertFirst(51)
    dllobj.InsertFirst(21)
    dllobj.InsertFirst(11)
    
    print("Number of elements are in the linkedlist : ", dllobj.Count())
    dllobj.Display()
    
    dllobj.InsertLast(70)
    dllobj.InsertLast(75)
    dllobj.InsertLast(80)

    print("Number of elements are in the linkedlist : ", dllobj.Count())
    dllobj.Display()
    
    dllobj.InsertAtPos(65,3)
    dllobj.InsertAtPos(95,6)
    
    print("Number of elements are in the linkedlist : ", dllobj.Count())
    dllobj.Display()
    
    dllobj.DeleteFirst()
    
    print("Number of elements are in the linkedlist : ", dllobj.Count())
    dllobj.Display()
    
    dllobj.DeleteLast()
    
    print("Number of elements are in the linkedlist : ", dllobj.Count())
    dllobj.Display()
    
    dllobj.DeleteAtPos(3)
    
    print("Number of elements are in the linkedlist : ", dllobj.Count())
    dllobj.Display()

#----------------------------------------------------------------------------
#   SINGLY CIRCULAR CALLS
#----------------------------------------------------------------------------
    sclobj = SinglyCLL()
    
    sclobj.InsertFirst(101)
    sclobj.InsertFirst(51)
    sclobj.InsertFirst(21)
    sclobj.InsertFirst(11)
    
    print("The Elements in the linkedlist are : ", sclobj.Count())
    sclobj.Display()
    
    sclobj.InsertLast(20)
    sclobj.InsertLast(30)
    sclobj.InsertLast(40)
    sclobj.InsertLast(50)
    
    print("The Elements in the linkedlist are : ", sclobj.Count())
    sclobj.Display()
    
    sclobj.InsertAtPos(98,3)
    
    print("The Elements in the linkedlist are : ", sclobj.Count())
    sclobj.Display()
    
    sclobj.DeleteFirst()
    
    print("The Elements in the linkedlist are : ", sclobj.Count())
    sclobj.Display()
    
    sclobj.DeleteLast()
    
    print("The Elements in the linkedlist are : ", sclobj.Count())
    sclobj.Display()  
    
    sclobj.DeleteAtPos(4)
    
    print("The Elements in the linkedlist are : ", sclobj.Count())
    sclobj.Display()  
    
#----------------------------------------------------------------------------
#   DOUBLY CIRCULAR CALLS
#----------------------------------------------------------------------------
    dclobj = DoublyCLL()
    
    dclobj.InsertFirst(101)
    dclobj.InsertFirst(51)
    dclobj.InsertFirst(21)
    dclobj.InsertFirst(11)
    
    dclobj.Display()
    print("The Number of nodes in the linked list : ", dclobj.Count())
    
    dclobj.InsertLast(10)
    dclobj.InsertLast(20)
    dclobj.InsertLast(30)
    dclobj.InsertLast(40)
    
    dclobj.Display()
    print("The Number of nodes in the linked list : ", dclobj.Count())
    
    dclobj.InsertAtPos(58,4)
    
    dclobj.Display()
    print("The Number of nodes in the linked list : ", dclobj.Count())
    
    dclobj.DeleteFirst()

    dclobj.Display()
    print("The Number of nodes in the linked list : ", dclobj.Count())
    
    dclobj.DeleteLast()
    
    dclobj.Display()
    print("The Number of nodes in the linked list : ", dclobj.Count())
    
    dclobj.DeleteAtPos(4)
    
    dclobj.Display()
    print("The Number of nodes in the linked list : ", dclobj.Count())
    
    dclobj.SearchByPos(5)
    
#----------------------------------------------------------------------------
#   STACK CALLS
#----------------------------------------------------------------------------

    stobj = Stack()
    
    stobj.Push(53)
    stobj.Push(51)
    stobj.Push(21)
    stobj.Push(11)
    
    print("The Nodes are in the stack are : ", stobj.Count())
    stobj.Display()
    
    print("Deleted Node : ", stobj.Pop())
    
    print("The Nodes are in the stack are : ", stobj.Count())
    stobj.Display()
    
    print("First Node is : ", stobj.Peep())
    
#----------------------------------------------------------------------------
#   QUEUE CALLS
#----------------------------------------------------------------------------

    qobj = Queue()
    
    qobj.Enqueue(101)
    qobj.Enqueue(51)
    qobj.Enqueue(21)
    qobj.Enqueue(11)
    
    qobj.Display()
    
    print("Count of nodes in the queue : ", qobj.Count())
    
    print("Deleted Node is : ", qobj.Dequeue())
    
    qobj.Display()    
    print("Count of nodes in the queue : ", qobj.Count())
    
    print("Deleted Node is : ", qobj.Dequeue(), "Remaining Nodes are : ", qobj.Count())
    print("Deleted Node is : ", qobj.Dequeue(), "Remaining Nodes are : ", qobj.Count())
    print("Deleted Node is : ", qobj.Dequeue(), "Remaining Nodes are : ", qobj.Count())
    print("Deleted Node is : ", qobj.Dequeue(), "Remaining Nodes are : ", qobj.Count())

if __name__ ==  "__main__":
    main()