'''class node:
    def __init__(self,u):
        self.head=u
        self.next=None
class sll:
    def display(self):
        t=head
        while(t!=None):
            print(t.data,end="->")
            t=t.next
    def addfront(self,x):
        if self.head==None:
            self.head=node(x)
        else:
            t=node(x)
            t.next=self.head
            self.head=t
            
l1=sll()       
head=node(10)
l1.addfront(20)
l1.addfront(30)
l1.addfront(40)
l1.addback(50)
l1.display()'''


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
    def addf(self,x):
        if self.head==None:
            self.head=node(x)
        else:
            t=node(x)
            t.next=self.head
            self.head=t
        
l1=sll()       
l1.head=node(10)
l1.addf(20)
l1.addf(30)
l1.addf(40)
l1.addf(50)
l1.display()