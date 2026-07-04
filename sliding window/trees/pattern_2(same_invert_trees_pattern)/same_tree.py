# # 
# If interviewer says:

# Compare trees
# Identical trees
# Same structure
# Equal trees

# Think:

# Current node

# +

# Left subtree

# +

# Right subtree

# optimal solution 

#  both the same and invert tree ==> {VVIMP} comes under the pre-order traversal's  => here cur_node i.e root  is executed 1st  

# previous questions where post-order traversal ==> because their child's are printed 1st 

class Treenode1:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None
        
class Treenode2:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None

def same_tree(root1,root2):
    if root1 is None and root2 is None:
        return True
    if root1 is None or root2 is None:
        return False
    if root1.val != root2.val:
        return False
    
    return same_tree(root1.left,root2.left) and same_tree(root1.right,root2.right)       
      
root1 = Treenode1(1)
root1.left = Treenode1(2)
root1.right = Treenode1(3)

root2 = Treenode2(1)
root2.left = Treenode2(2)
root2.right = Treenode2(3)
print(same_tree(root1,root2))