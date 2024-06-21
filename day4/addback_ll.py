
'''class node:
    def __init__(self,u):
        self.data=u
        self.next=None
class sll:
    def display(self):
        t=head
        while(t!=None):
            print(t.data)
            t=t.next
l1=sll()       
head=node(10)
head.next=node(20)
head.next.next=node(30)
t=head
while(t.next!=None):
    t=t.next
t.next=node(50)
l1.display()'''

class node:
    def __init__(self,u):
        self.data=u
        self.next=None
class sll:
    def display(self):
        t=head
        while(t!=None):
            print(t.data,end="->")
            t=t.next
    def addback(self,x):
        t=head
        while(t.next!=None):
            t=t.next
        t.next=node(x)
        
l1=sll()       
head=node(10)
l1.addback(20)
l1.addback(30)
l1.addback(40)
l1.addback(50)
l1.display()