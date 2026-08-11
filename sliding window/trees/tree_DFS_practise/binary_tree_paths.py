
class Treenode:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None
        
def binary_tree_paths(root,path=None,result=None):
    
    if result is None:
        result = []
     
    if path is None:
        path = []
    
    if root is None:
        return result 
    
    path.append(str(root.val))
    
    if root.left is None and root.right is None:
        return result.append("->".join(path))
    
    
    binary_tree_paths(root.left,path,result)    
    binary_tree_paths(root.right,path,result)
    
    path.pop()
    
    return result 
root = Treenode(1)
root.left =  Treenode(2)
root.right = Treenode(3)

root.left.left = Treenode(4)
root.left.right = Treenode(5)

root.right.left = Treenode(6)
print(binary_tree_paths(root))