

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
    '''def display(self):
        t=self.tail
        while(t!=None):
            print(t.data,end="->")
            t=t.prev
        print()'''
    '''def addfront(self,x):
        if self.head==None:
            self.head=node(x)
            self.tail=self.head
        else:
            t=node(x)
            t.next=self.head
            self.head.prev=t
            self.head=t'''
    def addfront(self,x):
        if self.head==None:
            self.head=node(x)
            self.tail=self.head
        else:
            
            t=node(x)
            t.next=self.head
            self.head.prev=t.next
            self.head=t
l1=dll()       
l1.addfront(20)
l1.addfront(30)
l1.addfront(40)
l1.addfront(50)
l1.display()

        
        
            
        
    

            
            
        
        
        
