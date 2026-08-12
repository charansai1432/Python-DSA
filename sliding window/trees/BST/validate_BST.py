class Treenode:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None
        
root = Treenode(2)
root.left = Treenode(1)
root.right = Treenode(3)

def validate_BST(root,min_val,max_val):
    if root is None:
        return True
    
    if root.val <= min_val or root.val >= max_val:
        return False
    
    left = validate_BST(root.left,min_val,root.val)
    right = validate_BST(root.right,root.val,max_val)
    
    return left and right

print(validate_BST(root,float('-inf'),float('inf')))            