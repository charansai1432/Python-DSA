
# optimal solution 

class Treenode:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None
        
def count_nodes(root):
    if root is None:
        return 0
    left = count_nodes(root.left)
    right = count_nodes(root.right)
    return 1 + left + right       
        
        
root = Treenode(1)
root.left = Treenode(2)
root.right = Treenode(3)
root.left.left = Treenode(4)
root.left.right = Treenode(5)

print(count_nodes(root))