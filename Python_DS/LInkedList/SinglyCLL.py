############################################################################
#   SINGLY CIRCULAR LINKED LIST 
############################################################################

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
    
    sobj = SinglyCLL()
    
    sobj.InsertFirst(101)
    sobj.InsertFirst(51)
    sobj.InsertFirst(21)
    sobj.InsertFirst(11)
    
    print("The Elements in the linkedlist are : ", sobj.Count())
    sobj.Display()
    
    sobj.InsertLast(20)
    sobj.InsertLast(30)
    sobj.InsertLast(40)
    sobj.InsertLast(50)
    
    print("The Elements in the linkedlist are : ", sobj.Count())
    sobj.Display()
    
    sobj.InsertAtPos(98,3)
    
    print("The Elements in the linkedlist are : ", sobj.Count())
    sobj.Display()
    
    sobj.DeleteFirst()
    
    print("The Elements in the linkedlist are : ", sobj.Count())
    sobj.Display()
    
    sobj.DeleteLast()
    
    print("The Elements in the linkedlist are : ", sobj.Count())
    sobj.Display()  
    
    sobj.DeleteAtPos(4)
    
    print("The Elements in the linkedlist are : ", sobj.Count())
    sobj.Display()  


if __name__ == "__main__":
    main()