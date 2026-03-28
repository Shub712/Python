############################################################################
#   STACK
############################################################################

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


#////////////////////////////////////////////////////////////////////
#//
#//  Function Name : main
#//  Input :         Nothing  
#//  Output :        Nothing
#//  Description :   Entry point of the program, demonstrates stack operations
#//  Author :        Shubham Kiran Pawar
#//  Date :          28/03/2026
#//
#////////////////////////////////////////////////////////////////////
def main():
    
    sobj = Stack()
    
    sobj.Push(53)
    sobj.Push(51)
    sobj.Push(21)
    sobj.Push(11)
    
    print("The Nodes are in the stack are : ", sobj.Count())
    sobj.Display()
    
    print("Deleted Node : ", sobj.Pop())
    
    print("The Nodes are in the stack are : ", sobj.Count())
    sobj.Display()
    
    print("First Node is : ", sobj.Peep())
    

if __name__ == "__main__":
    main()