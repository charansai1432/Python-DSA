
# optimal solution 

class Treenode:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None
root = Treenode(1)
root.left = Treenode(2)
root.right = Treenode(3)
root.left.left = Treenode(4)
root.left.right= Treenode(5)


def diameter_of_tree(root):
    diameter = 0 
    def height_of_left_right_tree(root):
        nonlocal diameter
        if root is None:
            return 0
        l_height = height_of_left_right_tree(root.left)
        r_height = height_of_left_right_tree(root.right)
        diameter = max(diameter,l_height+r_height)
        return 1 + max(l_height,r_height)
    height_of_left_right_tree(root)
    return diameter


print(diameter_of_tree(root))
# here the inside function does 2 things 
    # 1. update the global answer 
    # 2. return the something for the parent 
    
    
# Return values are for the parent. 
# Global variables are for the final answer.


# Pattern Recognition

# When interviewer asks:

# Diameter
# Maximum path
# Best answer in tree
# Global maximum

# Think:

# Return information

# +

# Maintain global answer