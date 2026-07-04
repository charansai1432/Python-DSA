
# optimal solution 


# optimal solution 


class Treenode:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None
        
def max_val_in_tree(root):
    if root is None:
        return float('-inf')
    left_max_val = max_val_in_tree(root.left)
    right_max_val = max_val_in_tree(root.right)
    return max(root.val,left_max_val,right_max_val)
root = Treenode(1)
root.left = Treenode(2)
root.right = Treenode(3)
root.left.left = Treenode(4)
root.left.right = Treenode(5)
print(max_val_in_tree(root))