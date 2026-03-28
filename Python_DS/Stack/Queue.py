############################################################################
#   QUEUE 
############################################################################

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


#////////////////////////////////////////////////////////////////////
#//
#//  Function Name : main
#//  Input :         Nothing  
#//  Output :        Nothing
#//  Description :   Entry point of the program, demonstrates queue operations
#//  Author :        Shubham Kiran Pawar
#//  Date :          28/03/2026
#//
#////////////////////////////////////////////////////////////////////
def main():
    
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
    

if __name__ == "__main__":
    main()