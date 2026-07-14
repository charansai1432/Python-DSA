
# optimal solution approach 

class Treenode:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None

def issametree(root1,root2):
    if root1 is None and root2 is None:
        return True
    if root1 is None or root2 is None:
        return False
    if root1.val != root2.val:
        return False
    left_same = issametree(root1.left,root2.left)
    right_same = issametree(root1.right,root2.right)
    return left_same and right_same

def issubtree(root,subtree):
    if root is None:
        return False
    
    if issametree(root,subtree):
        return True
    left_search = issubtree(root.left,subtree)
    right_search = issubtree(root.right,subtree)
    
    return left_search or right_search



root = Treenode(1)
root.left = Treenode(2)
root.right = Treenode(3)
root.left.left = Treenode(4)
root.left.right = Treenode(5)

subtree = Treenode(2)
subtree = Treenode(4)
subtree = Treenode(5)

print(issubtree(root,subtree))     