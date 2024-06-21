#add elemnts of linked list
class node:
    def __init__(self,u):
        self.data=u
        self.next=None
class sll:
    def display(self):
        s=0
        t=head
        while(t!=None):
            s=s+t.data
            t=t.next
        print(s)
l1=sll()       
head=node(10)
head.next=node(20)
head.next.next=node(30)
l1.display()