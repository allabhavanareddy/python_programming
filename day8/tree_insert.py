class node:
    def __init__(self, value):
        self.data = value
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def insert(self,t,x):
        if t==None:
            t==node(x)
            return t
        if x < t.data:
            t.left = self.insert(t.left,x)
        else:
            t.right = self.insert(t.right,x)
        return t


    def inorder(self,t):
       
        if t!=None:
            self.inorder(t.left)
            print(t.data, end="->")
            self.inorder(t.right)

bst = BST()
bst.insert(bst.root, 20)
bst.insert(bst.root, 10)
bst.insert(bst.root, 40)
bst.insert(bst.root, 50)
bst.inorder(t)
print()