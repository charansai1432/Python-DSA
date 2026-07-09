

class Treenode:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None
        
def path_sum(root,target_sum):
    if root is None:
        return False
    
    target_sum -= root.val
    
    if root.left is None and root.right is None:
        return target_sum == 0 
    
    return (path_sum(root.left,target_sum) or path_sum(root.right,target_sum))

root = Treenode(5)
root.left = Treenode(4)
root.right = Treenode(8)

root.left.left = Treenode(11)
root.left.left.left = Treenode(7)   # 7 is the left child of 11
root.left.left.right = Treenode(2)  # 2 is the right child of 11

root.right.left = Treenode(13)
root.right.right = Treenode(4)
print(path_sum(root,17))