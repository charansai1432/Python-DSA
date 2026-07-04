
# optimal solution 


class Treenode:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None
        
def tree_sum(root):
    if root is None:
        return 0 
    
    left_sum = tree_sum(root.left)
    right_sum = tree_sum(root.right)
    return left_sum+right_sum+root.val
             
root = Treenode(1)
root.left = Treenode(2)
root.right = Treenode(3)
root.left.left = Treenode(4)
root.left.right = Treenode(5)
print(tree_sum(root))