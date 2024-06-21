
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
    def search(self,x):
        t=self.head
        while(t!=None):
            if t.data==x:
                print("found")
            t=t.next
        print("not found")
        
l1=sll()       
l1.head=node(10)
l1.addf(20)
l1.addf(30)
l1.addf(40)
l1.addf(50)
l1.display()
l1.search(80)