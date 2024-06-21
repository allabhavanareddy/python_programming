#check list is palindrome or not using recurrsion
class node:
    def __init__(self,u):
        self.data=u
        self.next=None
        self.prev=None
class dll:
    def __init__(self):
        self.head=None
        self.tail=None
    def display(self):
        t=self.head
        while(t!=None):
            print(t.data,end="->")
            t=t.next
        print()
   
    def addfront(self,x):
        if self.head==None:
            self.head=node(x)
            self.tail=self.head
        else:
            t=node(x)
            t.next=self.head
            self.head.prev=t
            self.head=t
    def pal(self):
        t=self.head
        t1=self.tail
        while t!=t1 and t!=t1.next:
            if t.data!=t1.data:
                return 0
                
            t=t.next
            t1=t1.prev
        return 1
l1=dll()       
l1.addfront(20)
l1.addfront(30)
l1.addfront(20)
l1.addfront(30)
l1.addfront(20)
l1.addfront(30)
l1.addfront(20)
l1.display()
print(l1.pal())



        
        
            
        
    

            
            
        
        
        



