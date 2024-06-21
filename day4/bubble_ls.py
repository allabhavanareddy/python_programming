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
    def bubblesort(self):
        T=self.head
        while(T.next!=None):
            t=self.head
            while t.next!=None:
                if t.data > t.next.data:
                    
                    t.data,t.next.data=t.next.data,t.data
                t=t.next
            T=T.next
            
           
l1=sll()       
l1.head=node(1)
l1.addf(3)
l1.addf(2)
l1.addf(1)
l1.addf(7)
l1.display()
l1.bubblesort()
l1.display()





'''class node:
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
    def bubblesort(self):
        T=self.head
        p=None
        while(T.next!=None):
            f=0
            t=self.head
            while t.next!=p:
                if t.data > t.next.data:
                    f=1
                    t.data,t.next.data=t.next.data,t.data
                t=t.next
            if f==0:
                break
            T=T.next
            
           
l1=sll()       
l1.head=node(1)
l1.addf(3)
l1.addf(2)
l1.addf(1)
l1.addf(7)
l1.display()
l1.bubblesort()
l1.display()'''


