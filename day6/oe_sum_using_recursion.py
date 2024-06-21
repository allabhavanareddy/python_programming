'''class node:
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
    def oe(self):
        os=0
        es=0
        t=self.head
        while t!=None:
            if t.data%2==0:
                es=es+t.data
            else:
                os=os+t.data
            t=t.next
        return es,os,os-es
    
l1=dll()       
l1.addback(20)
l1.addback(30)
l1.addback(40)
l1.addback(50)
l1.display()
print(l1.oe())'''   
        


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
    def evod(self,t,es,os):
         if t==None:
             return abs(es-os)
         if t.data%2==0:
             es=es+t.data
         else:
             os=os+t.data
         return self.evod(t.next,es,os)



l1=dll()       
l1.addback(20)
l1.addback(30)
l1.addback(40)
l1.addback(50)
l1.display()
print(l1.evod(l1.head,0,0))        
        
            
        
    

            
            

        
    

            
            