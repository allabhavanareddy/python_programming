#method to print length of linkedlist is even or odd

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
    def eo(self):
        t=self.head
        c=0
        while t!=None:
            c=c+1
            t=t.next
        return c
        t=self.head
        for i in range(c):
            if i%2==0:
                print("even")
            else:
                print("odd")
            
l1=sll()       
head=node(10)
l1.addf(20)
l1.addf(30)
l1.addf(40)
l1.display()
l1.eo()'''


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
    def eo(self):
        t=self.head
        s=self.head
        f=self.head
        while  (f!=None) and (f.next!=None):
            s=s.next
            f=f.next.next
        if f==None:
            print("even")
        else:
            print("odd")
        
l1=sll()       
l1.head=node(10)
l1.addf(20)
l1.addf(30)
l1.addf(40)
l1.display()
l1.eo()
