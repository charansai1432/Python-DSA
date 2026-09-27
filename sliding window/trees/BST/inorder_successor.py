class inorder_successor:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None
        
root = inorder_successor(8)
root.left = inorder_successor(3)
root.right = inorder_successor(10)

root.left.left = inorder_successor(1)
root.left.right = inorder_successor(6)
root.left.right.left = inorder_successor(4)
root.left.right.right = inorder_successor(7)

root.right.right = inorder_successor(14)
root.right.right.left = inorder_successor(13)

p = root.left.right #6 

def in_successor(root,p):
    
    
    # if right subtree is present for the 'p'
    if p.right is not None:
        successor = p.right
        while successor.left is not None:
            successor = successor.left
        return successor


    # in case p does not have the right subtree
    
    successor = None
    while root:
        
        if p.val < root.val:
            successor = root
            root = root.left
        else:
            root = root.right
    return successor
root = in_successor(root,p)
print(root.val)