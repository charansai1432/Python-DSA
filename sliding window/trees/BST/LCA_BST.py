
class Treenode:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None
        
root = Treenode(2)
root.left = Treenode(1)
root.right = Treenode(3)

p = root.left 
q = root.right 

def LCA_BST(root,p,q):
    if root is None:
        return None
    if root == p or root == q:
        return root
    left = LCA_BST(root.left,p,q)
    right = LCA_BST(root.right,p,q)
    if left and right:
        return root
    if left :
        return left 
    return right 
root = LCA_BST(root,p,q)

print(root.val)

# using the BST logic 

def LCA_BST(root,p,q):
    if root is None:
        return None
    
    if p.val < root.val and q.val < root.val:
        return LCA_BST(root.left,p,q)
    if p.val > root.val and q.val > root.val:
        return LCA_BST(root.right,p,q)
    return root
root = LCA_BST(root,p,q)
print(root.val)

