
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
    def back(self):
        f=self.head
        s=self.head
        while f!=None:
            f=f.next.next
            s=s.next
        self.tail.next=self.head
        self.head.prev=self.tail
       
        t1=s.prev
        t1.next=None
        s.prev=None
        self.head=s
        self.tail=t1

    
        
    '''def back(self):
        f=self.head
        s=self.head
        while f!=None:
            f=f.next.next
            s=s.next
        t=self.head
        t1=s
        while t1!=None:
            t.data,t1.data=t1.data,t.data
            t1=t.next
            t=t.next'''
    
        
l1=dll()       
l1.addfront(20)
l1.addfront(30)
l1.addfront(40)
l1.addfront(50)
l1.display()
l1.back()
l1.display()



        
        
            
        
    

            
            
        
        
        




