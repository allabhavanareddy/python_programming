class node:
    def __init__(self, u):
        self.data = u
        self.left = None
        self.right = None

class tree:
    def __init__(self):
        self.root = None

    def insert(self,root,x):
        if self.root is None:
            self.root=node(x)
            return self.root
        if root==None:
            return node(x)
        elif root.data>x:
            root.left=self.insert(root.left,x)
        else:
           root.right=self.insert(root.right,x)
        return root
           
           
    def inorder(self,root):
        if root :
            self.inorder(root.left)
            print(root.data,end="->")
            self.inorder(root.right)
    
    def leaf(self,root):
        if root is None:
            return 0
        if root.left==None and root.left==None:
            return root.data
        return self.leaf(root.left),self.leaf(root.right)
 
        
            
t1=tree()
t1.insert(t1.root,10)
t1.insert(t1.root,5)
t1.insert(t1.root,20)
t1.insert(t1.root,2)
t1.insert(t1.root,7)

t1.inorder(t1.root)
print()

print(t1.leaf(t1.root))

    



