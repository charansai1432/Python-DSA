# optimal solution 

class Treenode:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None
        
def balanced_tree(root):
    if root is None:
        return 0
    
    l_height = balanced_tree(root.left)
    
    if l_height == -1:                                            # return -1 which indicates that it's not a balanced tree 
        return -1
    
    r_height = balanced_tree(root.right)
    if r_height == -1:
        return -1
    
    if abs(l_height - r_height) > 1:
        return -1
    
    # FIX: Return the actual height of this subtree to the parent
    return 1 + max(l_height, r_height)
    # if abs(l_height - r_height) == 1:
    #     return True 
    # return False
root = Treenode(1)
root.left = Treenode(2)
root.right = Treenode(3)
root.left.left = Treenode(4)
root.left.right = Treenode(5)
balanced = balanced_tree(root) != -1
print(balanced)



# To fix this without writing two separate, slow functions, we make one single integer do two jobs:

# Job 1 (Height): If a subtree is balanced, it returns its actual height (e.g., 1, 2, 3) using 1 + max(l_height, r_height). T
# he parent uses this number to check its own balance.

# Job 2 (The Flag): If a subtree is unbalanced, it returns -1. The moment a parent sees -1, it stops calculating and just passes -1 all the way to the top.


# if left == -1:
#     return -1

# Meaning:

# My left subtree is already unbalanced.

# So I don't need to continue.