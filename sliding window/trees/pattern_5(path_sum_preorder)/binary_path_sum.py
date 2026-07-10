
# optimal solution approach 

class Treenode:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None
root = Treenode(1)
root.left = Treenode(2)
root.right = Treenode(3)
root.left.left = Treenode(4)
root.left.right = Treenode(5)

def binary_tree_path(root,path=""):
    
    if root is None:
        return 
    
    if path == "":
        path = str(root.val)
    else:
        path = path + "->" + str(root.val)
    if root.left is None and root.right is None:
        return [path]
    left = binary_tree_path(root.left,path)
    right = binary_tree_path(root.right,path)
    return left + right 
print(binary_tree_path(root))
    