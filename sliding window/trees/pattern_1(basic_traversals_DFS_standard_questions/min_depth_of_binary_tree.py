# optimal solution approach

class Treenode:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None

def min_height_of_BT(root):
    if root is None:
        return 0
    
    if root.left is None:
        return 1 + min_height_of_BT(root.right)
    
    if root.right is None:
        return  1 + min_height_of_BT(root.left)
    
    left_depth = min_height_of_BT(root.left)
    right_depth = min_height_of_BT(root.right)
    
    return 1 + min(left_depth,right_depth)
root = Treenode(1)
root.left = Treenode(2)
root.right = Treenode(3)

root.left.left = Treenode(4)
root.left.right = Treenode(5)

root.right.left = Treenode(6)
print(min_height_of_BT(root))