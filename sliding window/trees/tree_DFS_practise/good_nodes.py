class Treenode:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None
        
def good_nodes(root,max_val = float('-inf')):
    
    count = 0
    
    if root is None:
        return 0
    
    if root.val >= max_val:
        count += 1
        
    max_val = max(max_val,root.val)
        
    left_count = good_nodes(root.left)      
    right_count = good_nodes(root.right)
    
    return count + left_count + right_count  
        
        
        
        
root = Treenode(1)
root.left = Treenode(2)
root.right = Treenode(3)

root.left.left = Treenode(4)
root.left.right = Treenode(5)

root.right.left = Treenode(6)
print(good_nodes(root))