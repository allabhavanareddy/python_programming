'''class node:
    def __init__(self,u):
        self.data=u
        self.next=None
a=node(10)
b=node(20)
print(a.data,a.next)#10,None
print(b.data,b.next)#20,None

--------------------------------
class node:
    def __init__(self,u):
        self.data=u
        self.next=None
head=node(10)
head.next=node(20)
head.next.next=node(30)


print(head.data)
print(head.next.data)
print(head.next.next.data)
------------------------------'''
'''class node:
    def __init__(self,u):
        self.data=u
        self.next=None
head=node(10)
head.next=node(20)
head.next.next=node(30)
t=head
while(t!=None):
    print(t.data)
    t=t.next'''

#add node at back
class node:
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
l1.display()