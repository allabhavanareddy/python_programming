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
    def prime(self,t,c):
        if t==None:
            return c
        def pnp(s,n):
            if s>=(n//2)+1:
                return 1
            if n%s==0:
                return 0
            return pnp(s+1,n)
        if pnp(2,t.data):
            c=c+1 
        return self.prime(t.next,c)
                
l1=dll()       
l1.addback(2)
l1.addback(3)
l1.addback(40)
l1.addback(50)
l1.display()
print(l1.prime(l1.head,0))        
        
            
        
    

            
            

        
    

            
            