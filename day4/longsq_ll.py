class node:
    def __init__(self,u):
        self.data=u
        self.next=None
class sll:
    def __init__(self):
        self.head=None
    def display(self):
        t=self.head
        while(t!=None):
            print(t.data,end="->")
            t=t.next
        print()
    def addf(self,x):
        if self.head==None:
            self.head=node(x)
        else:
            t=node(x)
            t.next=self.head
            self.head=t
    def long(self):
        t=self.head
        c=1
        m=0
        while(t.next!=None):
            if t.data==(t.next.data-1):
                c=c+1
                
            else:
                if c>m:
                    m=c
                c=1
            t=t.next
        if c>m:
            m=c
        print(m)
        
            
l1=sll()       
l1.head=node(7)
l1.addf(4)
l1.addf(3)
l1.addf(2)
l1.addf(1)

l1.display()
print()
l1.long()


