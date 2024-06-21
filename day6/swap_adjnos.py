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
    def addback(self,x):
        if  self.head==None:
            self.head=node(x)
            self.tail=self.head
        else:
            t=node(x)
            self.tail.next=t
            t.prev=self.tail
            self.tail=t
    def swapalternate(self):
        '''
        t=self.head
        while(t!=None and t.next!=None):
            t.data,t.next.data=t.next.data,t.data
            t=t.next.next
        '''
        t=self.head
        t1=self.head.next
        t3=None
        c=0
        while(t!=None):
            t.next=t1.next
            t1.next=t
            t1.prev=t3
            t.prev=t1
           
            if(c==0):
                self.head=t1
                c=1
            else:
                t3.next=t1
            t,t1=t1,t
            t3=t1
            
            if(t1.next!=None):
                t1=t1.next.next
            t=t.next.next
l1=dll()       
l1.addback(20)
l1.addback(30)
l1.addback(40)
l1.addback(50)
l1.display()
l1.swapalternate()
l1.display()
        
        
            
        
    

            
            
        
        
        

