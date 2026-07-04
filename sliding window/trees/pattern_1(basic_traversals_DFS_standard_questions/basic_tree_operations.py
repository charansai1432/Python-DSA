

# In tree problems we mostly dont have the brute force solution 

# only for the few programs we have the brute force approach ==> not all programs have the brute force soutions only few progrmas have that one


# optimal solution 

class Treenode:
    def __init__(self,val):
        self.val = val 
        self.left = None
        self.right = None
        
        
def preorder(root):                   # root -> left -> right 
            
    if root is None:
        return 
    
    print(root.val,end = " ")
    preorder(root.left)
    preorder(root.right)    

def inorder(root):                  # left -> root -> right 
    if root is None:
        return 
    inorder(root.left)
    print(root.val,end = " ")
    inorder(root.right)

def postorder(root):            # left -> right -> root
    if root is None:
        return 
    postorder(root.left)
    postorder(root.right)
    print(root.val,end = " ")
    
root = Treenode(1)
root.left = Treenode(2)
root.right = Treenode(3)
root.left.left =  Treenode(4)
root.left.right = Treenode(5)
root.right.left = Treenode(6)
root.right.right = Treenode(7)

print("preorder")
preorder(root)
print()


print("inorder")
inorder(root)
print()

print("postorder")
postorder(root)
print()

