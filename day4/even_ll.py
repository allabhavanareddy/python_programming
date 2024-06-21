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
    def addback(self,x):
        t=self.head
        while(t.next!=None):
            t=t.next
        t.next=node(x)
    def addeven(self):
        t=self.head
        s=0
        while(t!=None):
            if t.data%2==0:
                s=s+t.data
            t=t.next
        print(s)
        
l1=sll()

l1.head=node(10)
l1.addback(20)
l1.addback(30)
l1.addback(40)
l1.addback(50)

l1.display()
print()
l1.addeven()