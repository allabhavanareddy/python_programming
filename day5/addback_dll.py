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
    def addback(self,x):
        if  self.head==None:
            self.head=node(x)
            self.tail=self.head
        else:
            '''self.tail.next=node(x)
            self.tail.next.prev=self.tail
            self.tail.next=tail.next'''
            t=node(x)
            self.tail.next=t
            t.prev=self.tail
            self.tail=t
   
l1=dll()       
l1.addback(20)
l1.addback(30)
l1.addback(40)
l1.addback(50)
l1.display()
        
        
            
        
    

            
            
        
        
        